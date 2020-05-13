bufsize = 1024
def server_Details(client, orgList):
    flag = "Organisation Name not found"
    for index in [1, 2, 3]:
        print ("Waiting for the Organisation Name..")
        orgNameRecv = client.recv(bufsize) #receive organisation name
        orgName = orgNameRecv.decode('utf-8')
        print ("Organisation Name received is ", orgName)
        
        for index in orgList:
            if index[0] == orgName:
                flag = "Organisation Name found"
                details = index
                
        if flag == "Organisation Name not found":
            client.send(flag.encode('utf-8')) #send status to server
        elif flag == "Organisation Name found":
            client.send(flag.encode('utf-8'))
            print (flag)
            reqServerName = client.recv(bufsize) #receive serverName from client
            reqServerName = reqServerName.decode('utf-8')
            client.send(details[1].encode('utf-8'))
            reqIPAdd = client.recv(bufsize) #receive ipAddress from client
            reqIPAdd = reqIPAdd.decode('utf-8')
            client.send(details[2].encode('utf-8'))
            return "continue"
        else:
            if index != 3:
                print ("\nOrganisation Name not found\n")
        
    return "end"
