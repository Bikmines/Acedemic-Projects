# sorting alphabetically or numerically
bufsize = 1024
def sorting(client, orgList):
    choiceRecv = client.recv(bufsize)
    choiceReceived = choiceRecv.decode('utf-8')
    if choiceReceived == '1':
        message = sortAlphabetically(client, orgList)
    elif choiceReceived == '2':
        message = sortNumerically(client, orgList)
    else:
        message = "Please choose from the options given: "
    client.send(message.encode('utf-8'))
    return "continue"

#sort by alphabetically
def sortAlphabetically(client, orgList):
    orgList.sort()
    newOrgList = open ("organisations.txt", 'w')
    for index in orgList:
        newOrgList.write(" ".join(index))
        newOrgList.write("\n")
    newOrgList.close()
    return "Sorting completed Alphabetically"
def fourthElement(elem):
    return elem[3]

#sort by numerically
def sortNumerically(client, orgList):
    orgList.sort(reverse = True, key = fourthElement)
    newOrgList = open ("organisations.txt", 'w')
    for index in orgList:
        newOrgList.write(" ".join(index))
        newOrgList.write("\n")
    newOrgList.close()
    return "Sorting Numerically"
