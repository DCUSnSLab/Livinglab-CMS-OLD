import subprocess, m3u8, time, cv2, os
from .files import FileTypeCheck

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_PATH = "{0}/media/icon/".format(BASE_DIR)

def GetThumbnail(path, save_dir):
    vodCap = cv2.VideoCapture(path)
    play_icon = cv2.imread(ICON_PATH+"playbutton.png")

    cnt = 0
    while(vodCap.isOpened()):

        if cnt == 0:
            ret, frame = vodCap.read()
            cv2.imwrite(save_dir+"thumbnail.jpg", frame)

            cnt +=1
        else:
            break
    vodCap.release()

def img2video(img, vod):

    sb = subprocess.call(
        'ffmpeg -loop 1 -i {0} -c:v libx264 -t 30 -pix_fmt yuv420p -vf scale=1920:1080 {1}'.format(img, vod),
        shell=True)
    if sb == 0:
        print("이미지 -> 비디오 변환 완료")
    else:
        print("이미지 -> 비디오 변환 실패")
    print(" img -> mp4 변환끝")
    return sb

def video2m3u8(vod ,ts, m3u8, vodConvert=0):

    if vodConvert == 0:
        # print(" mp4 -> ts 변환 시작")

        sb = subprocess.call(
            'ffmpeg -i {0} -hls_flags split_by_time -hls_time 1 -hls_list_size 0 -hls_playlist_type event \
             -hls_segment_filename {1} {2}'.format(vod, ts, m3u8), shell=True)

        if sb == 0:
            print("이미지 -> 비디오 변환 완료")
        else:
            print("이미지 -> 비디오 변환 실패")
    else:
        print("Error, Video not exist")

    # print(" mp4 -> ts 변환 끝")


class MediaHandler:

    FLAG = True  # True : Advertisement Loop, False : Media Selected

    def __init__(self, playlist, ad_list):
        self.playlist = playlist
        self.ad_list = ad_list

    # clear playlist data
    def initiate(self):

        readFIle = open(self.playlist)
        lines = readFIle.readlines()
        readFIle.close()

        writeFile = open(self.playlist, 'w')
        writeFile.writelines([item for item in lines[0:7]])
        writeFile.close()
        print("이전 플레이리스트 삭제")

    def GetAdTSfile(self, Ad_list):

        AD_TS_LIST = []  # 전체 광고 ts 파일 저장

        for idx, file in enumerate(Ad_list):

            TS_LIST = {'path': None, 'ts_list': []}  # 광고 1개에 대해서 ts 파일 저장

            TS_LIST['path'] = file

            file_str = str(file)

            adPath = file_str.split("/")

            playlist = m3u8.load(file)
            for idx, seg in enumerate(playlist.segments):
                ts_set = []
                segString = str(seg)
                extinf, ts = segString.split('\n')

                # 개별 ts 파일은 현재 위치하는 파일 경로를 추가해주어야함(상대경로)
                relpath = "../AD/" + adPath[2] + "/"
                ts = relpath + ts
                ts_set.append(extinf)
                ts_set.append(ts)

                TS_LIST['ts_list'].append(ts_set)

            AD_TS_LIST.append(TS_LIST)

        return AD_TS_LIST

    def GetContentTSfile(self, content):
        CON_TS_LIST = []  # 콘텐츠 ts 파일 저장

        CON_LIST = {'path': None, 'ts_list':[]} # 미디어 1개에 대해서 ts파일저장

        CON_LIST['path'] = content

        con_str = str(content)

        conPath = con_str.split("/")

        playlist = m3u8.load(content)
        for idx, seg in enumerate(playlist.segments):
            ts_set = []
            segString = str(seg)

            extinf, ts = segString.split('\n')

            # 개별 ts 파일은 현재 위치하는 파일 경로를 추가해주어야함(상대경로)
            relpath = "../contents/{0}/{1}/{2}/".format(conPath[2], conPath[3], conPath[4])
            ts = relpath + ts
            ts_set.append(extinf)
            ts_set.append(ts)

            CON_LIST['ts_list'].append(ts_set)

        CON_TS_LIST.append(CON_LIST)

        return CON_TS_LIST

    def GetContentM3U8(self, path):

        path_str = str(path)
        content_path = path_str.split('/')
        name, _ = FileTypeCheck(content_path[3])

        m3u8path = "media/{0}/{1}/{2}/vod-{3}/{4}.m3u8".format(content_path[0],
                                                               content_path[1],
                                                               content_path[2],
                                                               name, name)
        return m3u8path

    def GetTStime(self, ts):

        if ts.isdigit():
            i = int(ts)
            return i
        else:
            f = float(ts)
            return f


    def WriteM3U8(self, que):

        while True:
            if self.FLAG == True:

                source = self.GetAdTSfile(self.ad_list)
                # source_json = json.dumps(source, indent=4)
                # print(source_json)

                for item1 in source:
                    if self.FLAG == False:
                        break
                    else:
                        pass

                    with open(self.playlist, "a", encoding='utf-8') as file:
                        file.write("#EXT-X-DISCONTINUITY\n")
                        file.close()

                    for idx, item2 in enumerate(item1['ts_list']):
                        with open(self.playlist, "a", encoding='utf-8') as file:
                            file.write(item2[0] + "\n")
                            file.write(item2[1] + "\n")

                            file.close()

                            if not que.empty():
                                self.FLAG = False
                                break

                            # print("{0}-{1} media ts file added".format(item1['path'], idx))
                            sleeptime = self.GetTStime(item2[0][8:-1])
                            time.sleep(sleeptime)


            elif self.FLAG == False:
                path = que.get()
                #print("선택 미디어", path)

                content_path = self.GetContentM3U8(path)
                source = self.GetContentTSfile(content_path)

                # source_json = json.dumps(source, indent=4)
                # print(source_json)

                for item1 in source:
                    with open(self.playlist, "a", encoding='utf-8') as file:
                        file.write("#EXT-X-DISCONTINUITY\n")
                        file.close()

                    ts_num = len(item1['ts_list'])
                    ts_num_check = 0

                    for idx, item2 in enumerate(item1['ts_list']):

                        with open(self.playlist, "a", encoding='utf-8') as file:
                            file.write(item2[0] + "\n")
                            file.write(item2[1] + "\n")
                            file.close()

                            ts_num_check += 1
                            # print("{0}-{1} media ts file added".format(path, idx))

                            sleeptime = self.GetTStime(item2[0][8:-1])
                            time.sleep(sleeptime)

                            if que.empty():
                                pass
                                # print("que not inserted")

                            else:
                                # print("que inserted")
                                break

                    if ts_num_check == ts_num:
                        self.FLAG = True
