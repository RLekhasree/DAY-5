class AmazonService:
    def __init__(self,Agentname,agentId,customerId):
        self.customerId = customerId
        self.Agentname = Agentname
        self.agentId = agentId

agentName = "Trendy" 
AgentId = 1
     
complaint = input("Enter your issue :")
customerId = int(input("enter cust Id :"))
while complaint:
    Agent1 = AmazonService(agentName,AgentId,customerId)
    complaint = False
print("Agent",Agent1.agentId,"is handling customer : ",Agent1.customerId)