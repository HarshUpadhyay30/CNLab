import cv2
import socket
import pickle

client_ip = "127.0.0.1"
client_port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((client_ip, client_port))

buffer = []

print("[CLIENT] Waiting for video stream...")

while True:
    try:
        packet, _ = sock.recvfrom(65536) 
        marker, chunk = pickle.loads(packet)  

        buffer.append(chunk)

        if marker == 1: 
            data = b"".join(buffer)
            frame_data = pickle.loads(data)
            frame = cv2.imdecode(frame_data, cv2.IMREAD_COLOR)

            cv2.imshow("UDP Video Stream", frame)

            buffer.clear()
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except KeyboardInterrupt:
        break

sock.close()
cv2.destroyAllWindows()
print("[CLIENT] Streaming finished")



