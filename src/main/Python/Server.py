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
        try:                           
            if(not player.room):    
                client.send('ROOM'.encode('ascii'))   
                room_id = client.recv(1024).decode('ascii') 
                room_id = int(room_id)
                room = None
                if(room_id==0):
                    room = Room(len(rooms)+1)
                    rooms.append(room)
                else:
                    for room_ in rooms:
                        if(room_._id==room_id):
                            room = room_
                room.join(player)
            elif(player.room and not player.room.isPlaying):
                players_ = player.room.play()
                for player_ in players_:            
                    players.remove(player_)
                    player_.client.close()
                    nickname = player.name
                break

            else:
                message = client.recv(1024)
                broadcast(message)
        except Exception as e:                                                     
            index = players.index(player)
            players.remove(player)
            client.close()
            nickname = player.name
            broadcast('{} left the server!'.format(nickname).encode('ascii'))
            break

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