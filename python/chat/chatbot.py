def saudacoes(nome):
    import random
    frase = ["Bom dia! Meu nome é" + nome + ". como vai vocÊ", "Olá", "Oi, tudo bem?"]
    print(frase[random.randint(0,2)])

def recebeTexto():
    texto = "cliente: " + input("Cliente: ")
    palavraProibida = [ "idiota",
    "imbecil",
    "burro",
    "otário",
    "otaria",
    "babaca",
    "besta",
    "estúpido",
    "estupido",
    "estúpida",
    "estupida",
    "retardado",
    "retardada",
    "nojento",
    "nojenta",
    "lixo",
    "merda",
    "porra",
    "caralho",
    "cacete",
    "foda",
    "foder",
    "fodase",
    "foda-se",
    "vai se foder",
    "puta",
    "puto",
    "putaria",
    "pqp",
    "filho da puta",
    "filha da puta",
    "desgraçado",
    "desgracado",
    "desgraçada",
    "desgracada",
    "cu",
    "cuzão",
    "cuzao",
    "viado",
    "veado",
    "bicha",
    "arrombado",
    "arrombada",
    "corno",
    "corna",
    "safado",
    "safada",
    "vagabundo",
    "vagabunda",
    "maldito",
    "maldita",
    "inferno",
    "merdinha",
    "porra nenhuma"]
    for p in palavraProibida:
        if p in texto:
            print("Não vem não! Me respeite!")
            return recebeTexto()
        return texto

def buscaResposta(nome, texto):
    with open("informacoes.txt","+a") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("cliente: ","") == "Tchau":
                    print(nome+ ": volte sempre!")
                    return "fim"
            elif viu.strip() == texto.strip():
                proximalinha = conhecimento.readline()
                if "Chatbot: " in proximalinha:
                    return proximalinha
        else:
            print("me desculpe, não sei o que falar")
            conhecimento.write("\n" + texto)
            resposta_user = input("O que esperava?\n")
            conhecimento.write("\n" + "Chatbot: "+resposta_user)
            return "Hum..."
        
def exibeResposta(resposta, nome):
    print(resposta.replace("Chatbot",nome))
    if resposta == "fim":
        return "fim"
    return "continua"

