import gastos

def ejecutar_ui():
    while True:
        print("\n--- GESTOR DE GASTOS ---")
        print("1. Añadir gasto")
        print("2. Mostrar gastos")
        print("3. Mostrar total")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            concepto = input("¿En qué gastaste?: ")
            cantidad = float(input("¿Cuánto costó?: "))
            
            if gastos.agregar_gasto(concepto, cantidad):
                print("¡Gasto guardado!")
            else:
                print("Error: La cantidad debe ser mayor que 0.")

        elif opcion == "2":
            todos = gastos.obtener_gastos()
            if len(todos) == 0:
                print("No hay gastos registrados.")
            else:
                for g in todos:
                    print(f"- {g['concepto']}: ${g['cantidad']}")

        elif opcion == "3":
            total = gastos.calcular_total()
            print(f"Total gastado: ${total}")

        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción incorrecta.")