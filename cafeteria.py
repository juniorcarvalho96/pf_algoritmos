def main():
    
    numero_comandas = int(input("digite o numero de comandas: "))
    produtos = {"id" : [0,9,8,7,6], "nome": ["cafe,bolo,refrigerante,salgado,salada"], "valor" : [8,9,5,5,7]}
    comanda = [1] * numero_comandas
    Comandas = {"id":[],"numero": comanda}
    itemComanda = {"id" : [], "produto_id" : produtos["id"], "comanda_id" : Comandas["id"], "quantidadeItem": []}
    
    
    def carregar_arquivos():
        arquivo_produto = open("produtos.txt","a")
        arquivo_comandas = open("comandas.txt","a")
        arquivo_itens = open("itens.txt","a")
        return arquivo_produto,arquivo_comandas,arquivo_itens
    carregar_arquivos()
    

    
    
    
    def cadastrarItem(products):
        item = int(input("deseja cadastrar um novo produto? 0- não, qualquer outro valor sim: "))
        while item != 0: 
            products["id"].append(input("id do novo item: "))
            products["nome"].append(input("nome do novo item: "))
            products["valor"].append(int(input("digite o valor do produto")))
            item = int(input("deseja cadastrar um novo produto? 0- não, qualquer outro valor sim: "))
        return products
    
    
    
    def adicionar_item_a_comanda(comandas):
        comanda["id"].append(int(input("identificador da sua comanda: ")))
        itemComanda["produtos_id"].append(input("digite o nome do item: "))
        itemComanda["quantidadeItem"].append(input("digite a quantidade: "))
        return itemComanda["produtos_id"],itemComanda["quantidadeItem"]
        
        
    def MostrarCardapio(produtos):
        print("ID : ")
        print(produtos["id"])
        
        print("NOMES: ")
        print(produtos["nome"])
        
        print("Valores: ")
        print(produtos["valor"])
   
    
    
    def Mostrar_Itens_Comanda(produtos,itemComanda):
        conta_final = 0
        for j in range(len(itemComanda["quantidadeItem"])):
            conta_final += produtos["valor"][j] * itemComanda["quantidadeItem"][j]
        return print(conta_final)
    
      
      
    def Pagar_comanda(itemComanda):
        total_vendido = 0
        conta_final = 0
        conta_final += total_vendido
        itemComanda = itemComanda = {"id" : [], "produto_id" : produtos["id"], "comanda_id" : Comandas["id"], "quantidadeItem": []}
        return print(conta_final)
    
        
    def numera_comanda(comandas):
        for j in range(1, len(comandas)):
            if j >= 1 :
                comandas[j] = j + 1
        return comandas
    
    def menu():
        print("1.cadastrar novo item\n2.adicionar um item a comanda\n3. mostrar cardapio\n4. mostrar item da comanda \n5.pagar comanda\n6.valor vendido\n")
        opcao = int(input(""))
        while opcao != 0:
            if(opcao == 1):
                cadastrarItem(produtos)
            elif(opcao == 2):
                adicionar_item_a_comanda(Comandas) 
            elif(opcao == 3):
                MostrarCardapio(produtos) 
            elif(opcao == 4):
                Mostrar_Itens_Comanda(produtos,itemComanda)
            elif(opcao == 5):
                Pagar_comanda(itemComanda) 
            elif(opcao == 6):    
                print(f"valor total vendido: {Pagar_comanda(itemComanda)}") 
            else:
                print("erro...")
            print("1.cadastrar novo item\n2.adicionar um item a comanda\n3.mostrar cardapio\n4. mostrar item da comanda \n5.pagar comanda\n6.valor vendido\n0.sair")
            opcao = int(input(""))
        numera_comanda(comanda)
    
    menu()
   
main()
