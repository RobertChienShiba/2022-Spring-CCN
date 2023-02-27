import socket
import time

HOST = '127.0.0.1'
PORT = 8000
server_addr = (HOST, PORT)

send_base = 0
next_seq_num = 0

cwnd_size = 3
num_pkt = 10

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5)
while True:
    while next_seq_num < send_base + cwnd_size and next_seq_num < num_pkt:
        client.sendto(str(next_seq_num).encode(), server_addr)
        next_seq_num += 1
    try:
        ack,address = client.recvfrom(1024)
        if len(ack)>0:
            print("ack {} is arrive".format(int(ack)))
            send_base  = int(ack)+1
            if int(ack) == num_pkt-1:
                break        
    except socket.timeout as e:
        print("pkt {} is timeout !!".format(send_base))
        next_seq_num = send_base
        
