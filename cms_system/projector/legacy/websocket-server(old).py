import asyncio
import websockets
import socket

def GetcurrentIP():
    val = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    val.connect(("8.8.8.8", 80))
    print("현재 IP 주소 : ", val.getsockname()[0])

    return val.getsockname()[0]

# HOST IP ADDRESS
#HOST = "203.250.33.53"
HOST = GetcurrentIP()
PORT = 9998

# 클라이언트 접속이 되면 호출된다.
async def Comm_Sign2Media(websocket, path):
    print("통신 시작...\n")
    while True:
        print("루프 시작 및 통신 진행 중...\n")
        file_path = await websocket.recv()  # 클라이언트로부터 메시지 대기
        print("선택 미디어 파일 경로 : " + file_path)

        await websocket.send("Acknowleged : " + file_path)  # 클라인언트로 재전송
        print("루프 끝..\n")

print("------------서버 실행...-------------\n")
print("------------사이니지 웹 클라이언트 - 미디이 서버 연결...-------------\n")
# 웹 소켓 서버 생성.호스트: localhost, port: 9998

start_server = websockets.serve(Comm_Sign2Media, HOST, PORT)

print("--------비동기 상태로 서버 대기...--------\n")
# 비동기 상태로 서버 대기
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
