import ffmpeg

video_format = "flv"
server_url = "http://127.0.0.1:8080"

process = (
    ffmpeg
    .input("../hls/hls.m3u8")
    .output(
        server_url,
        codec = "copy", # use same codecs of the original video
        listen=1, # enables HTTP server
        f=video_format)
    .global_args("-re") # argument to act as a live stream
    .run()
)