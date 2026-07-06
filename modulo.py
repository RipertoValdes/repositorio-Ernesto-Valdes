# ----- VALIDACIONES ------

def validar_codigo(codigo, productos):
    if len(codigo.strip()) > 0:
        for c in productos.keys():
            if c.upper() == codigo.upper():
                return False 
        return True
    return False

def validar_nombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    return False

def validar_categoria(categoria):
    if len(categoria.strip()) > 0:
        return True
    return False

def validar_precio(precio):
    if precio > 0:
        return True
    return False

def validar_disponible(opcion):
    if opcion.lower() == "s" or opcion.lower() == "n":
        return True
    return False

def validar_stock(stock):
    if stock >= 0:
        return True
    return False

def validar_vendidos(vendidos):
    if vendidos >= 0:
        return True
    return False


# --- FUNCIONES DE OPERACION ---

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    codigo_mayuscula = codigo.upper()
    productos[codigo_mayuscula] = [nombre, categoria, precio, disponible]
    inventario[codigo_mayuscula] = [stock, vendidos]
    return True

def stock_categoria(categoria, productos, inventario):
    total_unidades = 0
    lo_encontre = False
    
    for c in productos.keys():
        if productos[c][1].upper() == categoria.upper():
            total_unidades = total_unidades + inventario[c][0]
            lo_encontre = True
            
    if lo_encontre == True:
        print(f"\nEl stock total para la categoria '{categoria}' es de {total_unidades} unidades")
    else:
        print("\nNo se encontraron productos en esa categoria")

def buscar_precio(precio_minimo, precio_maximo, productos, inventario):
    hay_productos = False
    lista_ordenada = []
    
    for c in productos.keys():
        precio_actual = productos[c][2]
        stock_actual = inventario[c][0]
        
        if precio_actual >= precio_minimo and precio_actual <= precio_maximo and stock_actual > 0:
            nombre_producto = productos[c][0]
            lista_ordenada.append(f"{nombre_producto}--{c}")
            hay_productos = True
            
    if hay_productos == True:
        lista_ordenada.sort() 
        print("")
        for item in lista_ordenada:
            print(item)
    else:
        print("\nNo hay productos con stock en ese rango de precios")

def buscar_codigo(codigo, productos):
    for c in productos.keys():
        if c.upper() == codigo.upper():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, productos):
    codigo_mayuscula = codigo.upper()
    if buscar_codigo(codigo_mayuscula, productos):
        # El precio se guarda en el indice 2
        productos[codigo_mayuscula][2] = nuevo_precio
        return True
    return False

def eliminar_producto(codigo, productos, inventario):
    codigo_mayuscula = codigo.upper()
    if buscar_codigo(codigo_mayuscula, productos):
        
        productos.pop(codigo_mayuscula)
        inventario.pop(codigo_mayuscula)
        return True
    return False

def mostrar_productos(productos, inventario):
    print("\n=== LISTA DE PRODUCTOS REGISTRADOS ===")
    for c in productos.keys():
        datos_prod = productos[c]
        datos_inv = inventario[c]
        
        print(f"CODIGO: {c}")
        print(f"Nombre: {datos_prod[0]}")
        print(f"Categoria: {datos_prod[1]}")
        print(f"Precio: ${datos_prod[2]}")
        print(f"Disponible: {datos_prod[3]}")
        print(f"Stock: {datos_inv[0]}")
        print(f"Vendidos: {datos_inv[1]}")
        print("-------------------------")
