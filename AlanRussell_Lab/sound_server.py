import zmq
import subprocess
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

# rainbow_cycle(0.001)
# 解释器
def play_sound():
    # 有问题 与引脚（neepixel）一起用会冲突
    subprocess.call('/usr/bin/omxplayer -o local /home/pi/Downloads/Rip16.wav', shell=True)

while True:
    #  Wait for next request from client
    message = socket.recv() # byte?
    print(f"Received request: {message} ({type(message)})")
    #  Do some 'work'
    # time.sleep(1)
    if message == b"play":
        #  Send reply back to client
        socket.send(b"ok")
        play_sound()
        
    else:
        socket.send(b"do not understand")