import argparse
import datetime

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from cartopy_basic_hud.colors import saturation_colormap
from cartopy_basic_hud.cli import str2bool
from cartopy_basic_hud.constants import CAPECOD_LAT_NORTH, CAPECOD_LAT_SOUTH, CAPECOD_LON_EAST, CAPECOD_LON_WEST
from cartopy_basic_hud.models import TelemetryPoint, TelemetryTrack


def show_hud(lat_min, lat_max, lon_min, lon_max, tracks=None, desaturate_old_points=True):
    extent = (lon_min, lon_max, lat_min, lat_max)  # (x0, x1, y0, y1)

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent(extent)
    ax.coastlines()

    # TODO - Consider taking the trouble to draw all the oldest points first, then the next oldest, etc.,
    #  so that the older points of the last track to be drawn aren't drawn over the newer points
    #  of the first track to be drawn. This seems like a more complicated task, because we can't
    #  simply do each track as its own scatter plot.
    if tracks:
        if desaturate_old_points:
            # plt.scatter() does not take an array of alpha values, so we'll need to construct a colormap
            # for each track where old timestamps are desaturated and new ones are fully saturated.

            # Get the list of colors, the cycle that is used by default for plotted lines.
            prop_cycle = plt.rcParams['axes.prop_cycle']
            colors = prop_cycle.by_key()['color']

            for i, track in enumerate(tracks):
                color_hex = colors[i % len(colors)]
                cmap = saturation_colormap(color_hex)

                plt.scatter(track.lons, track.lats, c=track.timestamps, cmap=cmap)
        else:
            for track in tracks:
                plt.scatter(track.lons, track.lats)

    plt.show()


def main():
    argparser = argparse.ArgumentParser("Use Cartopy to show a telemetry HUD.")
    argparser.add_argument("--lat-bounds", type=float, nargs=2, default=[CAPECOD_LAT_SOUTH, CAPECOD_LAT_NORTH])
    argparser.add_argument("--lon-bounds", type=float, nargs=2, default=[CAPECOD_LON_WEST, CAPECOD_LON_EAST])
    argparser.add_argument("--tracks", type=int, default=1, help="Number of fictional tracks to plot.")
    argparser.add_argument("--desaturate-old-points", type=str2bool, default=True, help="e.g. true, false, 1, 0.")

    # Parse CLI arguments.
    args = argparser.parse_args()
    lat_min = min(args.lat_bounds)
    lat_max = max(args.lat_bounds)
    lon_min = min(args.lon_bounds)
    lon_max = max(args.lon_bounds)

    # Make up random fictional track starting within the bounds.
    tracks = []
    while len(tracks) < args.tracks:
        # TODO - consider varying the start point between tracks.
        #  Given that this is just an example, I'm not worrying about it, but it might be preferable.
        start_point = TelemetryPoint(
            timestamp=datetime.datetime(2001, 1, 1, 11, 59, 59),
            lat=(lat_min + lat_max)/2,
            lon=(lon_min + lon_max)/2,
        )
        tracks.append(TelemetryTrack.make_wandering_track(start_point=start_point))

    print("args.desaturate_old_points = " + str(args.desaturate_old_points))

    show_hud(lat_min=lat_min, lat_max=lat_max, lon_min=lon_min, lon_max=lon_max,
             tracks=tracks,
             desaturate_old_points=args.desaturate_old_points)


if __name__ == "__main__":
    main()
