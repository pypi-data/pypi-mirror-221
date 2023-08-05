CONFIG_VALID = "[[green bold]OK[/green bold]] Configuration: {filepath}"
CONFIG_NOT_FOUND = (
    ":grey_question: The configuration files are not found. Lets create them first!"
)
CONFIG_CREATED = ":white_check_mark: The configuration file located at {filepath} has been created. Please restart the program."

SELECT_SPOTIFY_DEVICE = ":mobile_phone: SELECT DEVICE: "
SELECT_AUDIO_DEVICE = ":speaker: AUDIO DEVICE: "

JOB_TYPE = "[[green bold]OK[/green bold]] Ready to record the [magenta bold]{job_type}[/magenta bold]: {name}"
LINK_ERR = "[[red bold]ERROR[/red bold]] The link provided does not match the required format. Please ensure the link follows the correct format, such as this example: https://open.spotify.com/playlist/4weVyheZdSUIdDpmJyx2zf"


NEW_PLAYLIST = "[[green bold]ADDED[/green bold]] :file_folder: Playlist: {playlist}"
RENAME_PLAYLIST = (
    "[[green bold]RENAME[/green bold]] :file_folder: Playlist: {from_name} -> {to_name}"
)
DEL_PLAYLIST = "[[red bold]DELETE[/red bold]] :x: Playlist: {playlist}"


TRACK = ":musical_note: {title}"
NEW_TRACK = "[[green bold]ADDED[/green bold]] :musical_note: Track: {track_title}"
DEL_TRACK = "[[red bold]DELETE[/red bold]] :x: Track: {track_title}"
TRACK_SAVED = ":white_check_mark: Recorded: {filepath}"

DATABASE_OK = "[[green bold]OK[/green bold]] Database initialization."
STATS = "[[magenta bold]STATS[/magenta bold]] :file_folder: Playlists: {playlists_count} | :musical_note: Total Tracks: {tracks_count} | :fire: Tracks not downloaded: {undownloaded_count}"

SYNC_START = "[[blue bold]INFO[/blue bold]] The recording process has started. It will take about ~ {total_time}"
SYNC_OK = "[[blue bold]INFO[/blue bold]] :white_check_mark: Everything is up to date."

PB_ERROR = "[[red bold]ERROR[/red bold]] Please toggle Spotify playback and try again. This is a common problem."
REQ_ERROR = "[[red bold]ERROR[/red bold]][[blue bold]RETRY[/blue bold]] Error: {error}."
