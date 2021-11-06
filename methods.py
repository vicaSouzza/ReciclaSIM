## Importação de bibliotecas
import os
from math import radians, cos, sin, asin, sqrt

from bancodedados import bancoDadosInformacoes, bancoDadosPontoColeta



## Constantes
VOLTAR = 'VOLTAR'
SIM = 'SIM'
SAIR = 'SAIR'
ENCERRAR = 6
ERROR = 'Opcao invalida'
ERRORDIG = 'Digite alguma coisa'


## Exibe o menu principal  e solicita ao usuário a escolha de uma das opções
def exibeMenuInicial():
  
    print(
    r'''                                                                                                                                                                           
    
     ___        _    _      ___ ___ __  __ 
    | _ \___ __(_)__| |__ _/ __|_ _|  \/  |
    |   / -_) _| / _| / _` \__ \| || |\/| |
    |_|_\___\__|_\__|_\__,_|___/___|_|  |_|
                                     
                                                                
    ''') 
    print('''\n\n\n *** Recicle seu material, identifique as características e encontre um Ponto de Coleta mais proximo do endereço desejado ***\n\n
           
            [1] - Plástico
            [2] - Metal
            [3] - Vidro
            [4] - Papel
            [5] - Eletrônicos
            [6] - Encerrar o programa
            ''')

def exibeMenuFim():
   print(
        '''
            Fim...
            Obrigado por usar o ReclicaSIM!

            Desenvolvido por:
                - 
        ''')
    
## Obtem um array/vetor com o número das opções disponíveis
def getOpcoesMenuInicial():
    return [ 1, 2, 3, 4, 5, 6]

## Obtem um array/vetor contendo o número das opções disponíveis da lista de informações
def getOpcoesByInformacoes(info):
    opcoesDisponiveis = []

    for informacoes in info:
        opcoesDisponiveis.append(informacoes['id'])

    return opcoesDisponiveis

def opt(case):
    if case == 1:
        return 'plastico'
    if case == 2:
        return 'metal'
    if case == 3:
        return 'vidro'
    if case == 4:
        return 'papel'
    if case == 5:
        return 'eletronico'
    else:
        return ''

## Retorna os pontos de coleta a partir de uma categoria (plástico, vidro, papel...)
def getPontosDeColetaByCategoria(categoria):
    pontosDeColeta = []

    for ponto in bancoDadosPontoColeta():
        for categoriaPonto in ponto['categorias']:
            if categoriaPonto == categoria:
                pontosDeColeta.append(ponto)

    return pontosDeColeta

## Retorna um array/vetor contendo as opções de informações sobre o material escolhido (plástico, vidro, etc.)
def getInfoByTipo(opcao):
    informacoes = []
    tipo = opt(opcao)
    for info in bancoDadosInformacoes():
        if info['tipo'] == tipo:
            informacoes.append(info)

    return informacoes

## Retorna uma informação 
def getInfoById(informacoes, id):
    for informacoes in informacoes:
        if informacoes['id'] == id:
            return informacoes

## Retorna o ponto de coleta mais próximo (se baseia na latitude e longitude do usuário)
def getPontosDeColetaMaisProximo(pontosDeColeta, latitude, longitude, distMax):
    pontoMaisProximo = pontosDeColeta[0]
    pontos = []

    pontoMaisProximo['distancia'] = 0

    for ponto in pontosDeColeta:
        lon1 = longitude
        lat1 = latitude
        lon2 = ponto['longitude']
        lat2 = ponto['latitude']
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # Calcule a distância (em várias unidades) entre dois pontos na Terra usando sua latitude e longitude.
        #fonte:  https://www.ti-enxame.com/pt/python/como-posso-estimar-rapidamente-distancia-entre-dois-pontos-latitude-e-longitude/1072488907/
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
        distancia = c*r
        distancia = round(distancia)
        ponto['distancia'] = distancia
        
        

        if (ponto['distancia'] < distMax):
            pontos.append(ponto)
        
        if ponto['distancia'] < pontoMaisProximo['distancia']:
            pontoMaisProximo = ponto

    ## Caso não exista nenhum ponto de coleta dentro do raio de distância, retorne o mais próximo
    if len(pontos) == 0:
        pontos.append(pontoMaisProximo)

    return pontos

