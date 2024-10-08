import os
os.system ("cls")

# try:
#     n = int(input("Informe um número: "))
# except:
#     print ("Erro!")

try:
    n = int(input("Informe um número: "))
except (ValueError, KeyboardInterrupt) as e:  # e vai ser usado como apelido para o erro do tipo de valor 
    print (f"{e}")
