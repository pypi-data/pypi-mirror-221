"""
This module provides tools for creating kmz products for a CPHD type element.
"""

__classification__ = "UNCLASSIFIED"
__author__ = "Valkyrie Systems Corporation"

import logging
import os

import matplotlib.pyplot as plt
import numpy as np

from sarpy.io.kml import Document
from sarpy.geometry.geocoords import ecf_to_geodetic
import sarpy.visualization.kmz_product_creation as kpc

WGS84_SEMIMAJOR = 6378137.0
WGS84_SEMIMINOR = 6356752.314245

logger = logging.getLogger(__name__)


def ray_ellipsoid_intersection(
    semiaxis_a, semiaxis_b, semiaxis_c, pos_x, pos_y, pos_z, dir_x, dir_y, dir_z
):
    """
    Compute the intersection of a Ray with an Ellipsoid

    Parameters
    ----------
    semiaxis_a, semiaxis_b, semiaxis_b: float
        Semiaxes of the ellipsoid
    pos_x, pos_y, pos_y: float
        Ray origin
    dir_x, dir_y, dir_y: float
        Ray direction

    Returns
    -------
    intersection_x, intersection_y, intersection_z: float
        Point of intersection
    """
    # Based on https://stephenhartzell.medium.com/satellite-line-of-sight-intersection-with-earth-d786b4a6a9b6
    # >>> pos_x, pos_y, pos_z = symbols('pos_x pos_y pos_z')
    # >>> dir_x, dir_y, dir_z = symbols('dir_x dir_y dir_z')
    # >>> semiaxis_a, semiaxis_b, semiaxis_c = symbols('semiaxis_a semiaxis_b semiaxis_c')
    # >>> distance = symbols('distance')

    # >>> solutions = solve((pos_x + distance*dir_x)**2/semiaxis_a**2 + (pos_y + distance*dir_y)**2/semiaxis_b**2 + (pos_z + distance*dir_z)**2/semiaxis_c**2 - 1, distance)
    # >>> print(solutions[0])

    # black formatted
    distance = (
        -dir_x * pos_x * semiaxis_b**2 * semiaxis_c**2
        - dir_y * pos_y * semiaxis_a**2 * semiaxis_c**2
        - dir_z * pos_z * semiaxis_a**2 * semiaxis_b**2
        - semiaxis_a
        * semiaxis_b
        * semiaxis_c
        * np.sqrt(
            -(dir_x**2) * pos_y**2 * semiaxis_c**2
            - dir_x**2 * pos_z**2 * semiaxis_b**2
            + dir_x**2 * semiaxis_b**2 * semiaxis_c**2
            + 2 * dir_x * dir_y * pos_x * pos_y * semiaxis_c**2
            + 2 * dir_x * dir_z * pos_x * pos_z * semiaxis_b**2
            - dir_y**2 * pos_x**2 * semiaxis_c**2
            - dir_y**2 * pos_z**2 * semiaxis_a**2
            + dir_y**2 * semiaxis_a**2 * semiaxis_c**2
            + 2 * dir_y * dir_z * pos_y * pos_z * semiaxis_a**2
            - dir_z**2 * pos_x**2 * semiaxis_b**2
            - dir_z**2 * pos_y**2 * semiaxis_a**2
            + dir_z**2 * semiaxis_a**2 * semiaxis_b**2
        )
    ) / (
        dir_x**2 * semiaxis_b**2 * semiaxis_c**2
        + dir_y**2 * semiaxis_a**2 * semiaxis_c**2
        + dir_z**2 * semiaxis_a**2 * semiaxis_b**2
    )

    if np.isnan(distance):
        raise ValueError("Ray does not intersect ellipsoid")

    if distance < 0:
        raise ValueError("Ray points away from ellipsoid")

    return (
        pos_x + distance * dir_x,
        pos_y + distance * dir_y,
        pos_z + distance * dir_z,
    )


def ray_intersect_earth(position, direction):
    """Intersect an ECEF ray with the earth"""
    point_ecf = ray_ellipsoid_intersection(
        WGS84_SEMIMAJOR,
        WGS84_SEMIMAJOR,
        WGS84_SEMIMINOR,
        position[0],
        position[1],
        position[2],
        direction[0],
        direction[1],
        direction[2],
    )
    return point_ecf


