# EXERCÍCIO FINAL***********************************************************************************
# Gerenciamento de jogadores e times
# Escreva um programa em Python que realize o gerenciamento de jogadores
'''
Requisito 1: A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores
do time.

Requisito 2: A opção de adicionar um time deve pedir um nome para o time que será cadastrado

Requisito 3: A opção de remover um time deve pedir o índice específico do time que foi cadastrado
para fazer a sua exclusão.

Requisito 4: A opção de adicionar um jogador em um time, deve pedir um índice do time que foi
cadastrado e associar com o nome do jogador que será adicionado.

Requisito 5: A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado
e utilizar esse índice para remover o jogador que fora cadastrado no time.

Requisito 6: A opção de listar os jogadores de um time deve ser informado o índice de um time e listar
os jogadores que foram associados a ele
'''
import pprint

times = {
      'Corinthians': ['Cássio', 'Fagner', 'Gil', 'Veríssimo', 'Fábio Santos'],
      'Palmeiras': ['Weverton', 'Mayke', 'Gómez', 'Murilo', 'Piquerez'],
      'São Paulo': ['Rafael', 'Rafinha', 'Arboleda', 'Beraldo', 'Caio Paulista'],
      'Santos': ['João Bosco', 'João Lucas', 'Messias', 'Bauermann', 'Lucas Pires']
      }

pp = pprint.PrettyPrinter(depth=4)
opcoes = 0

while opcoes != 7:
      print('')
      print('#################### Seja bem vindo ao "Soccer Fut 2023" | Escolha entre as opções de 1 à 7 ####################')
      opcoes = int(input('''1. ListarTimes | 2. AddTime | 3. RemoveTime | 4. AddJogador | 5. RemoveJogador | 6. ListarJogadores | 7. SAIR: '''))
      print('')
      
      if opcoes == 1:
            for chave, valor in times.items():
                  qtdJogadores = len(valor)
                  print(f'• {chave}: {valor} "{qtdJogadores}" jogadores.')

      elif opcoes == 2:
            novoTime = input('Qual time deseja adicionar? ')
            times[novoTime] = []
            pp.pprint(times.keys())

      elif opcoes == 3:
            removeTime = input('Qual time deseja remover? ')
            times.pop(removeTime)
            pp.pprint(times.keys())

      elif opcoes == 4:
            novoJogador = input('Qual o nome do jogador que deseja add? ')
            qualTime = input(f'Em qual time deseja add o "{novoJogador}"? ')
            
            if qualTime in times:
                  times[qualTime].append(novoJogador)
                  print(times[qualTime])
      
      elif opcoes == 5:
            qualTime = input('O jogador que deseja remover perterce a qual time? ')
            pp.pprint(times[qualTime])
            print('')
            removeJogador = input(f'Qual jogador deseja remover do {qualTime}? ')
            
            if qualTime in times:
                  times[qualTime].remove(removeJogador)
                  pp.pprint(times[qualTime])

      elif opcoes == 6:
            print(times.keys())
            qualTime = input('Deseja listar os jogadores de qual time acima? ')
            pp.pprint(times[qualTime])

      elif opcoes == 7:
            opcoes = 7
        
      else:
            print('OPÇÃO INVÁLIDA: escolha as opções de 1 à 7')