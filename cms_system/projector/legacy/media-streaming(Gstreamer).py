import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib # 붉은줄이지만 import하는것으로 보임

# loop = GLib.MainLoop()
# Gst.init(None)

class TestRtspMediaFactory(GstRtspServer.RTSMediaFactory):
    def __init__(self):
        GstRtspServer.RTSPMediaFactory.__init__(self)


    def do_create_element(self, url):

        #set mp4 file path to filesrc's location property

        # src_demux = "filesrc location=1.mp4 ! qtdemux name=demux"

        # src_demux = "filesrc location={0} ! qtdemux name=demux".format(url)

        # src_demux = "filesrc location={file_path} ! qtdemux name=demux"

        src_demux = "filesrc location={0} ! qtdemux name=demux".format(file_path)

        h264_transcode = "demux.video_0"
        #uncomment following line if video transcoding is necessary
        #h264_transcode = "demux.video_0 ! decodebin ! queue ! x264enc"
        pipeline = "{0} {1} ! queue ! rtph264pay name=pay0 config-interval=1 pt=96".format(src_demux, h264_transcode)
        print("Element created: " + pipeline)
        return Gst.parse_launch(pipeline)

class GstreamerRtspServer():
    def __init__(self):
        self.rtspServer = GstRtspServer.RTSPServer()
        factory = TestRtspMediaFactory()
        factory.set_shared(True)
        mountPoints = self.rtspServer.get_mount_points()
        mountPoints.add_factory("/media-streaming", factory)
        self.rtspServer.attach(None)

if __name__ == '__main__':


    print('Enter name:')
    dir = input()
    print('filename, ' + dir)
    file_path = dir

    loop = GLib.MainLoop()
    Gst.init(None)

    s = GstreamerRtspServer()
    loop.run()

    # 이미지는 확장타입이 맞지않아 출력이 안되는 것으로 보임 opencv로 영상 만든다음 출력하는 방향으로
    # 업로드 시 그냥 60초 짜리 영상을 만들어버려?
