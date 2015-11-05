__author__ = 'stregula'
__version__ = "1.0"

import sys
import uuid
import re

if len(sys.argv) < 3:
    sys.exit('Usage: %s <inspector_output_file> <formatted_postmancoll_file>' % sys.argv[0])

filename = sys.argv[1]
collectionFile = sys.argv[2]

# This will be the file where the google postman formatted collection is stored
target = open(collectionFile, 'w')
target.write("{\n")

# Replace these with your own owner numbers
target.write("\t\"owner\": \"999999\",\n")
target.write("\t\"lastUpdatedBy\": \"999999\",\n")
target.write("\t\"lastRevision\": 72432501,\n")
target.write("\t\"team\": null,\n")

# Using random uuids for this, you may decide to seed them with something different
collectionId = uuid.uuid4()
target.write("%s%s%s" % ("\t\"id\": \"", collectionId, "\",\n"))
target.write("\t\"name\": \"AutomatedCollection\",\n")
target.write("\t\"description\": \"A collection generated by raw ACI inspector output\",\n")
target.write("\t\"remoteLink\": null,\n")
target.write("\t\"order\": [")

# Read the copy/paste/saved output from ACI Inspector sequentially
file_object = open(filename, 'r')

requestNum = 0
requestLine = ""
for line in file_object:
    newLine = re.sub('^.*url: ', '', line)
    #print newLine

    # find URL and payload
    request = newLine.split(" payload")
    print(request[0])
    request[1] = re.sub(' response: \{"imdata":\[\]\}', '', request[1])
    print(request[1])

    if requestNum > 0: 
        requestLine += "\n\t\t},\n"
        target.write(",\n")
    else:
        target.write("\n")
    requestLine += "\t\t{\n"
    requestLine += "\t\t\t\"folder\": null,\n"
    requestId = uuid.uuid4()
    requestLine += "\t\t\t\"id\": \"" + str(requestId) + "\",\n"
    requestLine += "\t\t\t\"name\": \"" + str(requestNum) + "\",\n"
    requestLine += "\t\t\t\"dataMode\": " + "\"raw\",\n"
    requestLine += "\t\t\t\"data\": " + "[],\n"
    requestLine += "\t\t\t\"descriptionFormat\": " + "\"html\",\n"
    requestLine += "\t\t\t\"description\": " + "\"\",\n"
    requestLine += "\t\t\t\"headers\": " + "\"\",\n"
    requestLine += "\t\t\t\"method\": " + "\"POST\",\n"
    requestLine += "\t\t\t\"pathVariables\": " + "{},\n"
    requestLine += "\t\t\t\"url\": " + "\"" + request[0] + "\",\n"
    requestLine += "\t\t\t\"preRequestScript\": " + "\"\",\n"
    requestLine += "\t\t\t\"tests\": " + "\"\",\n"
    requestLine += "\t\t\t\"currentHelper\": " + "\"normal\",\n"
    requestLine += "\t\t\t\"helperAttributes\": " + "{},\n"
    requestLine += "\t\t\t\"collectionId\": " + "\"" + str(collectionId) + "\",\n"
    #request[1] = re.sub('"', '\"', request[1])
    request[1] = request[1].replace("\"", '\\"')
    requestLine += "\t\t\t\"rawModeData\": " + "\"" + request[1].rstrip() + "\"\n"


    requestNum = requestNum + 1
    #print requestLine

    target.write("\t\t\"" + str(requestId) + "\"")

# Add the request blocks and then close them out
target.write("\n\t],")
target.write("\n\t\"requests\": [\n")
target.write(requestLine)
target.write("\t\t}\n\t]\n}")

# Done, now import the file into postman using the 'import' button
