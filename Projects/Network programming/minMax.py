bufsize = 1024
def statistics(client, orgList):
    timeList = []
    for index in orgList:
        timeList.append(int(index[3]))
    
    minimum = minVal(timeList)
    req = client.recv(bufsize) #receive request from client
    minRequest = req.decode('utf-8')
    
    if minRequest == "Requesting Minimum":
        client.send(str(minimum).encode('utf-8')) #send minRequest to server

    maximum = maxVal(timeList)
    request = client.recv(bufsize) #receive request from client
    request = request.decode('utf-8')
    
    if request == "Requesting Maximum":
        client.send(str(maximum).encode('utf-8')) #send maxRequest to server
        average = mean(timeList)
    request = client.recv(bufsize) #receive request from client
    request = request.decode('utf-8')
    
    if request == "Requesting Mean":
        client.send(str(average).encode('utf-8')) #send requesting mean to server
    return "continue"
#send mean, min and max of connection time    
def minVal(timeList):
    minimum = timeList[0]
    for index in timeList:
        if index < minimum:
            minimum = index
    return minimum

def maxVal( timeList ):
    maximum = timeList[0]
    for index in timeList:
        if index > maximum:
            maximum = index
    return maximum

def mean(timeList):
    length=len(timeList)
    add=0
    for index in timeList:
        add += index
    average = add/length
    return average

