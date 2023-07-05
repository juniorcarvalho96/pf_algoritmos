def main():
    arquivo = open("alegria.txt","a") 
    arquivo.write("a vida é boa\n o dia de amanhã será melhor!,\nvocê alcançará seus sonhos!,\no pior já passou.,\no dia está lindo hoje.,\npense positivo sempre.,\nfaremos um grande futuro juntos.,\nvocê está fantástico hoje.,\nvocê é excelente.,\n não desista eu estou com você!,\n sua inteligência sempre me surpreende.,\n viva feliz consigo mesmo.,\n não fique triste eu estou aqui.,\n sua vida é preciosa.,\n a cada dia você está mais esplêndido!,\n os seus sofrimentos não perdurarão eu sei!,\n confie no seu potencial eu confio.,\n vamos ficar juntos nessa!\n seus olhos são lindos.coração, fique bem.")
    arquivo = open("alegria.txt","r")
    nome = input("Qual seu nome?")
    saudacao = arquivo.readline(98)
    print(f"Olá {nome}, {saudacao}")
    n = int(input("digite um numero,0-para sair"))
    while n > 0:
        saudacao = arquivo.readline(98)
        print(f"Olá {nome}, {saudacao}")
        n = int(input("digite um numero,0-para sair"))
main()
    
