# projeto2

#2.1.1 - TAD interseção

def cria_intersecao(col, lin):
    '''
    cria_intersecao: str x int → intersecao

    cria_intersecao(col,lin) recebe um caracter e um inteiro correspondentes à coluna (col) e à 
    linha (lin) e devolve a interseção correspondente. O construtor verifica a validade dos seus 
    argumentos, gerando um ValueError com a mensagem 'cria_intersecao: argumentos invalidos' caso 
    os seus argumentos não sejam válidos.
    '''
    inter=(col, lin)
    if not eh_intersecao(inter):
        raise ValueError('cria_intersecao: argumentos invalidos')
    return inter

def obtem_col(i):
    '''
    obtem_col: intersecao → str

    obtem_col(i) devolve a coluna col da interseção i.
    '''
    return i[0]

def obtem_lin(i): 
    '''
    obtem_lin: intersecao → int

    obtem_lin(i) devolve a linha lin da interseção i.
    '''
    return i[1]

def eh_intersecao(arg, arg2=0): 
    '''
    eh_intersecao: universal → booleano

    eh_intersecao(arg) devolve True caso o seu argumento seja um TAD intersecao e False caso contrário.
    '''
    if type(arg)!=tuple:
        return False
    if len(arg)!=2:
        return False
    if type(obtem_col(arg))!=str or len(obtem_col(arg))!=1 or ord(obtem_col(arg))<65 or ord(obtem_col(arg))>83:
        return False
    if type(obtem_lin(arg))!=int or obtem_lin(arg)<1 or obtem_lin(arg)>19:
        return False
    return True

def intersecoes_iguais(i1, i2): 
    '''
    intersecoes_iguais: universal x universal → booleano

    intersecoes_iguais(i1, i2) devolve True apenas se i1 e i2 são interseções e são iguais, e False caso contrário.
    '''
    if not eh_intersecao(i1) or not eh_intersecao(i2):
        return False
    if obtem_col(i1)!=obtem_col(i2):
        return False
    if obtem_lin(i1)!=obtem_lin(i2):
        return False
    return True

def intersecao_para_str(i):
    '''
    intersecao_para_str: intersecao → str

    intersecao_para_str(i) devolve a cadeia de caracteres que representa o seu argumento.
    '''
    return obtem_col(i)+str(obtem_lin(i))

def str_para_intersecao(s):
    '''
    str_para_intersecao: str → intersecao

    str_para_intersecao(s) devolve a interseção representada pelo seu argumento.
    '''
    if type(s)!=str or len(s)<2:
        return False
    return cria_intersecao(s[0], int(s[1:]))

def obtem_intersecoes_adjacentes(i, l):
    '''
    obtem_intersecoes_adjacentes: territorio x intersecao → tuplo

    obtem_intersecoes_adjacentes(i, l) devolve um tuplo com as interseções adjacentes à interseção i 
    de acordo com a ordem de leitura em que l corresponde à interseção superior direita do tabuleiro de Go.
    '''
    inter_adj=()
    col_i=obtem_col(i)
    lin_i=obtem_lin(i)
    col_l=obtem_col(l)
    lin_l=obtem_lin(l)
    if 'A'<=col_i<=col_l and 1<=lin_i-1<=lin_l:
        inter_adj+=(cria_intersecao((col_i),(lin_i-1)),)             #adiciona a interseção de baixo
    if 'A'<=chr(ord(col_i)-1)<=col_l and 1<=lin_i<=lin_l:
        inter_adj+=(cria_intersecao((chr(ord(col_i)-1)),(lin_i)),)    #adiciona a interseção da esquerda
    if 'A'<=chr(ord(col_i)+1)<=col_l and 1<=lin_i<=lin_l:
        inter_adj+=(cria_intersecao((chr(ord(col_i)+1)),(lin_i)),)    #adiciona a interseção da direita
    if 'A'<=col_i<=col_l and 1<=lin_i+1<=lin_l:
        inter_adj+=(cria_intersecao((col_i),(lin_i+1)),)             #adiciona a interseção de cima
    return (inter_adj)

