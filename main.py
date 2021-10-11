## Importando arquivo funções (functions.py)
from myMethods import exibeInfoByopcao, limpaConsole, exibeMenuInicial, getOpcoesMenuInicial, exibeMensagemErro, exibeMenuFim

if __name__ == "__main__":
    ## Constantes
    OPCAO_ENCERRAR_PROGRAMA = 6

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

            if opcaoEscolhida != OPCAO_ENCERRAR_PROGRAMA:
                menuInicial = exibeInfoByopcao(opcaoEscolhida)
            else:
                limpaConsole()
                exibeMenuFim()    
        else:
            textoErro = 'Opção inexistente.' if len(str(opcaoEscolhida)) > 0 else 'Digite alguma coisa.'
            exibeMensagemErro(textoErro + '. Tente novamente.')
