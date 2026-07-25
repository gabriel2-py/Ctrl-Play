import chatbot as Pc


nome_maquina = "K_Yo"

Pc.saudacoes(nome_maquina)

while True:
    texto = Pc.recebeTexto()

    resposta = Pc.buscaResposta(
        nome_maquina,
        texto
    )

    if Pc.exibeResposta(
        resposta,
        nome_maquina
    ) == "fim":
        break