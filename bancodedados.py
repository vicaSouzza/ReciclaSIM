

## banco de dados
def bancoDadosInformacoes():
    return  [
        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': 
            '\n\n\nCaracteristica: Extremamente fáceis de moldar, podem tomar as mais diversas formas. ' +
            'O plástico pode ser rígido ou flexível, transparente ou opaco, resistente à humidade ou ' +
            'solúvel em água - as possibilidades são praticamente infinitas.', 
            'tipo': 'plastico' },

        { 'id': 2, 'descricao': 'Tipos de material', 
            'obs': 
            '\n\n\n------------------- Aqui estão alguns dos materiais que podem ser reutilizados:',
            'tipo': 'plastico' },

        { 'id': 3, 'descricao': 'Formas de reutilizar e utilizar', 
            'obs': 'Aqui vai a Forma de reutilizar', 
            'tipo': 'plastico' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': 'Aqui vai a Composição', 
            'tipo': 'plastico' },

        { 'id': 5, 'descricao': 'Cuidados', 
            'obs': 
            '\n\n\n',
            'tipo': 'plastico' },

        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': 'caract do metal', 
            'tipo': 'metal' },

        { 'id': 2, 'descricao': 'Tipos de material', 
            'obs': ''
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:',
            'tipo': 'metal' },

        { 'id': 3, 'descricao': 'Formas de reutilizar e utilizar', 
            'obs': 'metal', 
            'tipo': 'metal' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '', 
            'tipo': 'metal' },

        { 'id': 5, 'descricao': 'Cuidados', 
            'obs': 
            '\n\n\n',
            'tipo': 'metal' },    
        
        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': '', 
            'tipo': 'vidro' },

        { 'id': 2, 'descricao': 'Tipos de material', 
            'obs': ''
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:',
            'tipo': 'vidro' },

        { 'id': 3, 'descricao': 'Formas de reutilizar e utilizar', 
            'obs': 'vidro', 
            'tipo': 'vidro' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '', 
            'tipo': 'vidro' },
        
        { 'id': 5, 'descricao': 'Cuidados', 
            'obs': 
            '\n\n\n',
            'tipo': 'vidro' },
        
        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': '', 
            'tipo': 'papel' },

        { 'id': 2, 'descricao': 'Tipos de material', 
            'obs': 
            '\n\n\n------------------- Aqui estão alguns dos objetos que podem ser reutilizados:', 
            'tipo': 'papel' },

        { 'id': 3, 'descricao': 'Formas de reutilizar e utilizar', 
            'obs': 'papel', 
            'tipo': 'papel' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '', 
            'tipo': 'papel' },

        { 'id': 5, 'descricao': 'Cuidados', 
            'obs': 
            '\n\n\n',
            'tipo': 'papel' },

        { 'id': 1, 'descricao': 'Caracteristica', 
            'obs': '\n\nÉ considerado lixo eletrônico todo resíduo material oriundo do descarte de equipamentos eletrônicos.', 
            'tipo': 'eletronico' },

        { 'id': 2, 'descricao': 'Tipos de material', 
            'obs':
            '\n\n\n------------------- Aqui estão alguns dos materiais que podem ser reciclados:' 
            '\n\n\nMonitores de computador, telefones celulares e baterias, computadores, carregadores, fones de ouvido, ' +  
            'televisores, câmeras fotográficas, impressoras, tablets, mouses, teclados, radios e aparelho de som,' +
            'batedeiras, liquidificadores, ferros elétricos, furadeiras, secadores de cabelo, ' +
            'aspiradores de pó, cafeteiras, eletrodomésticos de grande porte como, geladeira, fogão, '+
            'maquina de lavar roupa e louça etc.',
            'tipo': 'eletronico' },

        { 'id': 3, 'descricao': 'Formas de reutilizar e utilizar', 
            'obs': '', 
            'tipo': 'eletronico' },

        { 'id': 4, 'descricao': 'Composiçao', 
            'obs': '\n\nO lixo eletrônico é produzido por materiais de origem inorgânica, como por exemplo:' + 
            'cobre, alumínio, metais pesados (mercúrio, cádmio, berílio e chumbo)', 
            'tipo': 'eletronico' },

        { 'id': 5, 'descricao': 'Cuidados', 
            'obs':'\n\n\nOs materiais eletrônicos são formados por, componentes de plástico, metal e placas de componentes '+
            'eletrônicos que ainda podem ser usados. Esses componentes podem conter mais de 60 '+
            'substâncias tóxicas e nocivas ao meio ambiente e as pessoas. Por isso não devem ser '+
            'descartados junto com outros materiais reciclaveis. Mantenha os materiais eletrônicos longe '+
            'de fatores que possam danificá-los, como calor e excesso de umidade, evitando assim vazamentos químicos e outros danos ao meio ambiente. '+
            'E nunca desmonte esses equipamentos sem conhecimento.', 
            'tipo': 'eletronico' },

    ]

## banco de dados com pontos de coleta da cidade
def bancoDadosPontoColeta():
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
