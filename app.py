#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


# Path: Dockerfile
#-----------------------------------------------------------------------------------------
import random

def escolha_do_computador():
    return random.choice(['pedra', 'papel', 'tesoura'])

def decidir_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

def jogar_novamente():
    resposta = input("Quer jogar novamente? (s/n): ").lower()
    return resposta == "s"

def main():
    while True:
        escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
        if escolha_jogador not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida. Tente novamente.")
            continue

        escolha_pc = escolha_do_computador()
        print(f"O computador escolheu: {escolha_pc}")
        resultado = decidir_vencedor(escolha_jogador, escolha_pc)
        print(resultado)

        if not jogar_novamente():
            break

if __name__ == "__main__":
    main()
