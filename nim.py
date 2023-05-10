
def usuario_escolhe_jogada(n,m):
    a = int(input('quantas pessas deseja retirar?'))
   
    if a > m or a <0:
        print('não é permitido esse número')
        a = int(input('quantas pessas deseja retirar?'))
    
    else:
        print('voce tirou',a,'peças')
    return a


def computador_escolhe_jogada(n,m):
    p=1
    a=0
    while m>=p:
        
        if ((n-p)%(m+1)) == 0:
            a=p
        p=p+1
    if a ==0:
        if p>n:
            return n
        if p<n: 
            return p   
        print('o pc tirou',p,'pessas do tabuleiro')
        print(a)
    else:
        print('o pc tirou',a,'pessas do tabuleiro')
        return a 

    


def partida():
    def jogada(k,n,m):
        
        while n >=0:
            if k == 0 and n>0:
                a =  usuario_escolhe_jogada(n,m)
                n = n - a
                print('sobrou',n,'pessas no tabuleiro') 
                if n>0:
                    k =1
                else:
                    print('voce venceu')
                    return
            if k ==1 and n>0:
                j = computador_escolhe_jogada(n,m)
                n = n-j
                print('sobrou',n,'pessas no tabuleiro') 
                if n>0:
                    k =0
                else:
                    print('O pc venceu')
                    return
    
        if n==0:
            print('o Jogo acabou')
    inicio = False
    if inicio == False:
        n = int(input('Quantas peças? '))
        m = int(input('Limite de pessas por Jogada? '))
        inicio = True
    
    if (n%(m+1)) == 0 and inicio == True:
        print('Você começa')
        jogada(0,n,m)
     
    if (n%(m+1)) != 0 and inicio == True:
        print('O PC começa')
        jogada(1,n,m)
    return

def start():
    a = input('Escolha o Modo que você quer Partida(P) Campeonato(C): ')
    if a == "P":
        partida()
    if a == "C":
        partida()
        partida()
        partida()
start()