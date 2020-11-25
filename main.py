palavra_secreta = 'palavra'
chave = [ '_' for i in range(len(palavra_secreta))] # cria uma lista de tracos

def run():
    c = 1

    while (1):
        if (c > 2):
            print('[*]\tFinalizando...')
            break
        chute = input('[*]\tDigite uma LETRA: ')

        for letra in range(len(palavra_secreta)):
            if (chute == palavra_secreta[letra]):
                chave[letra] = palavra_secreta[letra]

        painel = ' '.join(chave) # transforma a list em str e substitui ',' por ' '
        print(f'[*]\t{painel}')
        c+=1
        

def main():
    run()

if(__name__ == '__main__'):
    main()