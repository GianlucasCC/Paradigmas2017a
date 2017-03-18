#Exercicio 1
def somaQuad(x,y): return pow(x,2) + pow(y,2)
    #somaQuad(1,2)

#Execicio 2
def hasEqHeads(l1,l2): return l1[0] == l2[0]
    #hasEqHeads([1,2,3],[1,5,7])

#Exercicio 3
def sr(nomes): return "Sr." + nomes
    #list(map(sr,["Gianlucas","Micol","Portuga"]))

#Exercicio4
#Fiz desse jeito também, mas não sei se pode, então fiz de outro para garantir (:p).
def espaco(string): return string.count(" ")
    #espaco("ola mundo não sei o que escrever mais")

def espaco2(string): return string == " "
    #len(list(filter(espaco2,"ola mundo não sei o que escrever mais")))

#Execicio 5
def calc(n): return 3*n*2 + 2/n + 1
    #list(map(calc,[1,2,3]))

#Exercicio 6
def negativo(n): return n < 0
    #list(filter(negativo,[-1,2,-3,5,-8]))

#Exercicio 7
def intervalo(n): return n >= 1 and n <= 100
    #list(filter(intervalo,[1,2,3,500,100,20]))

#Exercicio 8
def pares(n): return n % 2 == 0
    #list(filter(pares,[1,2,3,4,5,6]))

#Exercicio 9
def charFound(c,s): return s.count(c) >= 1
    #charFound('c','Gianlucas')

#Exercicio 10
def marcador(html): return "<B>" + html + "</B>"
    #list(map(marcador,["olá","mundo","python","t1Parte1","não","sei"]))
