1� Este algoritmo tem a finalidade de 
treinar uma base de dados relacionada a
evas�o escolar.

2� Foi utilizado a linguagem de programa��o
python.

3� A biblioteca sklearn. Usamos o algoritmo de classifica��o Nayve Bayes.

4� O Algoritmo me retorna uma matriz com
arrays contendo 0 e/ou 1 com as caracter�sticas de cada
linha da base de dados. Por exemplo: Segue uma linha do arquivo csv

#sexo                                                   Masculino
#estadocivil                                            CASADO(A)
#corraca                                                    PARDA
#comoconcluiensinomedio             Sim Somente em Escola P�blica
#bolsaensinomedio                                   nao Respondeu
#tipoconstrucaocasa                                     Alvenaria
#possuibens                                                   N�o
#possuiviaradio                                               N�o
#possuibpcloas                                                Nao
#possuideficienciavisual                                      Nao
#possuideficienciafisica                                      Nao
#familiarpossuideficienciafisica                              Nao
#parentescoresponsavel1                                       Mae
#escolaridade_respons�vel_1                Fundamental incompleto
#escolaridaderesponsavel2                  Fundamental incompleto
#situacao                                                       1
#Name: 0, dtype: object

Exemplo de resultado:

matriz_final[0] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
matriz_final[1] = [1,0,1,0,1,1,1,0,0,0,1,0,1,1,0]

Esta mesma matriz � responsavel por armazenar (0)falso ou (1)verdadeiro na posi��o caso atenda a condi��o
do c�digo. No final de todas as linhas ser�o retornados arrays com 15 n�meros de acordo com o n�mero.
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

5� Retornar uma matriz de marca��o se o aluno est� evadido ou n�o.

# exemplo:

[0, 1, 0, 1, 0, 1, 0, 0, 0, 1]

1 = verdadeiro (evadido)
0 = falso (nao evadido)

O arquivo utilizado foi coxim_filtro.csv

Depois de retornada a matriz com as informa��es, podemos entao realizar a predi��o
dos dados. Segue um link de como pode ser feito.

https://medium.com/ciencia-descomplicada/machine-learning-classificando-gatos-e-cachorros-d45f1fddbff

Um forte abra�o!!!!!!


