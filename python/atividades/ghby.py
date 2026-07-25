with open("agentes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Phonix - D\n")
    arquivo.write("Fade - I\n")
    arquivo.write("Clove - C\n")
    arquivo.write("Chamber - S\n")

print("arquivo criado com sucesso!")

with open("agentes.txt", "r", encoding="utf-8") as arquivo:
    x = arquivo.read()
    print(x)

    