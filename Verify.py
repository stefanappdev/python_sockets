

import random

Agent_codes = []


predefined = ["AJK78", "KTV90", "NEL55", "DFG28"]

AgentA = "2975"
AgentB = "6144"

# Write code that will Generate all possible connection codes for the Agents and store them in their respective arrays. 

print("Generating connection codes....")

for pre in predefined:
    Agent_codes.append(pre+AgentA)
    Agent_codes.append(pre+AgentB)

print("connection codes have been generated")

questions = [("I saw a purple Kangaroo yesterday, did you?", "Only after the sun went down"),
             ("What did Eve say when she ate the fruit?", "Nothing"),
             ("What do you call a fish wearing a bowtie?", "Sofishticated"),
             ("What did the ocean say to the beach?", "Nothing it just waved"),
             ("Why did God save men but not fallen angels?", "Good Question")]

#This function should return a random instance from the questions array. 
def getSecretQuestion():
    qrand=random.choice(questions)
    return qrand



#This function must check the connection code given by the client (Agent) and return the name of the Agent (Agent A or B). If the code is invalid the function should return -1.
def check_conn_codes(connCode):
       
       if connCode not in Agent_codes:
       
            return(-1)
            
       elif connCode in Agent_codes:
            
            if connCode[5:]=="2975":
                agent="A"
                  

            elif connCode[5:]=="6144":
                agent="B"
                
       return(agent)
       
       
    




#testing section

print("valid agent codes:",Agent_codes)

'''
print(check_conn_codes("AJK786144"))
print(check_conn_codes("AJK7862975"))
print(check_conn_codes("KTV902975"))   
print(check_conn_codes("vDFG286144")) 
print(check_conn_codes("DFG286144"))
print(check_conn_codes("KTV902975"))


print((getSecretQuestion()))
print((getSecretQuestion()))
print((getSecretQuestion()))
print((getSecretQuestion()))
print((getSecretQuestion()))



sq=getSecretQuestion()
sq_ques=sq[0]
sq_ans=sq[1]
print(sq_ques)
print(sq_ans)
'''