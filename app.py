import modulo, os

def mostrar_menu():
    print("""\n========== MENU PRINCIPAL ==========
1. Stock por categoria
2. Buscar productos por rango de precio
3. Actualizar precio
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
====================================""")

def leer_opcion():
    while True:
        try:
            opcion_elegida = int(input("Ingresa una opcion: "))
            if opcion_elegida >= 1 and opcion_elegida <= 7:
                return opcion_elegida
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

productos = {
    "P101": ["Cuaderno", "Papeleria", 2490, True],
    "P102": ["Lapiz", "Papeleria", 590, True],
    "P103": ["Botella", "Accesorios", 6990, False],
    "P104": ["Mochila", "Accesorios", 24990, True]
}

inventario = {
    "P101": [30, 15],
    "P102": [120, 50],
    "P103": [0, 10],
    "P104": [8, 25]
}

while True:
    os.system("cls")
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        categoria_buscada = input("Ingrese categoria a buscar: ").strip()
        modulo.stock_categoria(categoria_buscada, productos, inventario)
        
    elif opcion == 2:
        try:
            precio_minimo = int(input("Ingresa el precio minimo: "))
            precio_maximo = int(input("Ingresa el precio maximo: "))
            modulo.buscar_precio(precio_minimo, precio_maximo, productos, inventario)
        except ValueError:
            print("Error: Los precios tienen que ser numeros enteros")
            
    elif opcion == 3:
        while True:
            codigo_ingresado = input("Ingresa el codigo del producto que quiere actualizar: ").strip()
            if modulo.buscar_codigo(codigo_ingresado, productos):
                try:
                    precio_nuevo = int(input("Ingresa el nuevo precio: "))
                    if modulo.validar_precio(precio_nuevo):
                        modulo.actualizar_precio(codigo_ingresado, precio_nuevo, productos)
                        print("El precio se actualizo con exito")
                        break 
                    else:
                        print("Error: El precio no puede ser negativo o cero")
                except ValueError:
                    print("Error: El precio tiene que ser un numero entero")
            else:
                print("Ese codigo de producto no existe")
                
            seguir = input("Quieres actualizar otro producto? (s/n): ").lower()
            if seguir != "s":
                break
                
    elif opcion == 4:
        while True:
            codigo_nuevo = input("Ingresa el codigo del producto nuevo: ").strip().upper()
            if modulo.validar_codigo(codigo_nuevo, productos):
                break
            else:
                print("Error: Ese codigo ya lo ocuparon o esta vacio")
                
        while True:
            nombre_nuevo = input("Ingresa el nombre del producto: ").strip()
            if modulo.validar_nombre(nombre_nuevo):
                break
            else:
                print("El nombre no puede estar en blanco")
                
        while True:
            cat_nueva = input("Ingrese la categoria: ").strip()
            if modulo.validar_categoria(cat_nueva):
                break
            else:
                print("La categoria no puede estar en blanco")
                
        while True:
            try:
                precio_ingresado = int(input("Ingresa el precio en pesos: "))
                if modulo.validar_precio(precio_ingresado):
                    break
                else:
                    print("El precio tiene que ser mayor a cero")
            except ValueError:
                print("ERROR: Debe ser un numero entero positivo")
                
        while True:
            disp = input("Esta disponible? (s/n): ").lower()
            if modulo.validar_disponible(disp):
                if disp == "s":
                    esta_disponible = True
                else:
                    esta_disponible = False
                break
            else:
                print("Solo puedes responder con 's' o 'n'")
                
        while True:
            try:
                stock_ingresado = int(input("Ingresa la cantidad de stock que hay: "))
                if modulo.validar_stock(stock_ingresado):
                    break
                else:
                    print("El stock no puede ser negativo")
            except ValueError:
                print("El stock debe ser un numero entero")
                
        while True:
            try:
                cant_vendidos = int(input("Ingresa la cantidad que ya se vendio: "))
                if modulo.validar_vendidos(cant_vendidos):
                    break
                else:
                    print("Los vendidos no pueden ser negativos")
            except ValueError:
                print("Debes ingresar un numero entero")
                
        modulo.agregar_producto(codigo_nuevo, nombre_nuevo, cat_nueva, precio_ingresado, esta_disponible, stock_ingresado, cant_vendidos, productos, inventario)
        print("Producto agregado con exito!")
        
    elif opcion == 5:
        codigo_borrar = input("Ingresa el codigo del producto que quieres eliminar: ").strip()
        if modulo.eliminar_producto(codigo_borrar, productos, inventario):
            print(f"El producto {codigo_borrar.upper()} fue eliminado correctamente")
        else:
            print("No se puede eliminar porque ese producto no existe")
            
    elif opcion == 6:
        modulo.mostrar_productos(productos, inventario)
        
    elif opcion == 7:
        print("Gracias por usar el programa, hasta luego!!")
        break
        
    print("")
    os.system("pause")
