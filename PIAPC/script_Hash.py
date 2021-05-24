import hashlib , os
import argparse , sys
import traceback

# Funcion para usar el HashTool
def HashTool(Ruta):
    print('\n -------------------------------------------------------------------------- ')
    print('\n°°° Estamos generando el hash del archivo ... °°°')
    print('\n -------------------------------------------------------------------------- ')
    try:
        file_obj = open(Ruta, "rb")
        file = file_obj.read()
        HASH = hashlib.sha512(file)
        print(HASH)
        Hashed = HASH.hexdigest()
        print(Hashed)
        print('\n -------------------------------------------------------------------------------------- ')
        print("°°° ¡Hash SHA-512 se ha completado exitosamente! °°°")
        print('\n -------------------------------------------------------------------------------------- ')
    except:
        traceback.print_exc(file=sys.stdout)
        print('\n -------------------------------------------------------------------------- ')
        print("\n Lo sentimos la ruta ingresada es invalida '")
        print('\n--------------------------------------------------------------------------- ')