def _create_cphd_styles(kmz_document):
    def _setpolygon(name, *, bbggrr, low_aa, low_width, high_aa, high_width, outline="1"):
        opaque = "ff"
        kmz_document.add_style(
            name + "_high",
            line_style={"color": opaque + bbggrr, "width": high_width},
            poly_style={"color": high_aa + bbggrr, "outline": str(outline)},
        )
        kmz_document.add_style(
            name + "_low",
            line_style={"color": opaque + bbggrr, "width": low_width},
            poly_style={"color": low_aa + bbggrr, "outline": str(outline)},
        )
        kmz_document.add_style_map(name, name + "_high", name + "_low")

    # iarp - intended for basic point clamped to ground
    label = {"color": "ff50c0c0", "scale": "1.0"}
    icon = {
        "color": "ff5050c0",
        "scale": "1.5",
        "icon_ref": "http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png",
    }
    kmz_document.add_style("iarp_high", label_style=label, icon_style=icon)
    label["scale"] = "0.75"
    icon["scale"] = "1.0"
    kmz_document.add_style("iarp_low", label_style=label, icon_style=icon)
    kmz_document.add_style_map("iarp", "iarp_high", "iarp_low")

    # srp position style - intended for gx track
    line = {"color": "ff50ff50", "width": "1.5"}
    label = {"color": "ffc0c0c0", "scale": "0.5"}
    icon = {
        "scale": "2.0",
        "icon_ref": "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png",
    }
    poly = {"color": "a050ff50"}
    kmz_document.add_style(
        "srp_high", line_style=line, label_style=label, icon_style=icon, poly_style=poly
    )
    line["width"] = "1.0"
    icon["scale"] = "1.0"
    poly = {"color": "7050ff50"}
    kmz_document.add_style(
        "srp_low", line_style=line, label_style=label, icon_style=icon, poly_style=poly
    )
    kmz_document.add_style_map("srp", "srp_high", "srp_low")

    _setpolygon(
        "mechanical_boresight",
        bbggrr="a00000",
        low_aa="70",
        low_width="2.0",
        high_aa="a0",
        high_width="3.5",
        outline="0",
    )

    _setpolygon(
        "electrical_boresight",
        bbggrr="a0a050",
        low_aa="70",
        low_width="2.0",
        high_aa="a0",
        high_width="3.5",
        outline="0",
    )

    _setpolygon(
        "globalimagearea",
        bbggrr="aa00ff",
        low_aa="00",
        low_width="1.0",
        high_aa="00",
        high_width="1.5",
    )

    _setpolygon(
        "channelimagearea",
        bbggrr="00aa7f",
        low_aa="70",
        low_width="1.0",
        high_aa="a0",
        high_width="1.5",
    )

    _setpolygon(
        "rcv_beam_footprint",
        bbggrr="ffaa55",
        low_aa="70",
        low_width="1.0",
        high_aa="a0",
        high_width="1.5",
    )

    _setpolygon(
        "tx_beam_footprint",
        bbggrr="0000ff",
        low_aa="70",
        low_width="1.0",
        high_aa="a0",
        high_width="1.5",
    )


def _imagearea_kml_coord(reader, imagearea_node):
    """Create KML coords of an imagearea footprint"""
    if imagearea_node.Polygon is not None:
        verts = [
            vert.get_array()
            for vert in sorted(imagearea_node.Polygon, key=lambda x: x.index)
        ]
    else:
        x1, y1 = imagearea_node.X1Y1.get_array()
        x2, y2 = imagearea_node.X2Y2.get_array()
        verts = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
    verts.append(verts[0])
    return _xy_to_kml_coord(reader, verts)


