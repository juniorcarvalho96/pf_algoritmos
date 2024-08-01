string = input("")
lista = []
op = string[6] 


for i in range(len(string)):
    if (i <= 12) and (i%4 == 0):
        lista.append(string[i])
        
for i in range(len(lista)):  
    int(lista[i])
        
def operacao(lista):
    if op == "+":
        d = lista[0] / lista[1] 
        k = lista[2] / lista[3]
        print(d+k)
        
    if op == "-":
        d = lista[0] / lista[1] 
        k = lista[2] / lista[3]
        print(d - k)
        
    if op == "*":
        d = lista[0] / lista[1] 
        k = lista[2] / lista[3]
        print(d * k)
        
    if op == "/":
        d = lista[0] / lista[1] 
        k = lista[2] / lista[3]
        print(d / k)
        

