def pergunta_Numero():
    numero = 1
    while True:
        try:
            val = str(input("por favor digite um inteiro: "))
        except:
            print("Parece que você não digitou um inteiro!")
            continue
        else:
            print("Muito bem!!")
            break
        finally:
            print("Tentativa numero: ", numero)
            numero = numero + 1
    print(val) 

pergunta_Numero()