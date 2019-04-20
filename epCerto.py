# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: João Nogueira Roxo da Fonseca, johnroxo@hotmail.com
# - aluno B: Gabriela Choichit Giosa, gabichoichit@gmail.com
#essa linha eh apenas um teste
import random 

inventario= ['gema da vida']
def carregar_cenarios():
    cenarios =  {
        "saguao insper": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "carona": {
            "titulo": "Caroninha do seu Jurandir",
            "descricao": "A kombi do seu Jurandir te deixou com sucesso na porta do Insper",
            "opcoes":{
                "saguao insper": "Entrar no insper.",
                "predio 2": "Ir para o predio 2 para tentar fazer o EP.",
            }
        },
        "onibus": {
            "titulo": "Busao para SP",
            "descricao" : "Voce pegou um onibos para Sp, porem apareceu um monstro no seu Busao.",
            "opcoes":{
                "lutar busao" : "tentar lutar contra o monstrengo(voce so tem essa opcao.).",
            }
        },
        "predio 2": {
            "titulo": "Voce foi para o predio 2.",
            "descricao" : "Voce nao conseguiu fazer o EP a tempo",
            "opcoes" : {}
        },
                        
        "charrete": {
            "titulo": "Simples mais eficiente",
            "descricao": "O cavalo ficou desidratado e desmaiou.",
            "opcoes": {
                "onibus": "Voltar para sua RP e pegar um onibus.",
                "carona": "Pegar carona com seu Jurandir e sua kombi.",
            }
        },
        "luta busao": {
            "titulo": "luta",
            "descricao": "voce saiu na porrada com o monstro",
            #luta(if ganha opcoes, perde game over)
            "opcoes": {
                "saguao insper" : " Ir para entrada do Insper.",
            }
        } ,                              
        "casa":{
            "titulo": "Cidade Raiz",
            "descricao": "Voce esta em Ribeirao Preto (Terra do cafe) em sua casa.",
            "opcoes":{
                "onibus": "Pegar um onibus direto para Sao Paulo",
                "charrete" : "Ir de charrete para Sao Paulo"
            }
        },
            
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "saguao insper": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "saguao insper": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "casa"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("Falta 1 dia para entrega do EP!Para sua sorte enquanto estava arrumando suas mala"
         "encontrou uma gema da vida em um bau antigo  no seu armario. Você está "
        "na sua casa, e precisa decidir como vai para Sao Paulo (gema da vida ja esta em seu inventario). "
        )
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual['titulo'])
        print(len(cenario_atual['titulo'])*'-')
        print(cenario_atual['descricao'])
        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Suas opcoes:")
            for x,y in opcoes.items():
                print ("{0}:{1}".format(x,y))
                escolha = input('qual sua opcao?')
                if escolha in opcoes:
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True
            
    
        
           

    print("Você perdeu!")



# Programa principal.
if __name__ == "__main__":
    main()
    




