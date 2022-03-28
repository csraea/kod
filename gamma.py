
# Python3 implementation
import sys
from math import log
from math import log
from math import floor

def Elias_Omega(item):
    result = [0]
    number = item

    while number > 1:
        code = base_ns.convert(number, 2).integer

        number = len(code) - 1
        result = code + result

    return result
  
log2 = lambda x: log(x, 2)
  
def Unary(x):
    print("Unary:\t\t" + str((x-1)*'0'+'1'))
    return (x-1)*'0'+'1'

def Binary(x):
    binary = "{0:b}".format(int(x))
    print("Binary:\t\t" + str(binary))
    binary_without_MSB = binary[1:]
    print("Binary':\t" + str(binary_without_MSB))
    return binary_without_MSB
 
def Binary_Representation_Without_MSB(x):
    binary = "{0:b}".format(int(x))
    binary_without_MSB = binary[1:]
    return binary_without_MSB
 
def Elias_Gamma(k):
    if (k == 0):
        return '0'
    N = 1 + floor(log(k, 2))
    Unary = (N-1)*'0'+'1'
    return Unary + Binary_Representation_Without_MSB(k)
 
def Elias_Delta(k):
    Gamma = Elias_Gamma(1 + floor(log(k, 2)))
    binary_without_MSB = Binary_Representation_Without_MSB(k)
    return Gamma+binary_without_MSB

#Elias Omega
def recursive_elias(n): #get elias integer code recursively
    s = ""
    if n>1:
        b = bin(n)[2:]
        stringb = str(b)
        b = stringb.replace("1","0",1)
        s += recursive_elias(len(b)-1) + b
    
    if n == 1:
        s+= "0"
    return s

def Elias_Omega(n):
    b = bin(n)[2:]
    n = len(b)-1
    return recursive_elias(n)+b

    

def main():
    Unary(int(sys.argv[1]))
    Binary(int(sys.argv[1]))
    print("Gamma':\t\t" + Elias_Gamma(int(sys.argv[1])))
    print("Delta:\t\t" + Elias_Delta(int(sys.argv[1])))
    print("Omega:\t\t" + Elias_Omega(int(sys.argv[1])))
    
if __name__ == "__main__":
    main()