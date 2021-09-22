import socket
import threading
from argparse import ArgumentParser 
from Player import *
from config import *
from Art import *

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
                print("-----------------------------------------\n      "
                      "       Welcome to Love letter     !\n"
                      " ----------------------------------------\n"
                      "\tShow menu          (type m)\n"
                      "\tHistory and Rules  (type rul)\n"
                      "\tCard action        (type card)\n"
                      "\tCreate room        (type 0)\n"
                      "\tJoin Room          (type room id)\n")
            else:
                if(message):
                    print(message)
        except Exception as e:                                            #case on wrong ip/port details
            print(e,"An error occured!")

def write():
    while True:                                                 
        message = "{}".format(input('\n'))

        if (message == 'rul'):
            rules()
        elif (message == 'card'):
            card()
        elif (message == 'm'):
            print("\tShow menu          (type m)\n"
                  "\tHistory and Rules  (type rul)\n"
                  "\tCard action        (type card)\n"
                  "\tCreate room        (type 0)\n"
                  "\tJoin Room          (type room id)\n")
        else:
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