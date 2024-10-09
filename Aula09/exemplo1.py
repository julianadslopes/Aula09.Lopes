import os
os.system ("cls")

# try:
#     n = int(input("Informe um número: "))
# except:
#     print ("Erro!")

# try:
#     n = int(input("Informe um número: "))
# except (ValueError, KeyboardInterrupt) as e:  # e vai ser usado como apelido para o erro do tipo de valor 
#     print (f"{e}")


try:
    txt = input ("Informe o nome: ") [0] # o [0] indica que quero uma 'lista'
except IndexError as e:
    print (f" {e} Precisa digitar algo")
else: # Neste caso, o else só vai ser rodado se NÃO DER ERRO
    print ("Acertou!")
finally:
    print ("Sempre executado")        