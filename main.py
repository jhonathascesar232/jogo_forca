from os import path, listdir
from os.path import isfile, join


#numero de chaces
def numeroNivel():
    """
    Retorna o numero de tentativas de acordo com o nivel
    """
    t = 0

    print('[*]\t1 - Fácil(5 tentativas)')
    print('[*]\t2 - Médio(3 tentativas)')
    print('[*]\t3 - Difícil(2 tentativas)')
    n = input('[*]\tEscolha o nivel:')

    if(n == '1'):
        t = 5
        print(f'[*]\t  Tentativas Totais\t{t}')
        return t
    elif(n == '2'):
        t = 3
        print(f'[*]\t  Tentativas Totais\t{t}')
        return t
    elif(n == '3'):
        t = 2
        print(f'[*]\t  Tentativas Totais\t{t}')
        return t
    else:
        print('[*]\t  Opcão inválida!')
        numeroNivel()
    

#ler a entra do usuario e verifica as letras
def lerLetra(chave, c):
    """
    param:chave
    param:c

    retorna a entrada do usuário, tentativas
    """
    while 1:
        chute = input('[*]\tDigite uma LETRA: ').lower()

        #verifica se a letra ja tem na chave
        if (chute not in chave):
            if (chute not in palavra_secreta): #verifica se a letra ja tem na palavra secreta
                c -= 1
                print(f'[*]\t Letra não encontrada! ({chute})')
            break

        print('[*]\tLetra ja foi dita!')
        print('[*]\tTente novamente!')
    
    return chute, c

#ler a palavra secreta
def lerArquivo():
    """
    Ler o arquivo e retorna a palavra!
    """
    #print(__file__) #str do aquivo py
    pasta = path.abspath(path.dirname(__file__)) #str do diretorio
    arquivo = pasta + "/PALAVRA_SECRETA_AKI.txt"
    #abre o arquivo
    with open(arquivo ,'r') as f:
        palavra = f.read().lower() #ler e converte para str
        palavra = palavra.replace('\n', "") #substitui '\n' -> ''
    return palavra

#verifica se o arquivo de texto ja tem se nao cria um va\io
def verificaArquivo():
    """
    Verifica se o arquivo de texto existe na pasta
    """
    pasta = path.abspath(path.dirname(__file__))#retorna o caminho da propria pasta
    p = 'PALAVRA_SECRETA_AKI.txt'
    
    files = [f for f in listdir(pasta) if isfile(join(pasta, f))] #retorna uma lista so de ficheiros
    if p not in files:
        with open(p, 'w') as f:
            pass

#fim
def fimJogo():
    print('[*]\n[*]\n[*]\tVoçê PERDEU!!!\n[*]')
    print('[*]\tFIM[*]\n[*]')

#loop do jogo
def run(tentativasRestantes, tentativas, chave):
    """
    Loop do pequeno jogo
    """

    while (1):
        #verifica se o player perdeu
        if (tentativasRestantes < tentativas):
            fimJogo()
            break
        #verifica se o player ganhou
        if (palavra_secreta == ''):
            print('[*]\tInsira uma PALAVRA SECRETA!')
            break
        if (''.join(chave) == palavra_secreta):
            print('[*]\n[*]\tVocê acertou a palavra secreta!')
            print(f'[*]\tPALAVRA: {palavra_secreta}')
            break
        
        print(f'[*]\n[*]\t  Tentativa restantes: {tentativasRestantes}')
        chute, tentativasRestantes = lerLetra(chave, tentativasRestantes)

        for letra in range(len(palavra_secreta)):
            if (chute == palavra_secreta[letra]):
                chave[letra] = palavra_secreta[letra]

        painel = ' '.join(chave) # transforma a list em str e substitui ',' por ' '
        print(f'[*]\n[*]\t{painel}\n[*]')

        
#funcao principal
def main():
    global palavra_secreta

    palavra_secreta = lerArquivo()
    chave = ['_' for i in range(len(palavra_secreta))]
    print('CHAVE',chave)

    tentativas = 1
    tentativasRestantes = numeroNivel()
    verificaArquivo()
    run(tentativasRestantes, tentativas, chave)

if(__name__ == '__main__'):
    main()

