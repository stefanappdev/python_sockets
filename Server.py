

import socket
from datetime import datetime
import threading
import Verify as av

server_log=open("server_log.txt","w")
if not server_log:
        print("Unable to access log file")

# Select an appropriate port number. 
PORT = 65000

# Set The Server's IP Address
SERVER_IP = "192.168.0.18"

# Set up the Server's Address
ADDR = (SERVER_IP, PORT)

FORMAT = 'utf-8'

# Add code to initialize the socket
try:
    print("creating socket for server...")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print("socket creation failed, exiting...")
    server_log.write("Server crashed due to socket errors\n")
    exit(-1)

try:
    print("Attempting to binding ip and port to server...")
    server.bind(ADDR)

except socket.error:
        print("binding failed, exiting...")
        server_log.write("Server crashed due to binding errors\n")
        exit(-1)
else:
        print("binding is sucessful")




 # This function processes messages that are read through the Socket.
def clientHandler(conn, addr): 

    

    agent_name=None
            
            
            
            
            
    def greetings():
                    localtime=datetime.now()
                    acknowlegdement=f"Welcome agent {agent_name} time logged in:{localtime}"
                    conn.send(acknowlegdement.encode(FORMAT))
                    server_log.write(f"{agent_name} has logged in sucessfully \n")
                    server.close()
                


 # Write Code that allows the Server to receive a connection code from an Agent. 
    conn_code=conn.recv(250).decode(FORMAT)
    print(f"from client{addr}:",conn_code)


# allows the Server to check if the connection code received is valid and sends random question. 
    
    agent_name=av.check_conn_codes(conn_code)
     
    
  
    if agent_name=="A" or agent_name=="B":
        
                print(agent_name)
                print("Verified connection code used")
                print("generating questions.......")
                sq=av.getSecretQuestion()
                sq_quest=sq[0]
                sq_ans=sq[1]
                print("Question:",sq_quest)
                print("Answer:",sq_ans)
                conn.send(sq_quest.encode(FORMAT))
                agent_answer=conn.recv(250).decode(FORMAT)
                server_log.write(f"Server question sent to agent: {sq_quest}\n")
                server_log.write(f"answer from agent: {agent_answer}\n")

             # allows the Server to check if the answer received is correct.
                print("checking results..")
                if agent_answer==sq_ans:
                        print("Correct!!")
                        greetings()
                else:
                    print("incorrect")
                    print(f"Unknown agent trying to access server,closing connection with agent {agent_name}...")
                    server_log.write("Server closed due to detected breaahes\n")
                    exit(-1)
                    server.close()
        
    else:
        print(f"Unknown agent trying to access server,closing connection with agent {agent_name}...")
        server_log.write("Server crashed due to detected breaches\n")
        exit(-1)
        server.close()     




                
                
                
#need to fix threading causes an issue when used
def runServer():
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    server_log.write("Server startup is sucessful\n")
    server.listen(2)
    
   
    while True:
    #finish multithreading in handler
        Agent,addr = server.accept()
        thread = threading.Thread(target=clientHandler, args=(Agent,addr) )
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")
        thread.start()
            
        


print("[STARTING] The Server is Starting...")
runServer() 

















'''
# Write Code that allows the Server to retrieve a random secret question.
    """Your Code here"""
    # Write Code that allows the Server to receive an answer from the Client.
    """Your Code here"""
    # Write Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X" 
    """Your Code here"""
    '''