class compound:
    def __init__(self,num):
        print(f"An Instance {num} is created to calculate compound interest")
        
    def compound(self,p,r,t):
        self.principal=p
        self.rate=r
        self.time_period=t
        compound_interest=(self.principal*self.rate*self.time_period)/100
        return compound_interest
    

x=compound(1)
print(x.compound(10,2,5))