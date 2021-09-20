import socket
import threading
from argparse import ArgumentParser 
from Player import *
from config import *

nickname = None

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect((host, port))                             

def receive():
    while True:                                                 
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            elif message == 'ROOM':
            	done = False
            	while (not done):
            		print("----------------------------------\n      Welcome to Love letter     \n ----------------------------------\n\t1. Join Room\t2.Create room\n")
            		user = input("Choose:\t")
            		if(user=="1"):
            			room_id = input("Type the room ID")
            			done = True
            			client.send((str(room_id)).encode('ascii'))
            		elif(user=="2"):
                		client.send((str(-1)).encode('ascii'))					#If answer is negative then it tells server to create room
                		done = True
            else:
                print(message)
        except Exception as e:                                            #case on wrong ip/port details
            print(e,"An error occured!")
            client.close()
            break

def write():
    while True:                                                 
        message = "{}: {}".format(nickname, input(''))
        client.send(message.encode('ascii'))

if __name__ == '__main__':

    parser = ArgumentParser(description=Player.__doc__)
    parser.add_argument("-n", "--name", dest="name",
                        help="Name on server")
    args = parser.parse_args()

    if args.name is None:
        args.name = input("Username: ")    

    nickname = args.name   
    receive_thread = threading.Thread(target=receive)               #receiving multiple messages
    receive_thread.start()
    write_thread = threading.Thread(target=write)                   #sending messages 
    write_thread.start()