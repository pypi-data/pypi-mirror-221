# 📻 Rec-Spotify

The program allows you to record Spotify tracks, albums, and playlists with a single simple command. It is also able to fully synchronize your Spotify playlists to a local folder and keep them up-to-date.

For now it works **only** on Windows.

## Requirements

- Python3
- Spotify Premium (no ad blocking functionality)
- [Virtual Audio Cable](https://vb-audio.com/Cable) (recommended, read below)

## Install

```sh
pip install rec-spotify
```

## Configration

On the first run, the program will launch a setup wizard. This will prompt you to enter your Spotify app credentials and other required information.

The config file is located at: ```C:\Users\<username>\.rec_spotify\config.ini```

Config example:

```ini
[SPOTIFY]
CLIENT_ID = <SPOTIFY_CLIENT_ID>
CLIENT_SECRET = <SPOTIFY_CLIENT_SECRET>
REDIRECT_URL = <REDIRECT_URL>

[SETTINGS]
MUSIC_DIR = D:\Music
AUDIO_FORMAT = mp3
AUDIO_QUALITY = 320
SAMPLE_RATE = 48000
```

## Usage

```sh
# Perform a full synchronization.
rec-spotify

# Record single track/album/playlist.
# Spotify URL format example: https://open.spotify.com/track/42vwak6ZIFMscDhzz3S52f
# Output path format example: C:\Users\<username>\Desktop or just "." to save in current directory
rec-spotify --url <url> --path <where_to_save>
```

## FAQ

### 1. What is the purpose of this program?

The answer is simple: I want to have local copies of all my Spotify tracks and playlists in original quality. Because who knows maybe one day i will lose access to my account or something else will happen.

### 2. Why do I need Virtual Audio Cable?

Virtual Audio Cable installation is optional but highly recommended for improved recording quality. It also allows listening to other audio while recording.


## TODO

- [ ] Linux support.
- [ ] Trim silence from beginning and end of track.
- [ ] Command-line interface for database management of tracks and playlists.
- [ ] Ad blocking.
