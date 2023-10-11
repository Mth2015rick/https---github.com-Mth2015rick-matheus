#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("digite seu nome: ")
while len(nome) < 3:
    print("a quantidade de caracteres é menor que tres caracteres")
if len(nome) < 3:
    nome = input("digite seu nome: ")
        
idade = int(input( "digite sua idade"))
while idade < 0 or idade > 150:
    print("idade invalida")
    if idade < 0 or idade > 150:
        idade = int(input("digite sua idade")) 
        
salario = float(input("digite seu salario"))

while salario < 0:
    print("salario invalido")
    if salario < 0:
        salario = float(input("dite seu salario"))       


sexo = input("digite seu sexo (f ou m): ")
while sexo != "f" and sexo != "m":
    print("sexo invalido")
    if sexo != "f" and sexo != "m":
        sexo = input("digite o sexo (f ou m): ")







        
        
        