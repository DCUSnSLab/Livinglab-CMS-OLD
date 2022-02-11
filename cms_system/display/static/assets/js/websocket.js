// Websocket connection - start
// 웹 서버를 접속한다.
var webSocket = new WebSocket("ws://203.250.33.53:9998");
// 웹 서버와의 통신을 주고 받은 결과를 출력할 오브젝트를 가져옵니다.
var messageTextArea = document.getElementById("messageTextArea");
// 소켓 접속이 되면 호출되는 함수
webSocket.onopen = function(message){
    console.log("MediaServer connected.. with websocket..\n");

};
// 소켓 접속이 끝나면 호출되는 함수
webSocket.onclose = function(message){
    console.log("MediaServer Disconnect...\n");
};
// 소켓 통신 중에 에러가 발생되면 호출되는 함수
webSocket.onerror = function(message){
    console.log("error...\n");
};
// 소켓 서버로 부터 메시지가 오면 호출되는 함수.
webSocket.onmessage = function(message){
// 출력 area에 메시지를 표시한다.
    console.log("Recieve From MediaServer => "+message.data+"\n");
};

//서버 접속 끊
function disconnect(){
webSocket.close();
}