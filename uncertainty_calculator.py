import math

class unit:
    number=0
    uncertainty=0

    def rd(self):
        
        sig=50
        self.number=round(self.number,sig)
        self.uncertainty=abs(round(self.uncertainty,sig))
    def __init__(self,number,uncertainty):
        self.number=number
        self.uncertainty=uncertainty
    def __add__(self,other):
        tmp=unit(0,0)
        tmp.number=self.number+other.number
        tmp.uncertainty=self.uncertainty+other.uncertainty
        tmp.rd()
        return tmp
    def __sub__(self,other):
        tmp=unit(0,0)
        tmp.number=self.number-other.number
        tmp.uncertainty=self.uncertainty+other.uncertainty
        tmp.rd()
        return tmp
    def __mul__(self,other):
        tmp=unit(0,0)
        tmp.number=self.number*other.number

        rel_num=self.uncertainty/self.number
        rel_other=other.uncertainty/other.number

        rel=rel_num+rel_other
        tmp.uncertainty=rel*tmp.number

        tmp.rd()
        return tmp
    def __truediv__(self,other):
        tmp=unit(0,0)
        tmp.number=self.number/other.number

        rel_num=self.uncertainty/self.number
        rel_other=other.uncertainty/other.number

        rel=rel_num+rel_other
        tmp.uncertainty=rel*tmp.number

        tmp.rd()
        return tmp
    def __pow__(self,value):
        tmp=unit(0,0)
        rel=self.uncertainty/self.number
        rel*=value.number

        tmp.number=pow(self.number,value.number,None)
        tmp.uncertainty=tmp.number*rel
        tmp.rd()

        return tmp

    def intro(self):
        print("number: "+str(self.number))
        print("uncertainty: "+str(self.uncertainty))
        print("relative uncertainty: "+str(self.uncertainty/self.number))

# m1=unit(1,0.01)
# m2=unit(2,0.03)

# m1.intro()
# m2.intro()
# print()
# m3=m1*m2
# m3.intro()

def cos(un):
    tmp=unit(0,0)
    tmp.number=math.cos(un.number/180*math.pi)
    tmp.uncertainty=math.cos((un.number+un.uncertainty)/180*math.pi)-tmp.number
    tmp.rd()
    return tmp

def sin(un):
    tmp=unit(0,0)
    tmp.number=math.sin(un.number/180*math.pi)
    tmp.uncertainty=math.sin((un.number+un.uncertainty)/180*math.pi)-tmp.number
    tmp.rd()
    return tmp


num=input("please input the number of variables:")

var=list()

for i in range(0,int(num)):
    var.append(unit(float(input("Please input number for variable"+str(i)+": ")),\
        float(input("Please input uncertainty for variable"+str(i)+": "))))

print("-"*60)

for num,itm in enumerate(var):  
    print("variable"+str(num)+": ")
    itm.intro()
    print()

while(1):
    print("-"*60)

    exp=input("please input the expression: ")
    
    res=eval(exp)
    res.intro()

