# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: João Nogueira Roxo da Fonseca, johnroxo@hotmail.com
# - aluno B: Gabriela Choichit Giosa, gabichoichit@gmail.com
#essa linha eh apenas um teste
import random 

{
    "saguao insper": {
        "titulo": "Saguao do perigo",
        "descricao": "Voce esta no saguao de entrada do insper",
        "opcoes": {
            "andar professor": "Tomar o elevador para o andar do professor",
            "biblioteca": "Ir para a biblioteca",
            "4 andar": "dar uma passada no 4 andar"
        }
    },
    "carona": {
        "titulo": "Caroninha do seu Jurandir",
        "descricao": "seu Jurandir vai te dar carona com uma condicao, tirar o monstro de dentro da Kombi dele",
        "opcoes":{
            "lutar" : "Voce precisa derrotar o montro para chegar em SP"                
        }
    },
    "onibus": {
        "titulo": "Busao para SP",
        "descricao" : "Voce pegou um onibos para Sp, porem apareceu um monstro no seu Busao.",
        "opcoes":{
            "lutar" : "tentar lutar contra o monstrengo(voce so tem essa opcao.)."
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
            "carona": "Pegar carona com seu Jurandir e sua kombi."
        }
    },
    "lutar": {
        "titulo": "luta",
        "descricao": "voce saiu na porrada com o monstro",
        "opcoes": {
            "saguao insper" : " Ir para entrada do Insper.",
            "predio 2": "Tentar fazer o EP com seus amigos"
        }
    } ,
    "4 andar":{
        "titulo": "4 andar",
        "descricao":"Voce subiu no quarto andar para ver como estao as coisas por la",
        "opcoes":{
            "jogar":"jogar um pouco para descontrair",
            "Sala 405": "Dar um alhada na sala para ver se tem algo que pode te ajudar com o EP",
            "andar professor": "ir para o andar do professor",
            "saguao insper" : "voltar para o saguo do insper"
        }
    },
 
    "jogar":{
        "titulo": "Nada como um bom descanso",
        "decricao":"Voce descansou bastante e obviamente perdeu o tempo do Ep",
        "opcoes":{}
    },
    "Sala 405":{
        "titulo": "Ambiente medonho",
        "descricao": "A sala esta apagada, voce procura algo que pode te ajudar com o EP e acha uma estranha passagem secreta, mas nada e tao facil, voce encontra um monstro que protege a passagem",
        "opcoes":{
            "Lutar": "Lutar com o monstro para ver o que tem atras dele.",
            "fugir": "Sair correndo da sala"
        }
    } ,
    "fugir":{
        "titulo": "fuga",
        "descricao":"voce fugiu da sala",
        "opcoes":{
            "jogar":"jogar um pouco para descontrair",
            "andar professor": "ir para o andar do professor",
            "saguao insper" : "voltar para o saguo do insper"}
        },
    "Lutar":{
        "titulo":"luta",
        "descricao": "Voce manda o monstro vir pra cima",
        "opcoes":{
            "andar professor": "ir para o andar do professor",
            "saguao insper" : "voltar para o saguo do insper"
        }
    },                        
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
        "descricao":  "O monstro do python so poder ser detido de duas maneiras:com a gema do ep feito, ou uma batalha final",                        
        "opcoes": {
           
        }
 
    },
    "biblioteca": {
        "titulo": "Caverna da tranquilidade",
        "descricao": "Voce esta na biblioteca",
        "opcoes": {
            "saguao insper": "Voltar para o saguao de entrada"
        }
    }
}


def main():
    nome_cenario_atual = "casa"
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("Falta 1 dia para entrega do EP!Para sua sorte enquanto estava arrumando suas mala"
         "encontrou uma gema da vida(ganha +100 de vida) em um bau antigo  no seu armario. Você está "
        "na sua casa, e precisa decidir como vai para Sao Paulo (gema da vida ja esta em seu inventario, que faz voce ter 200 de vida todo começo de luta). "
        )
    print()
    carregar_cenarios = ()
    cenarios, nome_cenario_atual = carregar_cenarios()
    gema_EP = False
    game_over = False
    inventario = ["gemaDaVida"]
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]       
        print(cenario_atual['titulo'])
        print(len(cenario_atual['titulo'])*'-')
        print(cenario_atual['descricao'])
        opcoes = cenario_atual['opcoes']
        monstro = 100
        jogador = 100
        gemaDaVida = 100
        if 'gemaDaVida' in inventario:
            jogador += gemaDaVida
#EP feito
        if nome_cenario_atual == 'professor' and gema_EP == True:
             print('parabens, por conta da gema da EP, foi criado um EP perfeito e voce entregou no praso para o professor !!!')                 
             break        
