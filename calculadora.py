# Yahir Navarro Amador

# Programa que ayuda a sacar la suma, resta, multiplicación y division de dos
# numeros
reg = 0
while reg == 0:
    print('----- C A L C U L A D O R A -----')
    print(' 1.- Suma \n 2.- Resta \n 3.- Multiplicación \n 4.- División \n')
    op = int(input('Ingresa la opción deseada: '))
    n1 = int(input('Ingrese el primer numero: '))
    n2 = int(input('Ingrese el segundo numero: '))
    if op == 1:
        resultado = n1 + n2
        operacion = 'Suma'
    elif op == 2:
        resultado = n1 - n2
        operacion = 'Resta'
    elif op == 3:
        resultado = n1 * n2
        operacion = 'Multiplicación'
    elif op == 4:
        while n2 <= 0:
            print('\nNo se puede realizar la division el segundo numero debe ' +
                  ' ser mayor a cero')
            n2 = int(input('\nIngrese el segundo numero: '))
        resultado = n1 / n2
        operacion = 'Division'
    else:
        print('\nOPCIÓN INVALIDA')
        
    print('\nEl resultado de la ' + operacion + ' es: ' + str(resultado))
    operacion = 0
    reg = int(input('¿Desea realizar otra operación? Si = 0 | No = 1: '))
print('Gracias vuelva pronto')

            
        
