# -*- coding: utf-8 -*-
"""Exercício15

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FUYko6VrMNZDQ08nvQFkRBnzI9owUb7y

**15) Escreva um programa que escreva os números que divididos por 11 dão resto igual a 5 entre 1000 a 1299.**
"""

i = 1000

while i <= 1299:
  if i % 11 == 5:
    print(i)
  i += 1