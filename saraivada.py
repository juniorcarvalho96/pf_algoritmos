import random
def main():
    lista = []
    volume_chuva = 0
    numero_de_pedras = int(input("quantas pedras vc quer?"))

    while (numero_de_pedras > 50 or numero_de_pedras < 0):
        numero_de_pedras = int(input("quantas pedras vc quer?"))

    while numero_de_pedras > 0:
        numero_de_pedras -= 1
        volume_pedra = random.randint(1, 50)
        volume_chuva += volume_pedra
        lista.append(volume_pedra)
    print(f"volume total da chuva:{volume_chuva/1000 :.2f} L")

    def minimos(l):
        contador = 0
        volume = 0
        for i in l:
            if i == min(l):
                contador += 1
                volume += min(l)
        return print(f"quantidade de volumes minimos: {contador}\nvolume total minimos: {volume}\nporcentagem: {(volume_chuva/volume)}%")

    def maximos(l):
        contador = 0
        volume = 0
        for i in l:
            if i == max(l):
                contador += 1
                volume += max(l)
        return print(f"quantidade de volumes maximos: {contador}\nvolume total maximos: {volume}\nporcentagem: {(volume_chuva/volume)}%")

    def valores_primos(l):
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39, 41, 43, 47]
        novo_primos = []
        for i in l:
            if i in primos:
                novo_primos.append(i)
        return print(novo_primos)
    def diferenca(l):
        soma = 0
        soma_multiplo = 0
        for i in range(len(l)):
            if i%2 == 0:
                soma += l[i]
        m = random.randint(8,90)
        for j in range(len(l)):
            if l[j] % m == 0:
                soma_multiplo += l[j]
        diff = soma - soma_multiplo
        return diff
    def volume_medio(l):
        soma_media = []
        medio = sum(l)/len(l)
        for i in range(len(l)):
            if l[i] <= 0.3 * medio:
                soma_media.append(l[i])
        resultado_final = sum(soma_media)/len(l)
        return resultado_final
            
                
                
    maximos(lista)
    minimos(lista)
    valores_primos(lista)
    print(diferenca(lista))
    print(volume_medio(lista))


main()

