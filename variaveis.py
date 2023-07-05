def main():
    n = int(input("digite o numero de varaveis: "))
    novaString = []
    string0 = ""
    fechar = 1
    while (fechar != 0):
        string = input("digite uma string: ")
        for item in string:
          if ord(item) != 95:
            novaString.append(item)
        for j in range(len(novaString)):
          string0 = string0 + novaString[j]
        print(string0)
        novaString.clear()
        string0 = ""
        n -= 1
        if n == 0:
            break
        fechar = int(input("digite um numero:0-para fechar o programa"))
       
        
        
main()

