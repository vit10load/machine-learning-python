1° Este algoritmo tem a finalidade de 
treinar uma base de dados relacionada a
evasão escolar.

2° Foi utilizado a linguagem de programação
python.

3° A biblioteca sklearn. Usamos o algoritmo de classificação Nayve Bayes.

4° O Algoritmo me retorna uma matriz com
arrays contendo 0 e/ou 1 com as características de cada
linha da base de dados. Por exemplo: Segue uma linha do arquivo csv

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

Exemplo de resultado:

matriz_final[0] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
matriz_final[1] = [1,0,1,0,1,1,1,0,0,0,1,0,1,1,0]

Esta mesma matriz é responsavel por armazenar (0)falso ou (1)verdadeiro na posição caso atenda a condição
do código. No final de todas as linhas serão retornados arrays com 15 números de acordo com o número.
de linhas do arquivo csv.

Exemplo matriz final com 15 valores(cada vetor):
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], 
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]

5° Retornar uma matriz de marcação se o aluno está evadido ou não.

# exemplo:

[0, 1, 0, 1, 0, 1, 0, 0, 0, 1]

1 = verdadeiro (evadido)
0 = falso (nao evadido)

O arquivo utilizado foi coxim_filtro.csv

Depois de retornada a matriz com as informações, podemos entao realizar a predição
dos dados. Segue um link de como pode ser feito.

https://medium.com/ciencia-descomplicada/machine-learning-classificando-gatos-e-cachorros-d45f1fddbff

Um forte abraço!!!!!!


