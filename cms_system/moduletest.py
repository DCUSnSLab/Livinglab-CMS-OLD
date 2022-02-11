import m3u8, json, time

class MediaHandler:

    # 파읽 읽기 모드
    # r - 읽기모드 (디폴트)
    # w - 쓰기모드, 파일이 있으면 모든 내용을 삭제
    # x - 쓰기모드, 파일이 있으면 오류 발생
    # a - 쓰기모드, 파일이 있으면 뒤에 내용을 추가
    # + - 읽기쓰기모드
    # t - 텍스트 모드, 텍스트 문자 기록에 사용 (디폴트)
    # b - 바이너리 모드, 바이트단위 데이터 기록에 사용

    def __init__(self):
        pass

    # clear playlist data
    def initiate(self, path):
        pass

# 미디어서버 http://127.0.0.1:7000/ 루트
# media/init/init.m3u8 메인 플레이리스트
# media/AD/ad1/ts 파일 광고 영상 -> init.m3u8에서 접근하기 위해 경로 변경필요
# ../AD/ad1/ ts파일
# ../AD/ad2/ ts파일
    def GetAdvertisement(self, Ad_list):

        AD_TS_LIST = []  # 전체 광고 ts 파일 저장

        for idx, file in enumerate(Ad_list):

            TS_LIST = {'path': None, 'ts_list': []} # 광고 1개에 대해서 ts 파일 저장

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
                ts = relpath+ts
                ts_set.append(extinf)
                ts_set.append(ts)

                TS_LIST['ts_list'].append(ts_set)

            AD_TS_LIST.append(TS_LIST)

        return AD_TS_LIST

    def ReadM3U8(self, path):

        f = open(path, 'rt', encoding='utf-8')
        line = f.read()
        print(line)
        f.close()

    def WriteM3U8(self, target, source):

        # source_json = json.dumps(source, indent=4)
        #
        # print(source_json)



        while True:

            for item1 in source:

                with open(target, "a", encoding='utf-8') as file:
                    file.write("#EXT-X-DISCONTINUITY\n")
                    file.close()

                for item2 in item1['ts_list']:

                    with open(target, "a", encoding='utf-8') as file:

                        file.write(item2[0] + "\n")
                        file.write(item2[1] + "\n")
                        file.close()
                        time.sleep(4.00)
                        print("done")

def testfunction(a):

    if a % 2 == 0:
        for a in range(0, 5):
            print("짝수")
            time.sleep(0.5)

    elif a % 2 == 1:
        for a in range(0, 5):
            print("홀수")
            time.sleep(0.5)

if __name__ == "__main__":

    while True:
        a = int(input())
        testfunction(a)

    # ad1 = 'media/AD/ad1/ad1.m3u8'
    # ad2 = 'media/AD/ad2/ad2.m3u8'
    # Ad_list = [ad1, ad2]
    # # Ad_list = [ad2]
    #
    # # 초기화
    # MS = MediaHandler()
    # AD_TS_LIST = MS.GetAdvertisement(Ad_list) # 사전 등록된 광고에서 ts 파일 추출
    # # 시작하기 전 init.m3u8 초기화 필요
    # # #EXT-X-DISCONTINUITY 태그를 찾아 #EXT-X-DISCONTINUITY를 포함한 아래 모든 플레이리스트를 삭제
    # MS.WriteM3U8('media/init/init.m3u8', AD_TS_LIST)
