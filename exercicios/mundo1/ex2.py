#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo(a)!")   

#nas versões mais antigas de python, que é mostrada no curso, era utilizado o .format() para formatar a string, como no exemplo abaixo:
#print("Olá, {}! Seja bem-vindo(a)!".format(nome))  
#agora, com as f-strings, é possível formatar a string de forma mais simples e legível, como no exemplo acima.