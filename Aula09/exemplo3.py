import os
os.system ("cls")

while True:
    try:
        num = int(input("Informe um número: "))
    except (ValueError) as e:
        print (f"{e} Valor informado não é válido")
    except KeyboardInterrupt as e:
        print (f"{e} Entrada interrompida pelo usuário")
        break
    else:
        print (f"Número {num} informado com sucesso")
        break  