def cphd_create_kmz_view(reader, output_directory, file_stem="view"):
    """
    Create a kmz view for the reader contents.

    Parameters
    ----------
    reader : CPHDTypeReader
    output_directory : str
    file_stem : str

    Returns
    -------
    None

    Examples
    --------
    .. code-block:: python

        import logging
        logger = logging.getLogger('sarpy')
        logger.setLevel('INFO')

        import os
        import sarpy.io.phase_history
        from sarpy.visualization.cphd_kmz_product_creation import cphd_create_kmz_view

        test_root = '<root directory>'
        reader = sarpy.io.phase_history.open(os.path.join(test_root, '<file name>>'))
        cphd_create_kmz_view(reader, test_root,
                             file_stem='View-<something descriptive>')

    """

    def add_global(kmz_doc, root):
        logger.info("Adding global to kmz.")
        folder = kmz_doc.add_container(
            par=root, the_type="Folder", name="Global", description="Global Metadata"
        )
        iarp_llh = reader.cphd_meta.SceneCoordinates.IARP.LLH.get_array()
        frm = "{1:0.8f},{0:0.8f},0"  # SICD version throws away height
        coords = frm.format(*iarp_llh)
        placemark = kmz_doc.add_container(
            par=folder, name="IARP", description="IARP", styleUrl="#iarp"
        )
        kmz_doc.add_point(coords, par=placemark, altitudeMode="absolute")

        ia_coords = _imagearea_kml_coord(
            reader, reader.cphd_meta.SceneCoordinates.ImageArea
        )
        placemark = kmz_doc.add_container(
            par=folder,
            name="ImageArea",
            description="ImageArea",
            styleUrl="#globalimagearea",
        )
        kmz_doc.add_polygon(
            " ".join(ia_coords),
            par=placemark,
            name="ImageArea",
            altitudeMode="absolute",
        )

    def add_channel(kmz_doc, root, channel_name):
        channel_names = [chan.Identifier for chan in reader.cphd_meta.Data.Channels]
        channel_index = channel_names.index(channel_name)
        logger.info(f"Adding channel '{channel_name}' to kmz.")

        signal = reader.read_pvp_variable("SIGNAL", channel_name)
        if signal is None:
            num_vectors = reader.cphd_meta.Data.Channels[channel_index].NumVectors
            signal = np.ones(num_vectors)

        num_subselect = 24
        indices = np.where(signal == 1)[0]
        indices = indices[
            np.round(
                np.linspace(0, indices.size - 1, num_subselect, endpoint=True)
            ).astype(int)
        ]

        times = (
            reader.read_pvp_variable("TxTime", channel_name)[indices]
            + reader.read_pvp_variable("RcvTime", channel_name)[indices]
        ) / 2.0
        arp_pos = (
            reader.read_pvp_variable("TxPos", channel_name)[indices]
            + reader.read_pvp_variable("RcvPos", channel_name)[indices]
        ) / 2.0
        srp_pos = reader.read_pvp_variable("SRPPos", channel_name)[indices]
        collection_start = reader.cphd_meta.Global.Timeline.CollectionStart.astype(
            "datetime64[us]"
        )
        whens = collection_start + (times * 1e6).astype("timedelta64[us]")
        whens = [str(time) + "Z" for time in whens]

        time_args = {"beginTime": whens[0], "endTime": whens[-1]}

        folder = kmz_doc.add_container(
            par=root,
            the_type="Folder",
            name=f"Channel {channel_name}",
            description=f"Channel {channel_name}",
            when=whens[0],
        )
        arp_coords = ecef_to_kml_coord(arp_pos)
        placemark = kmz_doc.add_container(
            par=folder,
            name=channel_name,
            description=f"aperture position for channel {channel_name}",
            styleUrl="#arp",
            **time_args,
        )
        kmz_doc.add_gx_track(
            arp_coords,
            whens,
            par=placemark,
            extrude=True,
            tesselate=True,
            altitudeMode="absolute",
        )

        srp_coords = ecef_to_kml_coord(srp_pos)
        placemark = kmz_doc.add_container(
            par=folder,
            name="SRP",
            description=f"stabilization reference point for channel {channel_name}",
            styleUrl="#srp",
            **time_args,
        )
        kmz_doc.add_gx_track(
            srp_coords,
            whens,
            par=placemark,
            extrude=True,
            tesselate=True,
            altitudeMode="absolute",
        )

        if reader.cphd_meta.Channel.Parameters[channel_index].ImageArea is not None:
            ia_coords = _imagearea_kml_coord(
                reader, reader.cphd_meta.Channel.Parameters[channel_index].ImageArea
            )
            placemark = kmz_doc.add_container(
                par=folder,
                name="ImageArea",
                description=f"ImageArea for channel {channel_name}",
                styleUrl="#channelimagearea",
            )
            kmz_doc.add_polygon(
                " ".join(ia_coords),
                par=placemark,
                name=f"ImageArea for channel {channel_name}",
                altitudeMode="absolute",
            )

        aiming = _antenna_aiming(reader, channel_index, signal)
        antenna_folder = kmz_doc.add_container(
            the_type="Folder",
            par=folder,
            name="Antenna",
            description=f"Antenna Aiming for channel {channel_name}",
        )
        boresight_folder = kmz_doc.add_container(
            the_type="Folder",
            par=antenna_folder,
            name="Boresights",
            description=f"Boresights for channel {channel_name}",
        )
        footprint_folder = kmz_doc.add_container(
            the_type="Folder",
            par=antenna_folder,
            name="3dB Footprints",
            description=f"Beam Footprints for channel {channel_name}",
        )
        for txrcv in ("Tx", "Rcv"):
            for when in ('start', 'middle', 'end'):
                if when not in aiming[txrcv]['beam_footprint']:
                    continue  # footprint calculation must have failed
                this_footprint = aiming[txrcv]['beam_footprint'][when]

                name = f'{txrcv} beam footprint @ {when}'
                timestamp = str(collection_start + (this_footprint['time'] * 1e6).astype("timedelta64[us]")) + 'Z'
                placemark = kmz_doc.add_container(
                    par=footprint_folder,
                    name=name,
                    description=f"{name} for channel {channel_name}",
                    styleUrl=f'#{txrcv.lower()}_beam_footprint',
                    visibility=True,
                    when=timestamp,
                )
                coords = ecef_to_kml_coord(this_footprint['contour'])
                kmz_doc.add_polygon(
                    " ".join(coords), par=placemark,
                )

            for boresight_type in ("mechanical", "electrical"):
                visibility = txrcv == "Rcv"  # only display Rcv by default
                name = f"{txrcv} {boresight_type} boresight"

                on_earth_ecf = np.asarray(
                    [
                        ray_intersect_earth(apc_pos, along)
                        for apc_pos, along in zip(
                            aiming[txrcv]["apc_position"][indices],
                            aiming[txrcv]["pointing"][boresight_type][indices],
                        )
                    ]
                )

                placemark = kmz_doc.add_container(
                    par=boresight_folder,
                    name=name,
                    description=f"{name} for channel {channel_name}<br><br>Highlighted edge indicates start time",
                    styleUrl=f"#{boresight_type}_boresight",
                    visibility=visibility,
                )
                boresight_coords = ecef_to_kml_coord(on_earth_ecf)

                # complex 3d polygons don't always render nicely.  So, we'll manually triangluate it.
                mg = kmz_doc.add_multi_geometry(par=placemark)
                # Highlight the starting point
                kmz_doc.add_line_string(coords=' '.join([arp_coords[0], boresight_coords[0]]),
                                        par=mg,
                                        altitudeMode='absolute',)
                for idx in range(len(arp_coords)-1):
                    coords = [
                        arp_coords[idx],
                        boresight_coords[idx],
                        arp_coords[idx+1],
                        arp_coords[idx],
                    ]
                    kmz_doc.add_polygon(' '.join(coords), par=mg, altitudeMode='absolute')
                    coords = [
                        boresight_coords[idx],
                        boresight_coords[idx+1],
                        arp_coords[idx+1],
                        boresight_coords[idx],
                    ]
                    kmz_doc.add_polygon(' '.join(coords), par=mg, altitudeMode='absolute')

    kmz_file = os.path.join(output_directory, f"{file_stem}_cphd.kmz")
    with prepare_kmz_file(kmz_file, name=reader.file_name) as kmz_doc:
        root = kmz_doc.add_container(
            the_type="Folder", name=reader.cphd_meta.CollectionID.CoreName
        )
        add_global(kmz_doc, root)
        for chan in reader.cphd_meta.Data.Channels:
            add_channel(kmz_doc, root, channel_name=chan.Identifier)


