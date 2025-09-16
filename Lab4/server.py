import cv2
import socket
import pickle
import math
import time
import subprocess

server_ip = "127.0.0.1"
server_port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

url = "https://www.youtube.com/watch?v=8cfwD8ybFfw"
result = subprocess.run(
    ["yt-dlp", "-f", "best[ext=mp4]", "-g", url],
    capture_output=True,
    text=True
)
direct_url = result.stdout.strip()
cap = cv2.VideoCapture(direct_url)

if not cap.isOpened():
    raise FileNotFoundError(f"Error: Could not open {video_path}")

CHUNK_SIZE = 60000  
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("[SERVER] End of video reached.")
        break
    
    _, buffer = cv2.imencode(".jpg", frame)
    data = pickle.dumps(buffer)


    total_chunks = math.ceil(len(data) / CHUNK_SIZE)

    for i in range(total_chunks):
        start = i * CHUNK_SIZE
        end = start + CHUNK_SIZE
        chunk = data[start:end]

        marker = 1 if i == total_chunks - 1 else 0
        sock.sendto(pickle.dumps((marker, chunk)), (server_ip, server_port))

    frame_count += 1
    print(f"[SERVER] Video frame {frame_count} uploaded")

    time.sleep(0.05) 

cap.release()
sock.close()
print("[SERVER] Streaming finished")





