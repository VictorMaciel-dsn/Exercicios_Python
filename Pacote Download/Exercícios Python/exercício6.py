# -*- coding: utf-8 -*-
"""Exercício6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SySKWbNnundMVav2S5nVUbvpoRLKy14o

**6) Faça um programa para exibir a soma dos números divisíveis por 7 entre 2 e 300**
"""

soma = 0
i = 7

while (i >= 2 and i <= 300):
  soma += i
  print("Número: ", i)
  i += 7

print("\nSoma: ", soma)