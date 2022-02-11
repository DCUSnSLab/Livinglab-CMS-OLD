import asyncio
import websockets
from network import GetcurrentIP
import multiprocessing as mp
import subprocess
from contents.mediaProcessing import MediaHandler

# 웹 소켓 경우 추가 파라미터를 받을 수가 없음
# 파라미터 추가하는 방법을 찾기전까진 queue 글로벌 변수로 선언해서 임시방편으로 사용
q = mp.Queue()
# q = mp.SimpleQueue()

async def Comm_Sign2Media(websocket, path):
    print("process 1번")
    print("통신 시작...\n")
    async for message in websocket:
        print("루프 시작 및 통신 진행 중...\n")
        print("선택 미디어 파일 경로 : ", message)
        await websocket.send("Acknowleged2 :" + message)
        # 웹소켓으로 받은 콘텐츠 경로를 큐에 삽입

        q.put(message)
        print("루프 끝..\n")

async def Async2Signage():
    # HOST IP ADDRESS
    # HOST = "203.250.33.53"
    HOST = GetcurrentIP()
    PORT = 9998

    print("--------비동기 상태로 서버 대기...--------\n")
    # 비동기 상태로 서버 대기
    async with websockets.serve(Comm_Sign2Media, HOST, PORT):
        await asyncio.Future()  # run forever

def Websocket(q):
    print("--------서버 실행--------\n")
    asyncio.run(Async2Signage())  # 비동기적으로 실행하고 있다는 것이군

def Reciever(q):

    playlist = 'media/init/init.m3u8'
    ad1 = 'media/AD/ad1/ad1.m3u8'
    ad2 = 'media/AD/ad2/ad2.m3u8'
    Ad_list = [ad1, ad2]

    # # 초기화
    MS = MediaHandler(playlist, Ad_list)
    MS.initiate()
    MS.WriteM3U8(q)

def Hls_Streaming(q):
    # 웹서버 실행
    print("웹 서버 실행..")
    subprocess.call(["python", "-m", "http.server", "7000"])

if __name__ == "__main__":

    p0 = mp.Process(target=Hls_Streaming, args=(q,)) # HLS 스트리밍 서버, 클라이언트 요청수집
    p1 = mp.Process(target=Websocket, args=(q,)) # 웹 소켓 서버, 클라이언트 요청수집
    p2 = mp.Process(target=Reciever, args=(q,))  # 클라이언트 요청에 따른 m3u8플레이리스트 수정


    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()






