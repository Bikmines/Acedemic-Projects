#server Program that handles multiple client
from socket import *
from threading import Thread
import serverDetails, minMax, managing, adding, delete

#Socket Creation
host = gethostname()
port = 6666
address = (host, port)
bufsize = 1024
server = socket(AF_INET, SOCK_STREAM)
server.bind(address)
server.listen(5)

class ClientHandler(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.__client = client

    def run(self):
        welcomeMsg = "Welcome to the Server\n"
        self.__client.send(welcomeMsg.encode("utf-8")) #message to client
        while True:
            try:
                userList = file_contains("users.txt") #obtaining list of users from users.txt
                userStatus, userName = serverAuthentication(self.__client, userList)
                try:
                    if userStatus == "Access Granted":
                        print ("Successfully authenticated")
                        print ("Waiting to choose an option...")
                        choice_Recv = self.__client.recv(bufsize)
                        choice = choice_Recv.decode('utf-8')
                        orgList = file_contains("organisations.txt")
                        status = "continue"
                        while status != "end":
                            if choice == '1':
                                status = serverDetails.server_Details(self.__client, orgList)
                            elif choice == '2':
                                status = minMax.statistics(self.__client, orgList)
                            elif choice == '3':
                                status = managing.sorting(self.__client,orgList)
                            elif choice == '4':
                                status = adding.add_Organisation(self.__client, orgList)
                            elif choice == '5':
                                status = delete.remove_Organisation(self.__client, orgList)
                            else:
                                status = "end"
                            if status == "continue":
                                choice_Recv = self.__client.recv(bufsize)
                                choice = choice_Recv.decode('utf-8')
                        if status == "end":
                            print ("Closing Connection...")
                            print("logging out User")
                            self.__client.close()#closing connections
                            print ('Connection Terminated')
                            break
                   #exceptional handling    
                except ConnectionResetError:
                    userStatus = "Access Denied"
                    usersList = []
                    usersOnline = open ("onlineUsers.txt", 'r')
                    userNames = usersOnline.read()
                    userNames = userNames.split()
                    for index in userNames:
                        if index != userName:
                            usersList.append(index)
                    usersOnline.close()
                    

                    usersConnected = open ("onlineUsers.txt", 'w')
                    usersConnected.write(' '.join(usersList))
                    usersConnected.close()
                return userStatus 
            except ConnectionResetError: 
                print ('\nClosing Connection...')
                self.__client.close() 
                print ('\nconnection Terminated')
                break
            
# reading file from users.txt and organisations.txt
def file_contains(fileName):    
    inputFile = open(fileName, 'r')
    users = [] #create empty list

    for line in inputFile:
        line = line.rstrip() 
        users.append(line.split()) 
    inputFile.close()
    return users

#Authenticating Users
def serverAuthentication(client, userList):
    flag = "Access Denied"
    for index in [1, 2, 3]:
        
        userNameRecv = client.recv(bufsize) #receiving Username
        userName = userNameRecv.decode("utf-8")
        
        passwordRecv = client.recv(bufsize) #receiving Password
        password = passwordRecv.decode("utf-8")
        
        print ("\nServer received Username and Password")
        
        response = "Unsuccessful"
        for index in userList: # userList contains all usernames and password
            if index[0] == userName:
                if index[1] == password:
                    response = "Connection Successful"
                    break
                
        if response == "Connection Successful":
            #checking already logged in user in onlineUsers.txt
            usersOnline = open ("onlineUsers.txt", 'r')
            users = usersOnline.read()
            usersOnline.close()

            if userName in users:
                response = "User already in use"
                client.send(response.encode('utf-8'))
            else:
                #writing username in onlineUsers file
                usersOnline = open ("onlineUsers.txt", 'w')
                users = users + " " + userName
                usersOnline.write(users)
                usersOnline.close()

                #sending sucessful message to client
                client.send(response.encode('utf-8'))
                flag = "Access Granted"
                return flag, userName
        else:
            response = "Invalid Username or Password"
            client.send(response.encode('utf-8'))# send message to server
            userName = "Invalid Username"
    return flag, userName




while True:
    print("\nWaiting for connection......")
    client, address = server.accept()
    print("connected from: ", address)
    handler = ClientHandler(client)
    handler.start()
    

