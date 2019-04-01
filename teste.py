######################## 1 MONTANDO DATASET   ################################################  
#Caracteristicas
#e fofinho?
#Tem uma orelhinha pequena?
#Faz miau?

#Se SIM = 1 Evadido / Se NAO = -1 Nao Evadido
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

df = pd.read_csv("C://Users//vitcl//Desktop//IC-GILSON-2019//coxim_filtro.csv")

print(df.head(5))

marcacoes = []

pessoas = []

for x in range(0,6):
    linha = df.loc[x,:]
    print(linha[15])
    if linha[15] == 'Evadido':
        marcacoes.append(1)
    elif linha[15] == 'Nao Evadido':
        marcacoes.append(-1)



for posicao in range(0,7):
    linhas = df.loc[posicao,:]
    print(linhas.possuibens)
    print(linhas.possuiviaradio)
    print(linhas.familiarpossuideficienciafisica)

    if linhas.possuibens == 'Sim':
        pessoas.append(1)
    if linhas.possuiviaradio == 'Sim':
        pessoas.append(1)
    if linhas.familiarpossuideficienciafisica == 'Sim':
        pessoas.append(0)
    print("-------------------------------------")
    

print(pessoas)

#bichinho1 = [1, 1, 1]
#bichinho2 = [1, 0, 1]
#bichinho3 = [0, 1, 1]
#bichinho4 = [1, 1, 0]
#bichinho5 = [0, 1, 0]
#bichinho6 = [0, 1, 0]

#dados = [bichinho1, bichinho2, bichinho3, bichinho4, bichinho5, bichinho6]

#Se GATO = 1 / Se CACHORRO = -1
#marcacoes = [1, 1, 1, -1, -1, -1]

######################## 2 CRIANDO MODELO   ################################################  


#modelo = MultinomialNB()
#modelo.fit(dados, marcacoes)

######################## 3 FAZENDO PREDICOES   ################################################ 
#bicho_misterioso1 = [1, 1, 1]
#bicho_misterioso2 = [1, 0, 0]
#bicho_misterioso3 = [0, 0, 1]

#teste = [bicho_misterioso1, bicho_misterioso2, bicho_misterioso3]

#marcacoes_teste = [1, -1, 1]

######################## 4 OBSERVANDO RESULTADOS   ################################################ 
#resultado = modelo.predict(teste)

#diferencas = resultado - marcacoes_teste

#acertos = [d for d in diferencas if d == 0]

#total_de_acertos = len(acertos)

#total_de_elementos = len(teste)

#taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

#print("1: Evadido e -1: Nao Evadido")

#print("Resultado: ")
#print(resultado)

#print ("Marcacoes: ")
#print("Diferencas: ")
#print(diferencas)

#print("Taxa de acerto do Algoritmo: ")
#print(taxa_de_acerto)
#print(marcacoes_teste)