def ecef_to_kml_coord(ecf_points):
    # TODO apply geoid.  KML expects MSL
    llh_points = ecf_to_geodetic(ecf_points)
    return [f"{lon},{lat},{alt}" for (lat, lon, alt) in llh_points]


def prepare_kmz_file(file_name, **args):
    """
    Prepare a kmz document and archive for exporting.

    Parameters
    ----------
    file_name : str
    args
        Passed through to the Document constructor.

    Returns
    -------
    Document
    """

    document = Document(file_name=file_name, **args)
    kpc._create_sicd_styles(document)
    _create_cphd_styles(document)
    return document


def _xy_to_kml_coord(reader, xy):
    """Convert a ReferenceSurface XY location to a kml coordinate"""
    xy = np.atleast_2d(xy)
    if reader.cphd_meta.SceneCoordinates.ReferenceSurface.Planar is not None:
        iarp_ecf = reader.cphd_meta.SceneCoordinates.IARP.ECF.get_array()
        uiax = (
            reader.cphd_meta.SceneCoordinates.ReferenceSurface.Planar.uIAX.get_array()
        )
        uiay = (
            reader.cphd_meta.SceneCoordinates.ReferenceSurface.Planar.uIAY.get_array()
        )
        xy_ecf = iarp_ecf + xy[:, 0, np.newaxis] * uiax + xy[:, 1, np.newaxis] * uiay
    else:
        raise NotImplementedError
    return ecef_to_kml_coord(xy_ecf)


