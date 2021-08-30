# -*- coding: utf-8 -*-

'''
Esse problema pode ser simplesmente resolvido com arvore geradora mínima.
Nesse caso, usei o algoritimo de kruskal, de complexidade de tempo M*log( N ),
onde M é o número de arestas e N o de vértices.
'''

def read_entradas( ):
    
    while True:
        
        m , n = map( int , input().split() )
        if m == 0 and m == n:
            break
        
        V = set( list ( range ( m ) ) )
        E = dict( )
        for i in range( n ):
            x , y , z = map( int , input().split() )
            E[ ( x , y ) ] = z
        
        yield V , E


#--------------------------------------------------
# Essas 4 funções abaixo são para implementação de flo-
# resta de conjuntos disjuntos. Elas são explicadas
# no capitulo X do Livro do Cormen. Resolvi não usar
# classes, pois essa é uma estrutura de dados facilmente
# implementada por dicionários python

def make_set( F , x ):
    F[ x ] = x

def get_set( F , x ):
    
    y = x
    while F[ y ] != y:
        y = F[ y ]
    return y

def link_sets( F , x , y ):
    
    x = get_set( F , x )
    y = get_set( F , y )
    F[ y ] = x

def flat_set( F , x ):
    
    '''
        Antes do flat_set:
        x      = [ 0 , 1 , 2 , 3 , 4 ]
        F[ x ] = [ 3 , 2 , 2 , 4 , 1 ]

        0 -> 3 -> 4 -> 1 -> 2

        Após o flat_set:
        x      = [ 0 , 1 , 2 , 3 , 4 ]
        F[ x ] = [ 2 , 2 , 2 , 2 , 2 ]
        
        0 -\
            \
        1 -> 2
            /|
        3 -/ |
             |
        4----|

        flat set é fundamental para diminuir
        o tempo de execução de get_set
    '''

    seq = []
    while x != F[ x ]:
        seq.append( x )
        x = F[ x ]
    
    pivot = F[ x ]
    for x in seq:
        F[ x ] = pivot

#--------------------------------------------------

def kruskal( V , E ):
    
    F = {}
    for u in V:
        make_set( F , u )
    
    edges_list = list( E.keys() )
    edges_list.sort( key = lambda x : E[ x ] )
    
    A = dict( )
    for u , v in edges_list:
        
        S1 = get_set( F , u )
        S2 = get_set( F , v )
        if S1 == S2:
            continue
        
        A[ ( u , v ) ] = E[ ( u , v ) ]
        link_sets( F , u , v )
        flat_set( F , u )
        
    return A
    
def main():
    
     for V , E in read_entradas():
         
         soma_1 = 0
         for tup in E:
             soma_1 += E[ tup ]
        
         A = kruskal( V , E )
         soma_2 = 0
         for tup in A:
             soma_2 += A[ tup ]
         print( soma_1 - soma_2 )

if __name__ == "__main__":
    main()
