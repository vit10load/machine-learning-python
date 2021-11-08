<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>

EVASAO: PROJETO SOBRE MACHINE LEARNING COM PYTHON
=================================================

[![Build Status](https://api.travis-ci.com/python/mypy.svg?branch=master)](https://travis-ci.com/python/mypy)
[![Documentation Status](https://readthedocs.org/projects/mypy/badge/?version=latest)](https://mypy.readthedocs.io/en/latest/?badge=latest)
[![Chat at https://gitter.im/python/typing](https://badges.gitter.im/python/typing.svg)](https://gitter.im/python/typing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


3 Pilares de desenvolvimento do projeto
---------------------------------------

- 1° Este algoritmo tem a finalidade de treinar uma base de dados com informações sobre os alunos de uma determinada instituição.

- 2° Foi utilizado a linguagem de programação python para solucionar o problema.

- 3° A biblioteca sklearn foi o objeto de estudo para o desenvolvimento e implementação.


Qual a importância deste projeto?
---------------------------------

A importância esta ligado ao fato de tentar prevenir que uma determinada parcela de alunos venha
desistir do curso. Assim o mesmo ficando com status evadido no sistema acadêmico.

Segue um exemplo de treinamento com caẽs e gatos

``` 
    from sklearn.naive_bayes import MultinomialNB
    import pandas as pd

    bichinho1 = [1, 1, 1]
    bichinho2 = [1, 0, 1]
    ichinho3 = [0, 1, 1]
    bichinho4 = [1, 1, 0]
    bichinho5 = [0, 1, 0]
    bichinho6 = [0, 1, 0]

    dados = [bichinho1, bichinho2, bichinho3, bichinho4, bichinho5, bichinho6]

    #Se GATO = 1 / Se CACHORRO = -1
    marcacoes = [1, 1, 1, -1, -1, -1]


    modelo = MultinomialNB()
    modelo.fit(dados, marcacoes)

```

Inicio Rapido
--------------

Mypy can be installed using pip:

    $ python3 teste.py



Fonte
-----

* Link: [linter-mypy](https://medium.com/ciencia-descomplicada/machine-learning-classificando-gatos-e-cachorros-d45f1fddbff)

