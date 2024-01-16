from vidstream import *
import tkinter as tk
import socket
import threading
import requests

# get ip address
local_ip_address = socket.gethostbyname(socket.gethostname())
#public_ip_address = requests.get('http://api.ipify.org').text ## public ip

#print(local_ip_address)


server = StreamingServer(local_ip_address, 8888)
receiver = AudioReceiver(local_ip_address, 9999)

# function for connection
def start_listening():
    t1 = threading.Thread(target=server.start_server())
    t2 = threading.Thread(target=receiver.start_server())
    t1.start()
    t2.start()

# function to start camera
def start_camera():
    camera_client = CameraClient(text_ip_target.get(1.0, 'end-1c'), 6666)
    t3 = threading.Thread(CameraClient.start_stream)
    t3.start()

# function to start screen sharing
def start_screensharing():
    screensharing_client = ScreenShareClient(text_ip_target.get(1.0, 'end-1c'), 6666)
    t4 = threading.Thread(target=screensharing_client.start_stream)
    t4.start()

# function to start audio stram
def start_audio():
    audio_client = AudioSender(text_ip_target.get(1.0, 'end-1c'), 7777)
    t5 = threading.Thread(target=audio_client.start_stream)
    t5.start()

# gui
window = tk.Tk()
window.title("call / screansharing")
window.geometry('300x300')

label_ip_target = tk.Label(window, text="Target IP")
label_ip_target.pack()

text_ip_target = tk.Text(window, height=1)
text_ip_target.pack()

btn_listening = tk.Button(window, text="Start listening", width=40, command=start_listening)
btn_listening.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start camera", width=40, command=start_camera)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start screensharing", width=40, command=start_screensharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start audio", width=40, command=start_audio)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()