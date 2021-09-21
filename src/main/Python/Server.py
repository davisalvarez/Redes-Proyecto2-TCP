import socket
import select
import sys
import threading
from config import *
from Player import *
from Room import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                               #binding host and port to socket
server.listen()

players = []
rooms = []

def broadcast(message):                                                 
    for player in players:
        player.client.send(message)

def handle(player):
    client = player.client                                         
    while True:
#        try:                           
        if(not player.room):    
            client.send('ROOM'.encode('ascii'))   
            room_id = client.recv(1024).decode('ascii') 
            room_id = int(room_id)
            room = None
            room_exists = False                         #Make sure that the room exists
            if(room_id==0):
                room = Room(len(rooms)+1)
                rooms.append(room)
                room_exists = True
            else:
                for room_ in rooms:
                    if(room_._id==room_id):
                        room = room_
                        room_exists = True
            if room_exists:                             #Make sure that the room exists
                room.join(player)
            else:                                       #Else, tell the user
                # message = b'Provided room does not exists'
                # broadcast(message)
                client.send('Provided room does not exists'.encode('ascii'))
        elif(player.room and not player.room.isPlaying):
            player.room.play()
        else:
            message = client.recv(1024)
            broadcast(message)
#        except Exception as e:
#            print(e)                                                        
#            index = players.index(player)
#            players.remove(player)
#            client.close()
#            nickname = player.name
#            broadcast('{} left the server!'.format(nickname).encode('ascii'))
#            break

def receive():                                                          
    while True:
        client, address = server.accept()     
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        player = Player(nickname, client)
        players.append(player)
        print("Connected with {} as {}".format(str(address), nickname))  
        broadcast("{} joined the server!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(player,))
        thread.start()

receive()