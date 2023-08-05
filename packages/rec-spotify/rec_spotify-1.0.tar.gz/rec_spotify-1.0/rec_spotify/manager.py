import os
import sys
import typing as t

from rec_spotify.database import Database
import rec_spotify.messages as m
from rec_spotify.console import console
from rec_spotify.spotify import SpotifyClient
from rec_spotify.items import Track, Collection
from rec_spotify.config import Config
from rec_spotify.utils import download_cover, get_estimate_time
from rec_spotify.recorder import Recorder
from rec_spotify.lyrics import Lyrics


class Manager(object):
    @classmethod
    def sync(cls) -> None:
        "Synchronize Spotify content with local database"
        Database.init_db()

        # Print db stats
        playlists = Database.get_playlists()
        tracks = Database.get_tracks(total=True)
        undownloaded = list(filter(lambda x: not x.downloaded, tracks))
        console.print(
            m.STATS.format(
                playlists_count=len(playlists),
                tracks_count=len(tracks),
                undownloaded_count=len(undownloaded),
            )
        )

        # Sync Playlists
        process_play_ids = []
        sp_playlists = SpotifyClient.get_user_playlists()
        for sp_playlist in sp_playlists:
            loc_playlist = Database.get_playlist(sp_playlist.id)
            if loc_playlist is None:
                sp_playlist.create_dir()
                Database.add_playlist(sp_playlist)
                console.print(m.NEW_PLAYLIST.format(playlist=sp_playlist.name))

            elif sp_playlist.name != loc_playlist.name:
                old_name = loc_playlist.name
                loc_playlist.change_name(str(sp_playlist.name))
                Database.update_playlist(loc_playlist)
                console.print(
                    m.RENAME_PLAYLIST.format(
                        from_name=old_name,
                        to_name=sp_playlist.name,
                    )
                )
            process_play_ids.append(sp_playlist.id)

        deleted_playlists = Database.get_playlists_deleted(process_play_ids)
        for playlist in deleted_playlists:
            tracks_to_delete = Database.get_playlist_tracks(playlist)
            playlist.delete()
            Database.delete_playlist(playlist)
            console.print(m.DEL_PLAYLIST.format(playlist=playlist.name))
            for track in tracks_to_delete:
                track.delete()
                console.print(m.DEL_TRACK.format(track_title=track.title))

        # Sync Tracks
        tracks_to_download: t.Set[Track] = set()
        for sp_playlist in sp_playlists:
            processed_track_ids = []
            for sp_track in sp_playlist.get_tracks():
                loc_track = Database.get_track(sp_track.id)
                if loc_track is None:
                    sp_track.set_download_path()
                    Database.add_track(sp_track)
                    console.print(m.NEW_TRACK.format(track_title=sp_track.title))

                processed_track_ids.append(sp_track.id)

            to_delete = Database.get_deleted_tracks(processed_track_ids, sp_playlist)
            for track in to_delete:
                track.delete()
                Database.delete_track(track)
                console.print(m.DEL_TRACK.format(track_title=track.title))

        undownloaded = Database.get_tracks(downloaded=False)
        tracks_to_download = tracks_to_download.union(undownloaded)
        if len(undownloaded) == 0:
            console.print(m.SYNC_OK)
            sys.exit(0)

        # Recording
        total_time = get_estimate_time(
            sum(track.duration for track in tracks_to_download)
        )
        console.print(
            m.SYNC_START.format(
                total_time=total_time,
            )
        )
        console.print()
        console.rule(":radio: Recorder Log")
        for track in tracks_to_download:
            cls._record_and_save(track)
            Database.mark_downloaded(track, state=True)

    @classmethod
    def record_track(cls, track: Track) -> None:
        "Record and save single track."
        track = SpotifyClient.get_track(track)
        console.print(
            m.JOB_TYPE.format(
                job_type="track",
                name=track.title,
            )
        )
        cls._record_and_save(track)

    @classmethod
    def record_collection(cls, collection: Collection) -> None:
        "Record and save all tracks in a collection."
        collection = SpotifyClient.get_collection(collection)
        collection.create_dir()
        console.print(
            m.JOB_TYPE.format(
                job_type=collection.kind,
                name=collection.name,
            )
        )
        total_time = get_estimate_time(
            sum(track.duration for track in collection.get_tracks())
        )

        console.print(
            m.SYNC_START.format(
                total_time=total_time,
            )
        )
        console.print()
        console.rule(":radio: Recorder Log")
        for track in collection.get_tracks():
            cls._record_and_save(track)

    @classmethod
    def _record_and_save(cls, track: Track) -> None:
        "Helper method to record and save a single track."
        metadata = SpotifyClient.get_track_metadata(track)
        song_cover = download_cover(metadata["cover_url"])
        recorded_obj = Recorder.record(track)
        track.set_download_path()
        recorded_obj.export(
            out_f=track.filepath,
            format=Config.AUDIO_FORMAT,
            codec="libmp3lame",
            parameters=["-b:a", "320k", "-abr", "1"],
            tags=metadata,
            cover=song_cover.name,
        )

        lyrics = Lyrics.find(track)
        if lyrics is not None:
            Lyrics.embed_lyrics(track, lyrics)

        os.remove(song_cover.name)
        console.print(m.TRACK_SAVED.format(filepath=track.filepath))
        console.print()

    @classmethod
    def init(cls) -> None:
        "Initialize main dependencies."
        Config.init()
        SpotifyClient.init()
        Recorder.init()

    @classmethod
    def close(cls) -> None:
        "Cleanup - close database connections etc."
        Database.close()
        Recorder.close()
