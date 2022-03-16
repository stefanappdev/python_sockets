

import socket

agent_log=open("agent_chat_log.txt","w")
if not agent_log:
    print("Unable to access log file")

# port number to connnect to server 
PORT = 65000
# The Server's IP Address
SERVER_IP = "192.168.0.18"

# Set up the Server's Address
ADDR = (SERVER_IP,PORT)
FORMAT = 'utf-8'


#  initialize the client Socket and connect with server.
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

# Write Code that will allow the Client (Agent) to send messages to the server. The Function accepts the message as a String (msg) and sends that message to the Server through a connection established.
def send(msg):
    client.send(msg.encode(FORMAT))
    

# Write code to Prompts the Agent to enter their connection code and returns the code given.
def getConCode():
    concode=input("Enter your connection code: ")
    return concode


# Write code to Prompts the Agent to enter an answer and returns the answer given.
def getAnswer(question):
    answer=input("Please enter answer to the question provided: ")
    return answer

# Get Connection Code.
connCode = getConCode()

# Send Connection Code to Server.
send(connCode)
agent_log.write("sucessfully sent message to server\n")

# Recive question from server.
server_question= client.recv(250).decode(FORMAT)
print(server_question)
agent_log.writelines(f"received question from server:{server_question}"+"\n")

# Get Answer from Agent.
answer = getAnswer(server_question)

# Send Answer to Server.
send(answer)
agent_log.writelines(f"sending answer to server:{answer}"+"\n")


# Receive and print response from the server.
server_response=client.recv(250).decode(FORMAT)
print(server_response)



