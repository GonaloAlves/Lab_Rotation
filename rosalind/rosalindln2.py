#import math 
#from math import sqrt 

def hyp_squared(file_name):
        values = open(file_name, "r").read().split()
        a = int(values[0])
        b = int(values[1])
        return a**2 + b**2

if __name__ == '__main__':
        print (hyp_squared("/home/mako/PE/rosalind_ini2.txt"))


""" tea_party = ['March Hare', 'Hatter', 'Dormouse', 'Alice','Mako','Marco']
#print (tea_party[0])

#tea_party[1] = 'Cheshire Cat'
print (tea_party[4:])

a = 'flimsy'
b = 'miserable'
g = a[2:]
c = b[0:1] + a[2:]
print (g) """



#a = 947
#b = 925
#c = a**2 + b**2
#print(c)
#print (sqrt(c))
#print(math.sqrt(c))
