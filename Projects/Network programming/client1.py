#client side program
from socket import *
bufsize = 1024

def main():
    host = gethostname()
    port = 6666
    address = (host, port)
    
    client = socket(AF_INET, SOCK_STREAM)
    try:
        #connecting  to server
        client.connect(address)
        welcomeMsg = client.recv(bufsize)
        status = ""
        choice= ""
        #displaying welcome message 
        print(welcomeMsg.decode('utf-8'))
        authStatus = authentication(client)
        if authStatus == "Access Denied":
            print ("end")
        else:
            print (authStatus +"\nChoose an option")
            choice = menu()
            client.send(str(choice).encode('utf-8')) #send choice to server 
            while choice != 6:
                choice = str(choice)
                if choice == "1":
                    status = orgDetails(client)
                elif choice == "2":
                    status = statistics(client)
                elif choice == "3":
                    status = sorting(client)
                elif choice == "4":
                    status = addNewOrganisation(client)
                elif choice == "5":
                    status = removeOrganisation(client)
                else:
                    print ("Please enter the choice from the given range")
                 #choice = int(choice)
                    
                choice = 6
                if status == "continue":
                    choice = menu()
                    client.send(str(choice).encode('utf-8'))
    except ConnectionRefusedError:  #exception handling
        print ("Server not Active")
        status = "end"
        choice = 6
        
   
        
    print("Client is Terminated")
    if status != "end":
        choice = str(choice)
        client.send (choice.encode('utf-8')) #send choice to server
    client.close()  #close the  connection to server
            
def authentication(client):
    flag = "Access Denied"
    for index in [1, 2, 3]:
        
        userName = input ("Username: ") #enter the userame
        client.send(userName.encode('utf-8')) #send username to server
        
        password = input ("Password: ") #Enter the password
        client.send(password.encode('utf-8')) #send password to server

        authMsg = client.recv(bufsize) #receive authentication from client
        authMsg = authMsg.decode('utf-8')

        if authMsg == "Connection Successful":
            print ("Connected to the Server")
            flag = "Access Granted"
            return flag
        elif authMsg == "User already in use":
            print ("Username already in use. Please use different Authentication")
        else:
            if index != 3:
                print ("\nInvalid Username or Password.\nTry Again\n")
                
    print ("\n3 incorrect attempts!! \n Disconnecting from the Server...\n")
    return flag
#check for orgDetails
#prompt for display orgDetails
def orgDetails(client):
    status = "Organisation Name not found"
    for index in [1, 2, 3]:
        orgName = input ("Enter an Organisation Name: ")
        client.send(orgName.encode('utf-8')) #send organisation name to server
        status = client.recv(bufsize) #receive status from client
        status = status.decode('utf-8')
        if status == "Organisation Name found" :
            status = "Thank you"
            reqServerName = "Requesting servername:"
            client.send(reqServerName.encode('utf-8')) 
            
            serverName = client.recv(bufsize)
            name = serverName.decode('utf-8')
            print("The ServerName is:",name)

            reqIPAdd= "Requesting IPaddress:"
            client.send(reqIPAdd.encode('utf-8')) #send ipAddress to server
            
            ipAddress = client.recv(bufsize) #receive ipAddress from client
            ipName = ipAddress.decode('utf-8')
            print("The Ip address is:",ipName)
            return "continue"        
        elif status == "Organisation Name not found":
            print (status)
            if index != 3:
                print ("\nEnter an Organisation Name in Records\n")

    print ("reached Max attempt\n")
    print ("\nDisconnecting from the Server...\n")
    return "end"

#prompt for display statistics
def statistics(client):
    print("Requesting Mean, Minimum value and Maximum value of time from server")
    reqMin = "Requesting Minimum"
    client.send(reqMin.encode('utf-8')) #send minValue to server

    minVal = client.recv(bufsize) #receive minValue from client
    minVal = minVal.decode('utf-8')
    print("The Minimum is:",int(minVal))

    reqMax = "Requesting Maximum"
    client.send(reqMax.encode('utf-8')) #send maxValue to server

    maxVal = client.recv(bufsize) #receive maxValue from client
    maxVal = maxVal.decode('utf-8')
    print("The Maximum is:",int(maxVal))

    reqMean = "Requesting Mean"
    client.send(reqMean.encode('utf-8')) #send mean to server
    
    mean = client.recv(bufsize)
    mean = mean.decode('utf-8') #receive mean from client
    print("The Mean is:",float(mean))

    return "continue"
                       
#Do sorting
def sorting(client):
    choice = sortingMenu()
    client.send(str(choice).encode('utf-8')) #send choice to server
    message = client.recv(bufsize) #receive message from client
    message = message.decode('utf-8')
    print (message)
    return "continue"

#create newOrganisation
def addNewOrganisation(client):
    for index in [1, 2, 3]:
        orgName = input ("Enter new Organisation name: ") 
        client.send(orgName.encode('utf-8')) 
        
        svrName = input ("Enter the Server Name: ") 
        client.send(svrName.encode('utf-8')) 

        ipAdd = input ("Enter the IP Address: ") 
        client.send(ipAdd.encode('utf-8'))

        noMinutes = input ("Enter the number of Minutes: ")
        client.send(noMinutes.encode('utf-8'))
        
        regMessage = client.recv(bufsize)
        regMessage = regMessage.decode('utf-8')

        if regMessage == "Add Organisation":
            print ("New Organisation Successfully created.\n")
            return "continue"
        else:
            if index != 3:
                print("\Organisation name already exists")
    print ("reached Max attempt\n")
    print ("Disconnecting from the server...\n")
    return "end"
   
    

                       
#Erasing the organisation
def removeOrganisation(client):
    for index in [1, 2, 3]:
        orgName = input ("Enter an Organisation name to be deleted: ")
        client.send(orgName.encode('utf-8')) #send organisationName to server

        message = client.recv(bufsize) #receive message from client
        message = message.decode('utf-8')

        if message == "Organisation exist":
            print ("\nDeleting Organisation ...\n")
            status = client.recv(bufsize)
            status = status.decode('utf-8')
            print (status)
            return "continue"
        else:
            if index != 3:
                print("Organisation name doesn't exists")
    print ("reached Max attempt\n")
    print ("\nDisconnecting from the server...\n")
    return "end"
            
def menu():
    print ("\n--------------------------------")
    print ("             Menu               ")
    print ("--------------------------------")
    print ("(1) Get sever name and IP address")
    print ("(2) Get statistics (mean, minimum, maximum)")
    print ("(3) Sort data by name or minutes")
    print ("(4) Add new organisation")
    print ("(5) Remove organisation")
    print ("(6) Quit program")
    try:
        choice = int(input("Enter your choice (1, 2, 3, 4, 5, 6): "))
    except ValueError:
        print ("Please enter the choice from the given range")
        choice = menu()
    return choice

def sortingMenu():
    print ("\n--------------------------------")
    print ("     Sorting Menu               ")
    print ("--------------------------------")
    print ("(1) Sort by Alphabetical Order")
    print ("(2) Sort by Numerical Descending Order")
    try:
        choice = int(input("Enter your choice (1, 2): "))
    except ValueError:
        print ("Please enter the choice from the given range")
        choice = menu()
    return choice

main()
        
    