def ordena_intersecoes(t): 
    '''
    ordena_intersecoes: tuplo → tuplo

    ordena intersecoes(t) devolve um tuplo de interseções com as mesmas interseções de t ordenadas 
    de acordo com a ordem de leitura do tabuleiro de Go.
    '''
    return tuple(sorted(t, key=lambda x: (obtem_lin(x),obtem_col(x))))  #ordena primeiro o numero e depois a letra


#2.1.2 - TAD pedra

def cria_pedra_branca():
    '''
    cria_pedra_branca: {} → pedra

    cria_pedra_branca() devolve uma pedra pertencente ao jogador branco.
    '''
    return 'O'

def cria_pedra_preta():
    '''
    cria_pedra_preta: {} → pedra

    cria_pedra_preta() devolve uma pedra pertencente ao jogador preto.
    '''
    return 'X'

def cria_pedra_neutra():
    '''
    cria_pedra_neutra: {} → pedra

    cria_pedra_neutra() devolve uma pedra neutra.
    '''
    return '.'

def eh_pedra(arg):
    '''
    eh_pedra: universal → booleano

    eh_pedra(arg) devolve True caso o seu argumento seja um TAD pedra e False caso contrário.
    '''
    return arg in (cria_pedra_branca(), cria_pedra_neutra(), cria_pedra_preta())

def eh_pedra_branca(p):
    '''
    eh_pedra_branca: pedra → booleano
    eh_pedra_branca(p) devolve True caso a pedra p seja do jogador branco e False caso contrário.
    '''
    return p==cria_pedra_branca()

def eh_pedra_preta(p):
    '''
    eh_pedra_preta: pedra → booleano
    eh_pedra_preta(p) devolve True caso a pedra p seja do jogador preto e False caso contrário.
    '''
    return p==cria_pedra_preta()

def pedras_iguais(p1, p2):
    '''
    pedras_iguais:universal x universal → booleano
    pedras_iguais(p1, p2) devolve True apenas se p1 e p2 são pedras e são iguais.
    '''
    return eh_pedra(p1) and eh_pedra(p2) and p1==p2

def pedra_para_str(p):
    '''
    pedra_para_str: pedra → str

    pedra_para_str(p) devolve a cadeia de caracteres que representa o jogador dono da pedra, isto é, 
    cria_pedra_branca(), cria_pedra_preta() ou cria_pedra_neutra() para pedras do jogador branco, preto ou neutra respetivamente.
    '''
    if eh_pedra_branca(p):
        return cria_pedra_branca()
    if eh_pedra_preta(p):
        return cria_pedra_preta()
    if not eh_pedra_jogador(p):
        return cria_pedra_neutra()

def eh_pedra_jogador(p):
    '''
    eh_pedra_jogador: pedra → booleano 

    eh_pedra_jogador(p) devolve True caso a pedra p seja de um jogador e False caso contrário.
    '''
    return eh_pedra_branca(p) or eh_pedra_preta(p)


#2.1.3 - TAD goban

def cria_goban_vazio(n):
    '''
    cria_goban_vazio: int → goban

    cria_goban_vazio(n) devolve um goban de tamanho n x n, sem interseções ocupadas. O construtor verifica a 
    validade do argumento, gerando um ValueError com a mensagem 'cria_goban_vazio: argumento invalido' caso os 
    seu argumento não seja válido. Considere que um goban pode ser de dimensão 9 x 9, 13 x 13 ou 19 x 19.
    '''
    if (n!=9 and n!=13 and n!=19) or type(n)!=int:
        raise ValueError('cria_goban_vazio: argumento invalido')
    return list(list(cria_pedra_neutra() for _ in range(n)) for _ in range(n))    #cria uma lista com n listas com n pedras neutras

