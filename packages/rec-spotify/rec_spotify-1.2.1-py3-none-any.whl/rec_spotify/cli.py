import argparse
import sys

import rec_spotify.messages as m
from rec_spotify.items import Collection, Track
from rec_spotify.manager import Manager
from rec_spotify.config import Config
from rec_spotify.console import console, get_logo
from rec_spotify.utils import parse_spotify_url


def app() -> None:
    """CLI entrypoint."""

    console.print(get_logo())

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=False,
        help="Spotify link or ID for a separate track, playlist, or album.",
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        required=False,
        help="The output directory for saving recorded files",
    )

    args = parser.parse_args()
    manager = Manager()
    if args.url and args.path:
        match = parse_spotify_url(args.url)
        if match is not None:
            link_type, id = match
            manager.init()
            Config.MUSIC_DIR = args.path
            if link_type == "track":
                track = Track(id)
                manager.record_track(track)
            else:
                collection = Collection(id, kind=link_type)
                manager.record_collection(collection)

        else:
            console.print(m.LINK_ERR)
            sys.exit(1)

    elif len(sys.argv) == 1:
        manager.init()
        manager.sync()

    manager.close()
    sys.exit(0)


if __name__ == "__main__":
    app()
