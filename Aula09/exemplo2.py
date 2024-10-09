import os
os.system ("cls")

try:
    resp = input ("Informe (s/n): ") .lower()

    if resp == "":
        raise EOFError ("Você não digitou nada") # o raise gera uma exceção manualmente
    if resp.isdigit (): # .isdigit verifica se é dígito
        raise ValueError ("Não informe números")
except EOFError as e:
    print (f"{e}")
except ValueError as e:
    print (f"{e}")