def cria_goban(n, ib, ip):
    '''
    cria_goban: int x tuplo x tuplo → goban

    cria_goban(n, ib, ip) devolve um goban de tamanho n x n, com as interseções do tuplo ib ocupadas por pedras 
    brancas e as interseções do tuplo ip ocupadas por pedras pretas. O construtor verifica a validade dos 
    argumentos, gerando um ValueError com a mensagem 'cria_goban: argumentos invalidos' caso os seus argumentos 
    não sejam válidos. Considere que um goban pode ser de dimensão 9 x 9, 13 x 13 ou 19 x 19.
    '''
    if (n!=9 and n!=13 and n!=19) or type(n)!=int or type(ib)!=tuple or type(ip)!=tuple:
        raise ValueError('cria_goban: argumentos invalidos')
    goban=cria_goban_vazio(n)
    inter=()
    for i in ib:
        if not eh_intersecao_valida(goban, i) or i in inter:       # (i in inter) testa a repetição das interseções
            raise ValueError('cria_goban: argumentos invalidos')
        inter+=(i,)
        coloca_pedra(goban, i, cria_pedra_branca())
    for i in ip:
        if not eh_intersecao_valida(goban, i) or i in inter:
            raise ValueError('cria_goban: argumentos invalidos')
        inter+=(i,)
        coloca_pedra(goban, i, cria_pedra_preta())
    return goban

def cria_copia_goban(g):
    '''
    cria_copia_goban: goban → goban
    
    cria_copia_goban(g) recebe um goban e devolve uma cópia do goban.
    '''
    g_copia=[]
    for i in g:
        sub_lista=[]
        for j in i:
            sub_lista+=[j,]
        g_copia+=[sub_lista,]
    return g_copia

def obtem_ultima_intersecao(g):
    '''
    obtem_ultima_intersecao: goban → intersecao
    
    obtem_ultima_intersecao(g) devolve a interseção que corresponde ao canto superior direito do goban g.
    '''
    return cria_intersecao(chr(len(g)+64), len(g))

def obtem_pedra(g, i):
    '''
    obtem_pedra: goban x intersecao → pedra

    obtem_pedra(g, i) devolve a pedra na interseção i do goban g. Se a posição não estiver ocupada, devolve 
    uma pedra neutra.
    '''
    num_col=ord(obtem_col(i))-65
    num_lin=obtem_lin(i)-1
    return g[num_col][num_lin]

def obtem_cadeia(g, i):
    '''
    obtem_cadeia: goban x intersecao → tuplo

    obtem_cadeia(g, i) devolve o tuplo formado pelas interseções (em ordem de leitura) das pedras da mesma 
    cor que formam a cadeia que passa pela interseção i. Se a posição não estiver ocupada, devolve a 
    cadeia de interseções livres.
    '''
    cadeia=(i,)
    k=0
    if eh_pedra_branca(obtem_pedra(g, i)):
        while k<len(cadeia):
            tuplo_inter_adj=obtem_intersecoes_adjacentes(cadeia[k], obtem_ultima_intersecao(g))
            for j in tuplo_inter_adj:
                if j not in cadeia and eh_pedra_branca(obtem_pedra(g, j)):
                    cadeia+=(j,)
            k+=1
    elif eh_pedra_preta(obtem_pedra(g, i)):
        while k<len(cadeia):
            tuplo_inter_adj=obtem_intersecoes_adjacentes(cadeia[k], obtem_ultima_intersecao(g))
            for j in tuplo_inter_adj:
                if j not in cadeia and eh_pedra_preta(obtem_pedra(g, j)):
                    cadeia+=(j,)
            k+=1
    elif not eh_pedra_jogador(obtem_pedra(g, i)):
        while k<len(cadeia):
            tuplo_inter_adj=obtem_intersecoes_adjacentes(cadeia[k], obtem_ultima_intersecao(g))
            for j in tuplo_inter_adj:
                if j not in cadeia and not eh_pedra_jogador(obtem_pedra(g, j)):
                    cadeia+=(j,)
            k+=1
    return ordena_intersecoes(cadeia)

