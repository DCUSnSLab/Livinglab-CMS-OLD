import vlc
import time
from moviepy.editor import VideoFileClip
import subprocess
import time

def VLC_Player():
    time.sleep(2)  # HLS_streaming 켜질때까지 기다림
    # BASE_DIR = "dev_src/Livinglab/Livinglab-CMS/projector/hls"
    LOCALHOST = "127.0.0.1"
    BASE_DIR = "hls/"
    Filename = "hls.m3u8"
    PORT = "7000/"
    HLS_URL = "http://" + LOCALHOST + ":" + PORT + BASE_DIR + Filename

    print("1", LOCALHOST)
    print("1", PORT)
    print("2", BASE_DIR)
    print("3", Filename)
    print("4", HLS_URL)

    clip = VideoFileClip(HLS_URL)
    print("d", clip.duration)

    player = vlc.MediaPlayer(HLS_URL)
    player.toggle_fullscreen()
    player.play()
    time.sleep(clip.duration)  # 영상 길이에 맞게 time.sleep해줘야함

if __name__ == "__main__":
    VLC_Player()