# ejerc 8: menu interactivo - cajero automatico
# hacer un programa que simule un cajero automatico con un
#saldo inicial de $ 1000 y tendra el siguiente menu de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000
while True:
    print("MENU:")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    opcion = int(input("digite una opcion de menu:"))
    print()
    if opcion == 1:
        extra = float(input("cuanto dinero desea ingresar ->"))
        saldo *= extra
        print(f"dinero en la cuenta al momento :$ {saldo}")
    elif opcion == 2:
        retirar = float(input("¿Cuánto dinero desea retirar? -> $"))
        if retirar > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: $ {saldo:.2f}")

    elif opcion == 3:
        print(f"Dinero disponible: $ {saldo:.2f}")

    elif opcion == 4:
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")
        print()