mts = ("ingles","espanhol","portugueis")

nome = input("digite o nome do aluno:")

idade = int(input("digite a idade do aluno:"))

aluno = {
    "nome": nome,
    "idade": idade,
    "mts": mts,
}

hobbis = set()
print('\ndigite 3 hobbis do aluno')
while len(hobbis) < 3:
    hobby = input(f"hobby {len(hobbis)+1}: ") 
    if hobby in hobbis:
        print("esse hobbie já foi adicionado")
    else:
        hobbis.add(hobby)

print("==== cadastro ====")

print("nome:", aluno ["nome"])
print("idade:", aluno["idade"])

print("\nmatérias:")
print(aluno["mts"])

print("\nHobbeis: ")
print(hobbis)