def _antenna_aiming(reader, channel_index, signal_pvp):
    cphd_meta = reader.cphd_meta
    results = {}

    if cphd_meta.Antenna is None:
        return results

    apcs = {}
    for apc in cphd_meta.Antenna.AntPhaseCenter:
        apcs[apc.Identifier] = apc

    acfs = {}
    for acf in cphd_meta.Antenna.AntCoordFrame:
        acfs[acf.Identifier] = acf

    patterns = {}
    for antpat in cphd_meta.Antenna.AntPattern:
        patterns[antpat.Identifier] = antpat

    def _compute_pointing(channel_index, apc_id, antpat_id, txrcv):
        times = reader.read_pvp_variable(f"{txrcv}Time", channel_index)
        uacx = reader.read_pvp_variable(f"{txrcv}ACX", channel_index)
        uacy = reader.read_pvp_variable(f"{txrcv}ACY", channel_index)
        if uacx is None or uacy is None:
            acf_id = apcs[apc_id].ACFId
            uacx = acfs[acf_id].XAxisPoly(times)
            uacy = acfs[acf_id].YAxisPoly(times)
        uacz = np.cross(uacx, uacy)

        pointing = {}
        pointing['raw'] = {
            'times': times,
            'uacx': uacx,
            'uacy': uacy,
            'uacz': uacz,
        }
        pointing["mechanical"] = uacz

        ebpvp = reader.read_pvp_variable(f"{txrcv}EB", channel_index)
        if ebpvp is not None:
            eb_dcx = ebpvp[:, 0]
            eb_dcy = ebpvp[:, 1]
        else:
            eb_dcx = patterns[antpat_id].EB.DCXPoly(times)
            eb_dcy = patterns[antpat_id].EB.DCYPoly(times)

        pointing['raw']['eb_dcx'] = eb_dcx
        pointing['raw']['eb_dcy'] = eb_dcy

        pointing["electrical"] = _acf_to_ecef(eb_dcx, eb_dcy, uacx, uacy)

        return pointing

    def _beam_footprint(antpat_id, apc_pos, time, uacx, uacy, eb_dcx, eb_dcy):
        """Compute a beam contour on the earth"""
        array_gain_poly = patterns[antpat_id].Array.GainPoly
        element_gain_poly = patterns[antpat_id].Element.GainPoly

        approx_gain_coefs = np.zeros((3, 3))
        approx_gain_coefs += np.pad(array_gain_poly.Coefs, [(0, 3), (0, 3)])[:3, :3]
        approx_gain_coefs += np.pad(element_gain_poly.Coefs, [(0, 3), (0, 3)])[:3, :3]

        Ns = 201
        db_down = 10  # dB down from peak
        deltaDC_Xmax = np.abs((-approx_gain_coefs[1, 0] +
                               np.sqrt(approx_gain_coefs[1, 0]**2-4*approx_gain_coefs[2, 0]*db_down)) /
                              (2*approx_gain_coefs[2, 0]))
        deltaDC_Ymax = np.abs((-approx_gain_coefs[0, 1] +
                               np.sqrt(approx_gain_coefs[0, 1]**2-4*approx_gain_coefs[0, 2]*db_down)) /
                              (2*approx_gain_coefs[0, 2]))
        X = np.linspace(-deltaDC_Xmax, deltaDC_Xmax, Ns)
        Y = np.linspace(-deltaDC_Ymax, deltaDC_Ymax, Ns)
        XXc, YYc = np.meshgrid(X, Y, indexing='ij')

        array_gain_pattern = array_gain_poly(XXc, YYc)
        element_gain_pattern = element_gain_poly(XXc + eb_dcx, YYc + eb_dcy)
        gain_pattern = array_gain_pattern + element_gain_pattern

        contour_levels = [-3]  # dB
        contour_sets = plt.contour(XXc, YYc, gain_pattern, levels=contour_levels)
        plt.close()  # close the figure created by contour
        contour_vertices = contour_sets.collections[0].get_paths()[0].vertices
        delta_dcx = contour_vertices[:, 0]
        delta_dcy = contour_vertices[:, 1]

        contour_pointing = _acf_to_ecef(delta_dcx + eb_dcx,
                                        delta_dcy + eb_dcy,
                                        uacx,
                                        uacy,)

        contour_earth_ecf = []
        for along in contour_pointing:
            contour_earth_ecf.append(ray_intersect_earth(apc_pos, along))
        return {
            'time': time,
            'contour': contour_earth_ecf
        }

    chan_params = cphd_meta.Channel.Parameters[channel_index]
    if not chan_params.Antenna:
        return {}

    result = {}
    tx_apc_id = chan_params.Antenna.TxAPCId
    result["Tx"] = {
        "APCId": tx_apc_id,
        "apc_position": reader.read_pvp_variable("TxPos", channel_index),
        "pointing": _compute_pointing(
            channel_index, tx_apc_id, chan_params.Antenna.TxAPATId, "Tx"
        ),
    }

    rcv_apc_id = chan_params.Antenna.RcvAPCId
    result["Rcv"] = {
        "APCId": rcv_apc_id,
        "apc_position": reader.read_pvp_variable("RcvPos", channel_index),
        "pointing": _compute_pointing(
            channel_index, rcv_apc_id, chan_params.Antenna.RcvAPATId, "Rcv"
        ),
    }

    indices = np.where(signal_pvp == 1)[0]
    result['Tx']['beam_footprint'] = {}
    result['Rcv']['beam_footprint'] = {}
    for name, pvp_index in [('start', indices[0]),
                            ('middle', indices[len(indices)//2]),
                            ('end', indices[-1])]:
        try:
            result['Tx']['beam_footprint'][name] = _beam_footprint(antpat_id=chan_params.Antenna.TxAPATId,
                            apc_pos=reader.read_pvp_variable("TxPos", channel_index)[pvp_index],
                            time=reader.read_pvp_variable("TxTime", channel_index)[pvp_index],
                            uacx=result['Tx']['pointing']['raw']['uacx'][pvp_index],
                            uacy=result['Tx']['pointing']['raw']['uacy'][pvp_index],
                            eb_dcx=result['Tx']['pointing']['raw']['eb_dcx'][pvp_index],
                            eb_dcy=result['Tx']['pointing']['raw']['eb_dcy'][pvp_index],
            )
        except Exception as exc:
            logger.warning(f"Exception while calculating Tx beam footprint of {chan_params.Antenna.TxAPATId}")
            logger.warning(exc)

        try:
            result['Rcv']['beam_footprint'][name] = _beam_footprint(antpat_id=chan_params.Antenna.RcvAPATId,
                            apc_pos=reader.read_pvp_variable("RcvPos", channel_index)[pvp_index],
                            time=reader.read_pvp_variable("RcvTime", channel_index)[pvp_index],
                            uacx=result['Rcv']['pointing']['raw']['uacx'][pvp_index],
                            uacy=result['Rcv']['pointing']['raw']['uacy'][pvp_index],
                            eb_dcx=result['Rcv']['pointing']['raw']['eb_dcx'][pvp_index],
                            eb_dcy=result['Rcv']['pointing']['raw']['eb_dcy'][pvp_index],
            )
        except Exception as exc:
            logger.warning(f"Exception while calculating Rcv beam footprint of {chan_params.Antenna.RcvAPATId}")
            logger.warning(str(exc))

    return result


def _acf_to_ecef(eb_dcx, eb_dcy, uacx, uacy):
    uacz = np.cross(uacx, uacy)
    eb_dcz = np.sqrt(1 - eb_dcx**2 - eb_dcy**2)
    eb = np.stack((eb_dcx, eb_dcy, eb_dcz)).T

    eb_pointing = eb[:, 0, np.newaxis] * uacx
    eb_pointing += eb[:, 1, np.newaxis] * uacy
    eb_pointing += eb[:, 2, np.newaxis] * uacz

    return eb_pointing