#combate Busao
        if nome_cenario_atual == 'lutar':
            print("E sua primeira batalha, mostre o porque merece adiamento do EP!")
            print("Voce tem ", jogador, " de vida")
            while jogador > 0 and monstro > 0:
                B = random.randint(1,3)
                ataque_player = 20
                if B <= 2:
                    monstro -= ataque_player
                else:
                    jogador -= 10

                 
            if jogador <=0:
                print("Você morreu!")
            else:
                print("Voce ganhou, parabens!!Sua vida agora é igual a:")
                print(jogador)
                print("Após a luta mais acirrada da sua vida, você derrotou o monstro, parabens!!")
                print('Apos vencer o montro voce chega tranquilamente em SP')
                y = random.randint(1,100)
                if y <= 30:
                    if "gemaDeTeleporte" not in inventario:
                        inventario.append("gemaDeTeleporte")
                elif y > 30 and y < 75:
                    if "gemaDeAtaque" not in inventario:
                        inventario.append("gemaDeAtaque")
                elif y > 75 and y <= 99:
                    print("Porem não ganhou nada, siga a sua jornada!")
                else:
                    if "gema de EP feita" not in inventario:
                        inventario.append("gema de EP feita")
                        gema_EP = True
                        print("Parabens!! Voce ganhou a gema de EP concluida, ela torna a sua EP feita e perfeita!Va até o professor e faça a entrega") 
                print("Este é o seu inventario após a batalha:")
                print(inventario)
                
         
#Demais combates
        gemaDeAtaque = 20
        if 'gemaDeAtaque' in inventario:
             ataque_player += gemaDeAtaque
        if nome_cenario_atual == 'Lutar':
             print("Voce tem ", jogador, " de vida")
             print("E o monstro tem 100 de vida")
             while jogador > 0 and monstro > 0:
                B = random.randint(1,3)
                ataque_player = 20
                if B <= 2:
                    monstro -= ataque_player

                else:
                    jogador -= 10
                                                  
             if jogador <=0:
                 print("Você morreu!")
                 print("A vida do monstro foi de:", monstro)
             else:
                 print("Voce ganhou, parabens!!Sua vida agora é igual a:")
                 print(jogador)
                 print("Após a luta mais acirrada da sua vida, você derrotou o monstro, parabens!!")          
                 print("Voce percebeu que ele n escondia so uma passagem e sim um teletransporte")
                 print("Agora voce precisa escolher entre 3 salas, podendo ganhar itens bons ou ter uma surpresa inesperada")
                 print("E claro, para se teletransportar voce precisa ter a gema de teleporte no seu inventario.")
                 
                 if 'gemaDeTeleporte' in inventario:
                     sala_secreta = input('qual sala deseja ir(sala 1,sala 2 ou sala 3)??')
                     if sala_secreta == "sala 1": 
                         print("Que sorte..., voce ganhou um bonus de vida(+50) por entrar nessa sala.")
                         jogador += 50
                         print("Agora voce tem" , jogador, "de vida")
                     elif sala_secreta == "sala 2": 
                         print("Que sorte..., voce ganhou uma gema de ataque(+20) por entrar nessa sala.")
                         if "gemaDeAtaque" not in inventario:
                             inventario.append("gemaDeAtaque")
                     else:
                         print("Que pena.., voce perdeu 30 de vida por entrar nessa sala.")
                         jogador -= 30
                         print("Agora voce tem" , jogador, "de vida")
                 else:
                     print("infelizmente voce nao possui a gema de teleporte e seu inventario")
# Batalha final
        if nome_cenario_atual == "professor":
            professor = 500
            print("Você acaba de chegar a luta final, esta será sua última chance de fazer a EP")
            print("Voce tem ", jogador, " de vida e seu professor tem 500, Boa sorte!")
            while jogador > 0 and professor > 0:
                B = random.randint(1,3)
                ataque_player = 20
                if B <= 2:
                    professor -= ataque_player
                else:
                    jogador -= 25

                                                  
            if jogador <=0:
                 print("A batalha final acabou, e infelizmente você morreu")
                 print("A vida final do professor foi de ", professor, " pontos")
            else:
                 print("Voce ganhou, parabens!!Sua vida agora é igual a:")
                 print(jogador)
                 print("Você derrotou o professor e não precisou entregar a sua EP")
                 break
                 
            
            
        
            
                 
        
           
       
                        
                        
      

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
                
                
                
         
    
        
           
    if "gema de EP feita" in inventario and professor <= 0:
        print("parabens, voce ganhou gracas a gema da ep feita!!!")
    else:
        print("Você perdeu!")


# Programa principal.
if __name__ == "__main__":
    main()
