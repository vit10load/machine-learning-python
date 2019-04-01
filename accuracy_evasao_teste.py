import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

#df = pd.read_csv("C://Users//vitcl//Desktop//IC-GILSON-2019//coxim_filtro.csv")

df = pd.read_csv("C://Users//vitcl//Desktop//IC-GILSON-2019//coxim_filtro.csv")

print(df.shape[0])
print("-----------------------------------")
print(df.shape[1])
#sexo                                                   Masculino
#estadocivil                                            CASADO(A)
#corraca                                                    PARDA
#comoconcluiensinomedio             Sim Somente em Escola Pública
#bolsaensinomedio                                   nao Respondeu
#tipoconstrucaocasa                                     Alvenaria
#possuibens                                                   Não
#possuiviaradio                                               Não
#possuibpcloas                                                Nao
#possuideficienciavisual                                      Nao
#possuideficienciafisica                                      Nao
#familiarpossuideficienciafisica                              Nao
#parentescoresponsavel1                                       Mae
#escolaridade_responsável_1                Fundamental incompleto
#escolaridaderesponsavel2                  Fundamental incompleto
#situacao                                                       1
#Name: 0, dtype: object

lin = int(df.shape[0])
col = int(df.shape[1])
matriz_treino = []
matriz_final = []
contador = 15
marcacoes_treino = []

for i in range(lin):
         linha = []
         linha = df.loc[i,:]        
         linha[0] = np.where(df.loc[i,"sexo"] == 'Masculino',1,0)
         matriz_treino.append(int(linha[0]))
         linha[1] = np.where(df.loc[i,"estadocivil"] == 'CASADO(A)',1,0)
         matriz_treino.append(int(linha[1]))
         linha[2] = np.where(df.loc[i,"corraca"] == "PARDA",1,0)
         matriz_treino.append(int(linha[2]))
         linha[3] = np.where(df.loc[i,"comoconcluiensinomedio"] == "Sim Somente em Escola Pública",1,0)
         matriz_treino.append(int(linha[3]))
         linha[4] = np.where(df.loc[i,"bolsaensinomedio"] == "nao Respondeu",1,0)
         matriz_treino.append(int(linha[4]))
         linha[5] = np.where(df.loc[i,"tipoconstrucaocasa"] == "Alvenaria",1,0)
         matriz_treino.append(int(linha[5]))
         linha[6] = np.where(df.loc[i,"possuibens"] == "Não" or df.loc[i,"possuibens"] == "Nao",1,0)
         matriz_treino.append(int(linha[6]))
         linha[7] = np.where(df.loc[i,"possuiviaradio"] == "Não" or df.loc[i,"possuiviaradio"] == "Nao",1,0)
         matriz_treino.append(int(linha[7]))
         linha[8] = np.where(df.loc[i,"possuibpcloas"] == "Nao" or df.loc[i,"possuibpcloas"] == "Não",1,0)
         matriz_treino.append(int(linha[8]))
         linha[9] = np.where(df.loc[i,"possuideficienciavisual"] == "Nao" or df.loc[i,"possuideficienciavisual"] == "Não",1,0)
         matriz_treino.append(int(linha[9]))
         linha[10] = np.where(df.loc[i,"possuideficienciafisica"] == "Nao" or df.loc[i,"possuideficienciafisica"] == "Não",1,0)
         matriz_treino.append(int(linha[10]))
         linha[11] = np.where(df.loc[i,"familiarpossuideficienciafisica"] == "Não" or df.loc[i,"familiarpossuideficienciafisica"] == "Nao",1,0)
         matriz_treino.append(int(linha[11]))
         linha[12] = np.where(df.loc[i,"parentescoresponsavel1"] == "Mae" or df.loc[i,"parentescoresponsavel1"] == "Pai" or df.loc[i,"parentescoresponsavel1"] == "Avo",1,0)
         matriz_treino.append(int(linha[12]))
         linha[13] = np.where(df.loc[i,"escolaridade_responsável_1"] == "Fundamental incompleto" or df.loc[i,"escolaridade_responsável_1"] == "Medio incompleto"
                              or df.loc[i,"escolaridade_responsável_1"] == "Superior incompleto",1,0)
         matriz_treino.append(int(linha[13]))
         linha[14] = np.where(df.loc[i,"escolaridaderesponsavel2"] == "Fundamental incompleto"
                              or df.loc[i,"escolaridaderesponsavel2"] == "Medio incompleto"
                              or df.loc[i,"escolaridaderesponsavel2"] == "Superior incompleto",1,0)
         matriz_treino.append(int(linha[14]))
         linha[15] = np.where(df.loc[i,"situacao"] == "Evadido" or df.loc[i,"situacao"] == "Evadido",1,0)
         matriz_treino.append(int(linha[15]))
         marcacoes_treino.append(int(linha[15]))
         print(i)

         if i == (lin-1):
             for j in range(lin):
                 if contador == 15:
                     matriz_final.append(matriz_treino[:contador])
                     contador += 1
                 else:
                     matriz_final.append(matriz_treino[contador:(contador+15)])
                     contador += 15
                     contador += 1
