import subprocess

def convert(input, output):

    sb = subprocess.call(
        'ffmpeg -loop 1 -i ./img/%s -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=1920:1080 ./img/%s' % (input, output), shell=True)
    print("val : ",sb)

convert("v2.jpg", "out12345.mp4")