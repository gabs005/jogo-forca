import random

# Função para jogar o jogo da forca
def jogar_forca():
    print("================")
    print("🎯Seja Bem Vindo ao Jogo da Forca!")
    print("================")

    # Listando palavras para o jogo
    palavras = [
        "python",
        "programação",
        "desenvolvimento",
        "computador",
        "inteligência artificial",
        "tecnologia",
        "algoritmo",
        "software",
    ]

    # gerar palavra aleatória da lista de palavras
    gerar_palavra = random.choice(palavras)
    palavra_secreta = gerar_palavra.lower()

    # definindo _ para cada letra da palavra secreta
    letras_descobertas = ["_" for _ in palavra_secreta]

    # definindo o número de tentativas restantes
    tentativas_restantes = 6
    letras_tentadas = []

    # loop
    while tentativas_restantes > 0 and "_" in letras_descobertas:
        print("\nPalavra: " + " ".join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")

        # entrada do usuário
        palpite = input("Digite uma letra: ").lower().strip()
        print("-" * 40)

        # validando a entrada do usuário
        if len(palpite) != 1 or not palpite.isalpha():
            print("❌ Entrada inválida! Digite apenas UMA letra.")
            continue

        if palpite in letras_tentadas:
            print(f"❌ Você já tentou essa letra {palpite}. Tente outra.")
            continue

        # adicionando a letra tentada à lista de letras tentadas
        letras_tentadas.append(palpite)

        # verificando se a letra está na palavra secreta
        if palpite in palavra_secreta:
            print(f"✅ Boa! A letra '{palpite}' está na palavra.")

            # atualizando as letras descobertas com a letra correta
            for indice, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_descobertas[indice] = palpite
        else:
            print(f"❌ A letra '{palpite}' não está na palavra.")
            tentativas_restantes -= 1

            print()  # linha em branco para separar a saída do jogo

    # fim do jogo
    if "_" not in letras_descobertas:
        print("==========")
        print(f"🎉 Parabéns! Você acertou a palavra {palavra_secreta} e salvou o boneco!")
        print("==========")
    else:
        print("==========")
        print("💀 Você perdeu! O boneco foi enforcado!")
        print(f"A palavra era: {palavra_secreta}")
        print("==========")


# executando o jogo
if __name__ == "__main__":
    jogar_forca()