def coloca_pedra(g, i, p):
    '''
    coloca_pedra: goban x intersecao x pedra → goban

    coloca_pedra(g, i, p) modifica destrutivamente o goban g colocando a pedra do jogador p na interseção i, 
    e devolve o próprio goban.
    '''
    if eh_pedra_branca(p):
        num_col=ord(obtem_col(i))-65
        num_lin=obtem_lin(i)-1
        g[num_col][num_lin]=cria_pedra_branca()
    if eh_pedra_preta(p):
        num_col=ord(obtem_col(i))-65
        num_lin=obtem_lin(i)-1
        g[num_col][num_lin]=cria_pedra_preta()
    return g

def remove_pedra(g, i): 
    '''
    remove_pedra: goban x intersecao → goban

    remove_pedra(g, i) modifica destrutivamente o goban g removendo a pedra da interseção i, e devolve 
    o próprio goban.
    '''
    num_col=ord(obtem_col(i))-65
    num_lin=obtem_lin(i)-1
    g[num_col][num_lin]=cria_pedra_neutra()
    return g

def remove_cadeia(g, t): 
    '''
    remove_cadeia: goban x tuplo → goban

    remove_cadeia(g, t) modifica destrutivamente o goban g removendo as pedras nas interseções do tuplo t, 
    e devolve o próprio goban.
    '''
    for i in t:
        remove_pedra(g, i)
    return g

def eh_goban(arg): 
    '''
    eh_goban:universal → booleano

    eh_goban(arg) devolve True caso o seu argumento seja um TAD goban e False caso contrário.
    '''
    if type(arg)!=list or len(arg) not in (9, 13, 19):
        return False
    for i in arg:
        if type(i)!=list or len(i)!=len(arg):
            return False
        for j in i:
            if not eh_pedra(j):
                return False
    return True

def eh_intersecao_valida(g, i):
    '''
    eh_intersecao_valida: goban x intersecao → booleano

    eh_intersecao_valida(g, i) devolve True se i é uma interseção válida dentro do goban g e False caso contrário.
    '''
    if not eh_intersecao(i):
        return False
    ultima_i=obtem_ultima_intersecao(g)
    if 'A'<=obtem_col(i)<=obtem_col(ultima_i) and 1<=obtem_lin(i)<=obtem_lin(ultima_i):
        return True
    return False

def gobans_iguais(g1, g2):
    '''
    gobans_iguais: universal x universal → booleano

    gobans_iguais(g1, g2) devolve True apenas se g1 e g2 forem gobans e forem iguais.
    '''
    if not eh_goban(g1) or not eh_goban(g2):
        return False
    n1=obtem_lin(obtem_ultima_intersecao(g1))  #obtem o n do goban
    n2=obtem_lin(obtem_ultima_intersecao(g2))
    if n1!=n2:
        return False
    for i in range(n1):
        for j in range(n1):  
            inter=cria_intersecao(chr(i+65), j+1)
            if not pedras_iguais(obtem_pedra(g1, inter), obtem_pedra(g2, inter)):  #verifica se as pedras correspondentes à mesma interseção são iguais
                return False
    return True

def goban_para_str(g):
    '''
    goban_para_str: goban → str

    goban_para_str(g) devolve a cadeia de caracteres que representa o goban como mostrado nos exemplos.
    '''
    n=obtem_lin(obtem_ultima_intersecao(g))
    letras='  '
    numeros=''
    for i in range(n):
        letras+=' '+chr(65+i)              #cria a string com as letras todas
    for j in range(n):                     #cria a string com os numeros e pedras
        num=n-j
        if num>=10:
            numeros+=str(num)+' '
        else:
            numeros+=' '+str(num)+' '
        for i in range(n):                 #adiciona as pedras
            inter=cria_intersecao(chr(65+i), num)
            numeros+=obtem_pedra(g, inter)+' '
        if num>=10:
            numeros+=str(num)+'\n'
        else:
            numeros+=' '+str(num)+'\n'
    return letras+'\n'+numeros+letras

