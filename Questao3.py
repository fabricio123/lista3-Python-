nome = input("Qual seu nome [minimo 3 caracteres]: ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: ")) 
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ") 
civil = input("Estado civil (s, c, v ou d): ") 

while len(nome) <= 3: 
      nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150): 
      idade = int(input("digite uma idade entre 0 e 150 anos: "))

while (salario<0): 
      salario = float(input("digite novamente seu salário: ")) 

while (sexo!= 'f') and (sexo!='m'): 
      sexo = input("so pode ser 'f' ou 'm': ") 

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'): 
       print("Nao tem estado civil 'confuso'") 
       civil = input("Deve ser s, c, v ou d: ")
