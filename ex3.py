
idade = int(input("digite sua idade: "))
if idade < 0 or idade > 150:
        print("idade invalida")
else:
        print("idade valida")

nome = str(input("digite seu nome: "))
if nome > 3 or nome < 150:
            print("Nome válido")
else:
            print("Nome invaĺido")

salario = float(input("digite seu salário: "))
if salario.Lower()> 0:
            print("Salário válido")
else:
            print("Salário inválido")

sexo = input("Digite seu sexo (feminino ou masculino): ")
if sexo.lower() == "feminino" or sexo.lower() == "masculino":
            print("Sexo válido")
else:
            print("Sexo inválido")

estado_civil = input("Digite seu estado civil (s, c, v, d): ")
if estado_civil.lower() == "s" or estado_civil.lower() == "c" or estado_civil.lower() == "v" or estado_civil.lower() == "d":
                print("Estado civil válido")
else:
                print("Estado civil inválido")
    
    

