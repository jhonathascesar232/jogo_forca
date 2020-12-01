palavra_secreta = 'palavra'
chave = [ '_' for i in range(len(palavra_secreta))] # cria uma lista de tracos

#numero de chaces
def numeroNivel():
    t = 0

    print('[*]\t1 - Fácil(5 tentativas)')
    print('[*]\t2 - Médio(3 tentativas)')
    print('[*]\t3 - Difícil(2 tentativas)')
    n = input('[*]\tEscolha o nivel:')

    if(n == '1'):
        t = 5
        print(f'[*] Tentativas Totais\t{t}')
        return t
    elif(n == '2'):
        t = 3
        print(f'[*] Tentativas Totais\t{t}')
        return t
    elif(n == '3'):
        t = 2
        print(f'[*] Tentativas Totais\t{t}')
        return t
    else:
        print('[*]\tOpcão inválida!')
        numeroNivel()
    

#ler a entra do usuario e verifica as letras
def lerLetra(chave, c):
    while 1:
        chute = input('[*]\tDigite uma LETRA: ').lower()

        #verifica se a letra ja tem na chave
        if (chute not in chave):
            if (chute not in palavra_secreta):#verifica se a letra ja tem na palavra secreta
                c -= 1
                print(f'[*]\t Letra não encontrada! ({chute})')
            break

        print('[*]\tLetra ja foi dita!')
        print('[*]\tTente novamente!')
            

    return chute, c

#ler a palavra secreta
def lerArquivo():
    from os import path
    
    print(__file__) #str do aquivo py
    arquivo = path.abspath(path.dirname(__file__)) + "/PALAVRA_SECRETA_AKI.txt" #str do diretorio
    with open(arquivo ,'r') as f:
        palavra = f.read()
        print(palavra)

    return palavra

#loop do jogo
def run():
    tentativas = 1
    tentativasRestantes = numeroNivel()

    while (1):
        #verifica se o player perdeu
        if (tentativasRestantes < tentativas):
            print('\n[*]\tVocê perdeu!')
            print('[*]\tFinalizando...')
            break
        #verifica se o player ganhou
        if (''.join(chave) == palavra_secreta):
            print('[*]\n[*]\tVocê acertou a palavra secreta!')
            print(f'[*]\tPALAVRA: {palavra_secreta}')
            break
        
        print(f'[*]\n[*]\tTentativa restantes: {tentativasRestantes}')
        chute, tentativasRestantes = lerLetra(chave, tentativasRestantes)

        for letra in range(len(palavra_secreta)):
            if (chute == palavra_secreta[letra]):
                chave[letra] = palavra_secreta[letra]

        painel = ' '.join(chave) # transforma a list em str e substitui ',' por ' '
        print(f'[*]\n[*]\t{painel}\n[*]')
        
        
#funcao principal
def main():
    lerArquivo()

if(__name__ == '__main__'):
    main()