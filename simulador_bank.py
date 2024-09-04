def depositar(saldo, monto):
    saldo += monto
    return saldo

def retirar(saldo, monto):
    saldo -= monto
    return saldo

def verificar_usuario(users):
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")
    if user in users and users[user]["password"] == password:
        saldo_inicial = users[user]["saldo"]
        return user, saldo_inicial
    else:
        return None, None

users = {
    "user1": {"password": "12345678", "saldo": 1000},
    "user2": {"password": "12345678", "saldo": 500},
}

user, saldo = verificar_usuario(users)
if user is None:
    print("Usuario o contraseña incorrecta")
else:
    while True:
        opcion = input(f"""Bienvenido {user}
1.- Para depositar
2.- Para retirar
3.- Para ver tu saldo actual
4.- Para salir
""")
        if opcion == "1":
            monto = float(input("¿Cuánto deseas depositar? : "))
            saldo = depositar(saldo, monto)
            print("\nTu saldo actual es de: ", saldo)
        elif opcion == "2":
            monto = float(input("¿Cuánto deseas retirar? : "))
            if monto > saldo:
                print("\nNo tienes suficiente saldo")
            else:
                saldo = retirar(saldo, monto)
                print("\nTu saldo actual es ", saldo)
        elif opcion == "3":
            print("\nTu saldo actual es de: ", saldo)
        elif opcion == "4":
            print("\nCerrando scrip...")
            break
        else:
            print("Opción no valida, intenta de nuevo.")