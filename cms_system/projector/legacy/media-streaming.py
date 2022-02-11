import ffmpeg_streaming

from ffmpeg_streaming import Formats, Bitrate, Representation, Size



# load media
video = ffmpeg_streaming.input('./vod/5.mp4')

# Generate representations manually
# Specify the value of kilo bite rate and size for each stream explicitly
# _360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
#_480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
_720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

# create HLSfiles
# It creates a playlist file, and one or more segment files automatically.
# The output filename specifies the playlist filename.

hls = video.hls(Formats.h264())
hls.representations(_720p)
# hls.representations(_360p, _480p, _720p)
hls.output('./hls/hls.m3u8')
