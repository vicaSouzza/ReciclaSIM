## Importando arquivo myMethodos
from methods import exibeInfoByopcao, limpaConsole, exibeMenuInicial, getOpcoesMenuInicial, exibeMensagemErro, exibeMenuFim

if __name__ == "__main__":
    
    ENCERRAR = 6

    ## Variáveis
    menuInicial = True
    opcaoEscolhida = 0

    while menuInicial:
        ## Limpa o console
        limpaConsole()

        exibeMenuInicial()

        opcaoEscolhida = input('\nDigite o número da opção desejada: ')

        ## Converte para inteiro (int) caso o usuário tenha digitado somente números
        opcaoEscolhida = int(opcaoEscolhida) if opcaoEscolhida.isnumeric() else str(opcaoEscolhida)

        if getOpcoesMenuInicial().count(opcaoEscolhida) > 0:
            menuInicial = False

            if opcaoEscolhida != ENCERRAR:
                menuInicial = exibeInfoByopcao(opcaoEscolhida)
            else:
                limpaConsole()
                exibeMenuFim()    
        else:
            textoErro = 'Não temos essa opção.' if len(str(opcaoEscolhida)) > 0 else 'Digite alguma coisa.'
            exibeMensagemErro(textoErro)

