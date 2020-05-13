#deleting organisation
bufsize = 1024
def remove_Organisation(client, orgList):
    for index in [1, 2, 3]:
        print ("Waiting for the Organisation Name")
        flag = "Organisation doesn't exist"
        orgName = client.recv(bufsize) #receive orgName from client
        orgName = orgName.decode('utf-8')
        
        for index in orgList:
            if index[0] == orgName: #check if Organisation name exists in File
                print ("\nDeleting Organisation Name...\n")
                flag = "Organisation exist"
                client.send(flag.encode('utf-8')) #send organisation to server

                orgList.remove(index) #deleting Organisation from the list
                
                newOrgList = open ("organisations.txt", 'w')
                for index in orgList:
                    newOrgList.write(" ".join(index))
                    newOrgList.write("\n")
                newOrgList.close()
                message = "Organisation Deleted"
                print (message)
                client.send(message.encode('utf-8')) #send message to server
                return "continue"
        client.send(flag.encode('utf-8'))
    return "end"
        