def obtem_territorios(g):
    '''
    obtem_territorios: goban → tuplo

    obtem_territorios(g) devolve o tuplo formado pelos tuplos com as interseções de cada território de g.
    A função devolve as interseções de cada território ordenadas em ordem de leitura do tabuleiro de Go, 
    e os territórios ordenados em ordem de leitura da primeira interseção do território.
    '''
    t=()
    conj_inter=()
    for i in range(obtem_lin(obtem_ultima_intersecao(g))):
        for j in range(obtem_lin(obtem_ultima_intersecao(g))):                    #passa por todos os elementos do goban
            inter=cria_intersecao(chr(i+65), j+1)
            if not eh_pedra_jogador(obtem_pedra(g, inter)) and inter not in conj_inter:  #se for pedra neutra e não está nas interseções adicionadas ou tuplo
                terr=obtem_cadeia(g, inter)
                conj_inter+=terr
                t+=(terr,)           #adiciona um tuplo com as interseçoes do territorio
    return tuple(sorted(t, key=lambda x:(obtem_lin(x[0]),obtem_col(x[0]))))         #ordena pela primeira interseção de cada territorio

def obtem_adjacentes_diferentes(g, t):
    '''
    obtem_adjacentes_diferentes: goban x tuplo → tuplo

    obtem_adjacentes_diferentes(g, t) devolve o tuplo ordenado formado pelas interseções adjacentes às interseções 
    do tuplo t:
    (a) livres, se as interseções do tuplo t estão ocupadas por pedras de jogador;
    (b) ocupadas por pedras de jogador, se as interseções do tuplo t estão livres.
    Notar que o primeiro caso corresponde às liberdades de uma cadeia de pedras, enquanto que o segundo corresponde
    à fronteira de um território.
    '''
    t_a_d=()
    for i in t:
        inter_adj=obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        if not eh_pedra_jogador(obtem_pedra(g, i)):                                 #para as interseções livres
            for j in inter_adj:
                if eh_pedra_jogador(obtem_pedra(g, j)) and j not in t_a_d:          #testa se a interseção adjacente é ocupada e se não está na lista
                    t_a_d+=(j,)
        if eh_pedra_jogador(obtem_pedra(g, i)):                                     #para as interseções ocupadas
            for j in inter_adj:
                if not eh_pedra_jogador(obtem_pedra(g, j)) and j not in t_a_d:      #testa se a interseção adjacente é livre e se não está na lista
                    t_a_d+=(j,)
    return ordena_intersecoes(t_a_d)

def jogada(g, i, p):
    '''
    jogada(): goban x intersecao x pedra → goban

    jogada(g, i, p) modifica destrutivamente o goban g colocando a pedra de jogador p na interseção i e remove 
    todas as pedras do jogador contrário pertencentes a cadeias adjacentes à i sem liberdades, devolvendo o 
    próprio goban.
    '''
    if eh_pedra_jogador(obtem_pedra(g, i)):  #testa se a pedra é de jogador, se não for retorna o proprio g
        return g
    g_copia=cria_copia_goban(g)
    coloca_pedra(g, i, p)
    tuplo_inter_adj=obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    tipos_pedras=()
    for j in (tuplo_inter_adj):
        tuplo_cadeia=obtem_cadeia(g, j)
        pedra=obtem_pedra(g, j)
        tipos_pedras+=(pedra,)
        if obtem_adjacentes_diferentes(g, tuplo_cadeia)==() and p!=pedra:   #testa se a cadeia das interseções adjacentes ficar sem liberdade
            return remove_cadeia(g, tuplo_cadeia)                           #se ficar sem liberdade a cadeia é removida
    if obtem_adjacentes_diferentes(g, (i,))==() and p not in tipos_pedras:
        g=g_copia
    return g

