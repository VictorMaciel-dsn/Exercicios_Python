# -*- coding: utf-8 -*-
"""Exercício9

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T-BYQAzTzV1AcFUoIz96bB4QvBMBKFDF

**9) Faça um programa para imprimir a soma dos dez primeiros números inteiros positivos. (1 + 2 + 3 + ... + 10) utilizando repetição**
"""

i = 1
soma = 0

while i <= 10:
  soma = soma + i
  print('Números: ', i)
  i = i + 1

print('\nSoma: ', soma)