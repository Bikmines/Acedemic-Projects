#adding a newOrganisation
bufsize=1024
def add_Organisation(client, orgList):
    for index in [1, 2, 3]:
        flag = "Add Organisation"
        #Get organisation details
        orgName = client.recv(bufsize)
        orgName = orgName.decode('utf-8')
        svrName = client.recv(bufsize)
        svrName = svrName.decode('utf-8')
        ipAdd = client.recv(bufsize)
        ipAdd = ipAdd.decode('utf-8')
        noMinutes = client.recv(bufsize)
        noMinutes = noMinutes.decode('utf-8')

        print ("New Organisation Details Received")
        #Check if Organisation name exists
        for index in orgList:
            if index[0] == orgName:
                print ("\nOrganisation already exist")
                flag = "Existing Organisation Name"
                client.send(flag.encode('utf-8'))
                break
        #Add Organisation name to organisations.txt file
        if flag == "Add Organisation":
            currentOrg = open ("organisations.txt", 'a')
            currentOrg.write("\n" + orgName + " " + svrName + " " + ipAdd + " " + noMinutes)
            currentOrg.close()
            client.send(flag.encode('utf-8'))
            return "continue"

    return "end"