def obtem_pedras_jogadores(g):
    '''
    obtem_pedras_jogadores: goban → tuplo

    obtem_pedras_jogadores(g) devolve um tuplo de dois inteiros que correspondem ao número de interseções 
    ocupadas por pedras do jogador branco e preto, respetivamente.
    '''
    pedras_b=0
    pedras_p=0
    for i in range (obtem_lin(obtem_ultima_intersecao(g))):
        for j in range (obtem_lin(obtem_ultima_intersecao(g))):                 #passa por todos os elementos do goban
            inter=cria_intersecao(chr(i+65), j+1)
            pedra=obtem_pedra(g, inter)
            if eh_pedra_branca(pedra):      #se for a pedra for branca o numero de pedras brancas aumenta +1
                pedras_b+=1
            if eh_pedra_preta(pedra):       #se for a pedra for preta o numero de pedras pretas aumenta +1
                pedras_p+=1
    return (pedras_b, pedras_p)


#2.2 - Funções adicionais

def calcula_pontos(g):
    '''
    calcula_pontos: goban → tuple

    calcula_pontos(g) é uma função auxiliar que recebe um goban e devolve o tuplo de dois inteiros com as 
    pontuações dos jogadores branco e preto, respetivamente.
    '''
    pontos_b, pontos_p=obtem_pedras_jogadores(g)   #torna os pontos no numero de pedras de cada
    if pontos_b==pontos_p==0:
        return (pontos_b , pontos_p)
    terr=obtem_territorios(g)
    for i in range (len(terr)):
        tuplo_inter_adj=()
        for j in range (len(terr[i])):
            tuplo_inter_adj+=obtem_intersecoes_adjacentes(terr[i][j], obtem_ultima_intersecao(g)) #cria um tuplo com todas as interseções adjacentes ao territorio
        tuplo_inter_adj=tuple(map(lambda l: obtem_pedra(g, l), tuplo_inter_adj)) #transforma cada interseção na sua pedra correspondente
        if cria_pedra_preta() not in tuplo_inter_adj:  #testa se não há nenhuma pedra preta nas adjacentes do territorio
            pontos_b+=len(terr[i])  #se não houver adiciona o numero de interseções do territorio ao numero de pontos do branco
        if cria_pedra_branca() not in tuplo_inter_adj: #testa se não há nenhuma pedra branca nas adjacentes do territorio
            pontos_p+=len(terr[i])  #se não houver adiciona o numero de interseções do territorio ao numero de pontos do preto
    return (pontos_b , pontos_p)

def eh_jogada_legal(g, i, p, l):
    '''
    eh_jogada_legal: goban x intersecao x pedra x goban → booleano

    eh_jogada_legal(g, i, p, l) é uma função auxiliar que recebe um goban g, uma interseção i, uma pedra de 
    jogador p e um outro goban l e devolve True se a jogada for legal ou False caso contrário, sem modificar 
    g ou l. Para a deteção de repetição, considere que l representa o estado de tabuleiro que não pode ser 
    obtido após a resolução completa da jogada.
    '''
    if not eh_pedra_jogador(p) or not eh_goban(g) or not eh_goban(l) or not eh_intersecao_valida(g, i):
        return False
    g_copia=cria_copia_goban(g)
    g_jogada=jogada(g_copia, i, p)
    if eh_pedra_jogador(obtem_pedra(g, i)):
        return False
    if gobans_iguais(g_jogada, l):  #o g depois da jogada não pode ser igual a l
        return False
    if gobans_iguais(g_jogada, g):  #o g depois da jogada não pode ser igual ao g antes da jogada
        return False
    if obtem_adjacentes_diferentes(g_jogada, obtem_cadeia(g_jogada, i))==():  #a pedra colocada não pode ficar sem liberdade
        return False
    return True