## Exibe o banco de informações a partir de uma opção escolhida (plástico, vidro, etc.)
def exibeInfoByopcao(numeroinfo):
    ## Variáveis
    informacoes = getInfoByTipo(numeroinfo)
    opcoesDisponiveis = getOpcoesByInformacoes(informacoes)
    opcaoEscolhida = 0
    opcaoValida = False
    InfoEscolhido = {}

    ## Solicita ao usuário qual informação ele gostaria de saber 
    while not(opcaoValida):
        cleanConsole()

        print('Exibindo as opções de informações sobre o material escolhido...\n')

        for info in informacoes:
            print('[{id}] - {nome}'.format(id = info['id'], nome = info['descricao']))

        print('\nSe quiser voltar para o menu inicial, digite a palavra VOLTAR')
       

        opcaoEscolhida = input('\nO que deseja saber sobre o ' + str(info['tipo']) +', digite um numero: ')

        
        # ## Converte para inteiro (int) caso o usuário tenha digitado somente números
        opcaoEscolhida = int(opcaoEscolhida) if opcaoEscolhida.isnumeric() else str(opcaoEscolhida)

        if opcoesDisponiveis.count(opcaoEscolhida):
            opcaoValida = True
            infoEscolhida = getInfoById(informacoes, opcaoEscolhida)
        elif str(opcaoEscolhida).upper() == VOLTAR:
            ## Volta para o menu inicial
         cleanConsole()
         exibeMenuInicial()
         return True
        else:
            opcaoValida = False
            exibeMensagemErro('Tente novamente.')
    
    ## Reseta variável 'opcaoValida'
    opcaoValida = False

    ## Exibe a informação e solicita a latitude e longitude do usuário
    while not(opcaoValida):
        ## Variáveis
        latitude = ''
        longitude = ''
        pontosDeColetaDisponiveis = getPontosDeColetaByCategoria(infoEscolhida['tipo'])
        pontosDeColetaMaisProximos = {}

        cleanConsole()

        
        exibeInfo(infoEscolhida)
    
        print('\n-------------------------------------------------------- VAMOS CONTINUAR? ----------------------------------------------------------------------\n')
        print('\nOpcoes:\n')
        print('\nSe deseja descobrir qual o ponto de coleta mais próximo. Digite: SIM.  \nSe deseja voltar ao menu anterior. Digite: VOLTAR. \nSe deseja encerrar. Digite: SAIR.  \n\n')
        opcao_escolha = input('\nDigite sua escolha: ')

      
        if SIM == opcao_escolha:
            latitude = str(input('Digite a sua latitude: '))
            longitude = str(input('Digite a sua longitude: '))

            distMax = digiteDistancia()

            if len(latitude) > 0 and len(longitude):
                try:
                    latitude = float(latitude)
                    longitude = float(longitude)
                    distMax = float(distMax)

                    opcaoValida = True
                
                    pontosDeColetaMaisProximos = getPontosDeColetaMaisProximo(pontosDeColetaDisponiveis, latitude, longitude, distMax)
                    
                    cleanConsole()

                    if pontosDeColetaMaisProximos[0]['distancia'] <= distMax:
                        print('Os pontos mais próximos são esses: \n')
                        
                        for ponto in pontosDeColetaMaisProximos :
                            print('Distância: ', format(ponto['distancia'], '.2f'), ' Km\nNome: ', ponto['nome'], '\nEndereco: ', ponto['endereco'], '\n')
                    else:
                        print(f'Que pena!! não foi encontrado nenhum ponto de coleta no raio de {distMax:.2f} km. O local mais próximo encontra-se logo abaixo: ')
                        print('\nDistância: ', format(pontosDeColetaMaisProximos[0]['distancia'], '.2f'), ' Km\nNome: ', pontosDeColetaMaisProximos[0]['nome'], '\nEndereco: ', pontosDeColetaMaisProximos[0]['endereco'], '\n')

                    input('\nPressione qualquer tecla para voltar!\n')
                except:
                    opcaoValida = False
                    exibeMensagemErro(' Informe os dados corretamente.')
            else:
                opcaoValida = False
                exibeMensagemErro(' Informe os dados corretamente.')
        if VOLTAR == opcao_escolha:
            exibeInfoByopcao(numeroinfo)
            return False
        if SAIR == opcao_escolha:
            exibeMenuFim()
            return False
        
    ## Retorna True, assim redireciona o usário para o menu inicial da aplicação
    return True

## Exibe a informação escolhida
def exibeInfo(info):
    print('''------------------------------------------------- Informações sobre o material ----------------------------------------------------------------- ''' + str(info['obs']))

## Solicita ao usuário a distância máxima que ele está disposto a percorrer
def digiteDistancia():
    return input('Qual a distância máxima em KM você deseja percorrer até ponto de coleta: ')

## Exibe uma mensagem de erro 
def exibeMensagemErro(msg):
    cleanConsole()
    print('Ops... Tente mais uma vez ')
    print(str(msg))
    print('\nPressione qualquer tecla para voltar')
    input()
    
## Limpa o console
def cleanConsole():
    os.system('clear') ## windows
    os.system('cls') ## Executa o comando 'cls' no console no linux



## Funçao main
if __name__ == "__main__" :

    inicio = True
    opcao = 0
    
  
    while inicio:

        cleanConsole()
        exibeMenuInicial()

        opcao = input('\n Para opcao desejada, digite um numero do menu: ')
        ## Conversão para inteiro
        opcao = int(opcao) if opcao.isnumeric() else str(opcao)

        if getOpcoesMenuInicial().count(opcao) > 0:
            inicio = False
            if opcao != ENCERRAR: 
                inicio = exibeInfoByopcao(opcao)
            else: 
                cleanConsole()
                exibeMenuFim()
        else: 
            erroMsg = ERROR if len(str(opcao)) > 0 else ERRORDIG
            exibeMensagemErro(erroMsg)
