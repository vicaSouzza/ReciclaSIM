## Importação de bibliotecas
import os
from math import radians, cos, sin, asin, sqrt

## Constantes
VOLTAR = 'VOLTAR'
SIM = 'SIM'
SAIR = 'SAIR'
ENCERRAR = 6

## Exibe o menu principal  e solicita ao usuário a escolha de uma das opções
def exibeMenuInicial():
  
    print(
    r'''                                                                                                                                                                           
    
     ___        _    _      ___ ___ __  __ 
    | _ \___ __(_)__| |__ _/ __|_ _|  \/  |
    |   / -_) _| / _| / _` \__ \| || |\/| |
    |_|_\___\__|_\__|_\__,_|___/___|_|  |_|
                                            
                                                                
    ''') 
    print('''\nO objetivo deste programa é facilitar o processo de reciclagem auxiliando na identificação do material reciclável e depois na localização de um ponto de coleta. VAMOS COMEÇAR? 
    É muito facil, siga minhas instruções.
            
            [1] - Plástico
            [2] - Metal
            [3] - Vidro
            [4] - Papel
            [5] - Eletrônicos
            [6] - Encerrar o programa''')

def exibeMenuFim():
   print(
        '''
            Encerrando...
            Obrigado por utilizar a nossa solução!

            Desenvolvido por:
                - VITÓRIA SOUZA
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

## Converte uma opção de menu (1, 2, 3, etc.) para um tipo específico (papel, vidro, etc.)
def convertOpcaoByTipo(opcao):
    if opcao == 1:
        return 'plastico'
    elif opcao == 2:
        return 'metal'
    elif opcao == 3:
        return 'vidro'
    elif opcao == 4:
        return 'papel'
    elif opcao == 5:
        return 'eletronico'
    else:
        return ''

## Retorna os pontos de coleta a partir de uma categoria (plástico, vidro, papel...)
def getPontosDeColetaByCategoria(categoria):
    pontosDeColeta = []

    for ponto in getPontosDeColeta():
        for categoriaPonto in ponto['categorias']:
            if categoriaPonto == categoria:
                pontosDeColeta.append(ponto)

    return pontosDeColeta

## Retorna um array/vetor contendo as opções de informações sobre o material escolhido (plástico, vidro, etc.)
def getInfoByTipo(opcao):
    informacoes = []
    tipo = convertOpcaoByTipo(opcao)
    for info in getInfo():
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
        limpaConsole()

        print('Exibindo as opções de informações sobre o material escolhido...\n')

        for info in informacoes:
            print('[{id}] - {nome}'.format(id = info['id'], nome = info['descricao']))

        print('\nSe quiser voltar para o menu inicial, digite a palavra VOLTAR ;)')
       

        opcaoEscolhida = input('\nO que deseja saber sobre o ' + str(info['tipo']) +', digite um numero: ')

        # ## Converte para inteiro (int) caso o usuário tenha digitado somente números
        opcaoEscolhida = int(opcaoEscolhida) if opcaoEscolhida.isnumeric() else str(opcaoEscolhida)

        if opcoesDisponiveis.count(opcaoEscolhida):
            opcaoValida = True
            infoEscolhida = getInfoById(informacoes, opcaoEscolhida)
        elif str(opcaoEscolhida).upper() == VOLTAR:
            ## Volta para o menu inicial
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

        limpaConsole()

        
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
                    
                    limpaConsole()

                    if pontosDeColetaMaisProximos[0]['distancia'] <= distMax:
                        print('Os pontos mais próximos são esses: \n')
                        
                        for ponto in pontosDeColetaMaisProximos :
                            print('Distância: ', format(ponto['distancia'], '.2f'), ' Km\nNome: ', ponto['nome'], '\nEndereco: ', ponto['endereco'], '\n')
                    else:
                        print(f'Que pena!! não foi encontrado nenhum ponto de coleta no raio de {distMax:.2f} km. O local mais próximo encontra-se logo abaixo: ')
                        print('\nDistância: ', format(pontosDeColetaMaisProximos[0]['distancia'], '.2f'), ' Km\nNome: ', pontosDeColetaMaisProximos[0]['nome'], '\nEndereco: ', pontosDeColetaMaisProximos[0]['endereco'], '\n')

                    input('\nPressione qualquer tecla para voltar ao menu inicial!\n')
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
    limpaConsole()
    print('Ops... Tente mais uma vez ')
    print(str(msg))
    print('\nPressione qualquer tecla para voltar')
    input()
    
## Limpa o console
def limpaConsole():
    os.system('clear') ## windows
    os.system('cls') ## Executa o comando 'cls' no console no linux

## Retorna um array/vetor contendo todas as informarções que podem ser coletadas do material escolhido
def getInfo():
    return  [
        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': 
            '\n\n\nCaracteristica: Extremamente fáceis de moldar, podem tomar as mais diversas formas. ' +
            'O plástico pode ser rígido ou flexível, transparente ou opaco, resistente à humidade ou ' +
            'solúvel em água - as possibilidades são praticamente infinitas.', 
            'tipo': 'plastico' },

        { 'id': 2, 'descricao': 'Objetos para reutilizar', 
            'obs': 
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:',
            'tipo': 'plastico' },

        { 'id': 3, 'descricao': 'Forma de reutilizar', 
            'obs': 'Aqui vai a Forma de reutilizar', 
            'tipo': 'plastico' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': 'Aqui vai a Composição', 
            'tipo': 'plastico' },

        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': 'caract do metal', 
            'tipo': 'metal' },

        { 'id': 2, 'descricao': 'Objetos para reutilizar', 
            'obs': ''
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:',
            'tipo': 'metal' },

        { 'id': 3, 'descricao': 'Forma de reutilizar', 
            'obs': 'metal', 
            'tipo': 'metal' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '', 
            'tipo': 'metal' },
        
        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': '', 
            'tipo': 'vidro' },

        { 'id': 2, 'descricao': 'Objetos para reutilizar', 
            'obs': ''
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:',
            'tipo': 'vidro' },

        { 'id': 3, 'descricao': 'Forma de reutilizar', 
            'obs': 'vidro', 
            'tipo': 'vidro' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '', 
            'tipo': 'vidro' },
        
        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': '', 
            'tipo': 'papel' },

        { 'id': 2, 'descricao': 'Objetos para reutilizar', 
            'obs': 
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:', 
            'tipo': 'papel' },

        { 'id': 3, 'descricao': 'Forma de reutilizar', 
            'obs': 'papel', 
            'tipo': 'papel' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '', 
            'tipo': 'papel' },

        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': '\n\nÉ considerado lixo eletrônico todo resíduo material oriundo do descarte de equipamentos eletrônicos.', 
            'tipo': 'eletronico' },

        { 'id': 2, 'descricao': 'Objetos para reutilizar', 
            'obs':
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:' 
            '\n\n\nMonitores de computador, telefones celulares e baterias, computadores, carregadores, fones de ouvido, ' +  
            'televisores, câmeras fotográficas, impressoras, tablets, mouses, teclados, radios e aparelho de som,' +
            'eletrodomésticos de grande porte como, geladeira, ' +
            'fogão, maquina de lavar roupa e louça etc.',
            'tipo': 'eletronico' },

        { 'id': 3, 'descricao': 'Forma de reutilizar', 
            'obs': '', 
            'tipo': 'eletronico' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '\n\nO lixo eletrônico é produzido por materiais de origem inorgânica, como por exemplo:' + 
            'cobre, alumínio, metais pesados (mercúrio, cádmio, berílio e chumbo)', 
            'tipo': 'eletronico' },

    ]

## Retorna um array/vetor contendo os pontos de coleta disponíveis em Campinas/SP
def getPontosDeColeta():
    return [
        { 'id': 1, 'nome': 'Ecoponto - Parque Itajaí', 'endereco': 'R. Celso Soares Couto, S/N - Conj. Hab. Parque Itajaí, Campinas - SP', 'latitude': -22.96143, 'longitude': -47.18951, 'categorias': ['plastico', 'papel', 'vidro', 'metal'] },
        { 'id': 2, 'nome': 'Ponto Verde - Vila Costa e Silva', 'endereco': 'R. Saldanha da Gama, 77 - Vila Costa e Silva, Campinas - SP, 13081-000', 'latitude': -22.856155, 'longitude': -47.068549, 'categorias': ['plastico', 'papel', 'vidro', 'metal', 'eletronico'] },
        { 'id': 3, 'nome': 'Ecoponto - Jardim São Gabriel', 'endereco': 'R. José Martins Lourenço, 140-284 - Jardim São Gabriel, Campinas - SP, 13054-310', 'latitude': -22.94198, 'longitude': -47.02982, 'categorias': ['papel', 'metal', 'vidro', 'plastico'] },
        { 'id': 4, 'nome': 'Ecoponto - Jardim Pacaembu', 'endereco': 'R. Dante Suriani, 2-382 - Chácara Cneo, Campinas - SP, 13033-160', 'latitude': -22.904529, 'longitude': -47.105434, 'categorias': ['plastico', 'papel', 'vidro', 'metal'] },
        { 'id': 5, 'nome': 'Ecoponto - Jardim Paranapanema', 'endereco': 'R. Serra dÁgua, 326 - Jardim São Fernando, Campinas - SP, 13100-370', 'latitude': -22.91570, 'longitude': -47.03747, 'categorias': ['plastico', 'papel', 'vidro', 'metal']},
        { 'id': 6, 'nome': 'Ecoponto -  Vila Campos Sales', 'endereco': 'Av. São José dos Campos, S/N - Vila Campos Sales, Campinas - SP, 13040-565', 'latitude': -22.94837, 'longitude': -47.05779, 'categorias': ['papel', 'plastico', 'vidro', 'metal', 'eletronico']},
        { 'id': 7, 'nome': 'Ecoponto - Parque São Jorge', 'endereco': 'R. Plácida Pretini, 196-270 - Parque São Jorge, Campinas - SP, 13064-812', 'latitude': -22.89579, 'longitude': -47.15631, 'categorias': ['papel', 'plastico', 'vidro', 'metal']},
        { 'id': 8, 'nome': 'HT Papéis Barão - Coleta e reciclagem de resíduos', 'endereco': 'Av. Ruy Rodrigues, 394 - Jardim Novo Campos Eliseos, Campinas - SP, 13060-192', 'latitude': -22.934023, 'longitude': -47.105661, 'categorias': ['plastico', 'papel'] },
        { 'id': 9, 'nome': 'Ecoponto -  Vila União', 'endereco': 'R. Manoel Gomes Ferreira, 42 - Parque Tropical, Campinas - SP, 13060-523', 'latitude': -22.936016, 'longitude': -47.118061, 'categorias': ['papel', 'plastico', 'vidro', 'metal'] },
        { 'id': 10, 'nome': 'Ecoponto / Ponto Verde', 'endereco': 'Av. Santa Isabel, 2300 - Barão Geraldo, Campinas - SP, 13084-012', 'latitude': -22.817244, 'longitude': -47.100531, 'categorias': ['papel', 'plastico', 'vidro', 'metal'] },
        { 'id': 11, 'nome': 'GMV Recycle', 'endereco': 'Rod. Lix da Cunha, 911 - Jardim Nova America, Campinas - SP, 13070-715', 'latitude': -22.898166, 'longitude': -47.093476, 'categorias': ['papel', 'eletronico'] },
        { 'id': 12, 'nome': 'Ecoponto -  Jardim Eulina',  'endereco': 'Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP', 'latitude': -22.891751, 'longitude': -47.100940, 'categorias': ['papel', 'vidro', 'plastico', 'metal'] },
        { 'id': 13, 'nome': 'Reversis - Reciclagem de Eletrônicos e Informática',  'endereco': 'R. da Abolição, 1900 - Pte. Preta, Campinas - SP, 13041-445', 'latitude': -22.926823, 'longitude': -47.042984, 'categorias': ['eletronico'] },
        { 'id': 14, 'nome': 'Ponto Verde - Carlos Grimaldi', 'endereco': 'R. Cōnego Pedro Bonhomme, 2424 - Jardim Bela Vista, Campinas - SP, 13077-003', 'latitude': -22.87611, 'longitude': -47.03918, 'categorias': ['papel', 'vidro', 'plastico', 'metal']},
        { 'id': 15, 'nome': 'Cooperativa de Recicláveis Santa Genebra',  'endereco': 'R. Estácio de Sá, 577 - Jardim Santa Genebra, Campinas - SP, 13084-751', 'latitude': -22.852778, 'longitude': -47.074819, 'categorias': ['papel', 'vidro', 'plastico', 'metal'] }
    ]


