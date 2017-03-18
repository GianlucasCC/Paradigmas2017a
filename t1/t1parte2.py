#Exercicio 1
list(map(lambda nomes: 'Sr.' + nomes,["Gianlucas","Juvenal","Irineu","Fulano"]))

#Exercicio 2
list(map(lambda n: 3*n*2 + 2/n + 1,[1,2,3]))

#Exercicio 3
list(filter(lambda lista: lista[-1] in 'a',["Ciclana","Arara","Computador"]))

#Exercicio 4
list(filter(lambda idade: 2017 - idade > 1970, [20,30,51,57]))

#Exercicio 5
list(map(lambda numbers: numbers * 2,[1,2,3,4]))


