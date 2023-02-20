"""Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados."""

password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')

    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")
else:
    print('Tu contraseña es muy corta e insegura.')

    if (password != 'miClaveSegura'):
        print("Además, es incorrecta (por supuesto).")