def turno_jogador(g, p, l):
    '''
    turno_jogador: goban x pedra x goban → booleano

    turno_jogador(g, p, l) é uma função auxiliar que recebe um goban g, uma pedra de jogador p e um outro goban l, 
    e oferece ao jogador que joga com pedras p a opção de passar ou de colocar uma pedra própria numa interseção. 
    Se o jogador passar, a função devolve False sem modificar os argumentos. Caso contrário, a função devolve True 
    e modifica destrutivamente o tabuleiro g de acordo com a jogada realizada. A função deve apresentar a mensagem 
    do exemplo a seguir, repetindo a mensagem até que o jogador introduzir 'P' ou a representação externa de uma 
    interseção do tabuleiro de Go que corresponda a uma jogada legal. Considere que l representa o estado de 
    tabuleiro que não pode ser obtido após a resolução completa da jogada.
    '''
    impossivel=True
    tipo_pedra=pedra_para_str(p)
    while impossivel:  #enquanto não for introduzido 'P' ou uma interseção o ciclo continua
        try:
            atividade=input(f'Escreva uma intersecao ou \'P\' para passar [{tipo_pedra}]:')
        except(EOFError):
            continue
        if atividade=='P':
            return False
        try:
            inter=str_para_intersecao(atividade)
        except(ValueError):
            continue
        if eh_intersecao_valida(g, inter) and eh_jogada_legal(g, inter, p, l):
            impossivel=False
    jogada(g, inter, p)
    return True

def go(n, tb, tp):
    '''
    go: int x tuple x tuple → booleano
    
    go(n, tb, tp) é a função principal que permite jogar um jogo completo do Go de dois jogadores. A função recebe 
    um inteiro correspondente à dimensão do tabuleiro, e dois tuplos (potencialmente vazios) com a representação 
    externa das interseções ocupadas por pedras brancas (tb) e pretas (tp) inicialmente. O jogo termina quando os 
    dois jogadores passam a vez de jogar consecutivamente. A função devolve True se o jogador com pedras brancas 
    conseguir ganhar o jogo, ou False caso contrário. A função deve verificar a validade dos seus argumentos, 
    gerando um ValueError com a mensagem 'go: argumentos invalidos' caso os seus argumentos não sejam válidos.
    '''
    if n not in (9, 13, 19) or type(n)!=int or type(tb)!=tuple or type(tp)!=tuple:
        raise ValueError('go: argumentos invalidos')
    ib=()
    ip=()
    for i in tb:   #passa as interseções do tuplo de representação externa para tuplo
        try:
            inter=str_para_intersecao(i)
        except(ValueError):
            raise ValueError('go: argumentos invalidos')
        if not eh_intersecao_valida(cria_goban_vazio(n), inter) or inter in ib:
            raise ValueError('go: argumentos invalidos')
        ib+=(inter,)
    for i in tp:   #passa as interseções do tuplo de representação externa para tuplo
        try:
            inter=str_para_intersecao(i)
        except(ValueError):
            raise ValueError('go: argumentos invalidos')
        if not eh_intersecao_valida(cria_goban_vazio(n), inter) or inter in ib or inter in ip:
            raise ValueError('go: argumentos invalidos')
        ip+=(inter),
    g=cria_goban(n, ib, ip)
    pontos_b, pontos_p=calcula_pontos(g)
    turno_b=True  #define o turno branco como True para que caso na primeira jogada se o jogador preto passe, o jogo não termine
    print(f'Branco (O) tem {pontos_b} pontos\nPreto (X) tem {pontos_p} pontos\n{goban_para_str(g)}')
    while True:
        l=cria_copia_goban(g)
        turno_p=turno_jogador(g, cria_pedra_preta(), l)
        pontos_b, pontos_p=calcula_pontos(g)
        print(f'Branco (O) tem {pontos_b} pontos\nPreto (X) tem {pontos_p} pontos\n{goban_para_str(g)}')
        if not (turno_p or turno_b): #se ambos os jogadores passarem o ciclo acaba e o jogo também
            break
        l=cria_copia_goban(g)
        turno_b=turno_jogador(g, cria_pedra_branca(), l)
        pontos_b, pontos_p=calcula_pontos(g)
        print(f'Branco (O) tem {pontos_b} pontos\nPreto (X) tem {pontos_p} pontos\n{goban_para_str(g)}')
        if not (turno_p or turno_b): #se ambos os jogadores passarem o ciclo acaba e o jogo também
            break
    pontos_b, pontos_p=calcula_pontos(g)
    return pontos_b>=pontos_p

go(9, (), ())