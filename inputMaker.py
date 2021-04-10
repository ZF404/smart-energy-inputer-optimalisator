import numpy as np
import random as random



class inputMaker:
    
    
    def check_temp(self, temp):
        file = r"C:\Users\user\Desktop\bhl\podgrzewanie.txt"
        dane = []
        with open( file , "r" ) as f:
            for line in f:
                dane.append(line.split())
        for i in range(0,len(dane)):
            x=dane[i]
            if temp >= int(x[0]) and temp < int(x[1]):
                return([float(x[2]),float(x[3]),float(x[4])])

    def oczekiwana(self, free_work, hour):
        file = r"C:\Users\user\Desktop\bhl\oczekiwana.txt"
        dane=[]
        with open(file,"r") as f:
            for line in f:
                dane.append(line.split())
        for i in range(0,len(dane)):
            x=dane[i]
            if free_work==x[0] and hour>= float(x[1]) and hour < float(x[2]):
                return([int(x[3])])

    def get_wof(self, month, hour, sun):
        file = r"C:\Users\user\Desktop\bhl\fotowoltaika.txt"
        dane=[]
        with open(file,"r") as f:
            for line in f:
                dane.append(line.split())
        for i in range(0,len(dane)):
            dane[i]=[float(y) for y in dane[i]]
            x=dane[i]
            if (month in x[0:3]) and hour >= x[4] and hour < x[5] and sun>=x[6] and sun<x[7]:
                return([x[8]])

    def power_cost_revenue(self, month, free_work, hour):
        file = r"C:\Users\user\Desktop\bhl\siec.txt"
        dane = []
        with open( file , "r" ) as f:
            for line in f:
                split=line.split()
                dane.append(split)
        for i in range(0,len(dane)):
            x=dane[i]
            months=x[0:5]
            months=[int(y) for y in months]
            if month in months and x[6]==free_work and hour >= int(x[7]) and hour < int(x[8]):
                return([float(x[9]),float(x[10])])

    def inne(self, free_work_wakacje, hour):
        file = r"C:\Users\user\Desktop\bhl\urzadzenia.txt"
        dane = []
        with open( file , "r" ) as f:
            for line in f:
                split=line.split()
                dane.append(split)
        for i in range(0,len(dane)):
            if free_work_wakacje==dane[i][0] and hour>=int(dane[i][1]) and hour<int(dane[i][2]):
                return([float(dane[i][3])])


    def return_all(self, temp , sun, month, day, hour ):
        lista = [self.check_temp(temp), self.oczekiwana(day,hour) , self.get_wof(month,hour,sun) , self.inne(day,hour),self.power_cost_revenue(month,day,hour) ]
        return lista

input = inputMaker()
print(input.return_all(15,60,2,"work",15))

def optimisation(foto_excess , ACCU_loaded, month, hour , day , power_cost_revenue):
    if foto_excess==True and (power_cost_revenue(month,day,hour))[1] == 2.5:
        return("B")
    elif foto_excess==True and ACCU_loaded==False and power_cost_revenue(month,day,hour)[1] != 2.5:
        return("A")
    elif foto_excess==False and ACCU_loaded==False and power_cost_revenue(month,day,hour)[1] <= 1:
        return("C")
    else:
        return("D")

print(optimisation(True,True,10,15,"free",input.power_cost_revenue))



