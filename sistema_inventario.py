#Este sistema permite cargar manualmente un inventario y ver su resumen, registrar ventas, ver el resumen de ventas y
# el resumen total de Stock


inventario = {}

def cargar_inventario():
    while True:
        producto = input("Ingrese el nombre del producto o 'q' para volver al menu: ")
        if producto == 'q':
            break
        cantidad = int(input("Ingrese la cantidad en stock: "))
        precio = float(input("Ingrese el precio de venta del producto: "))
        costo = float(input("Ingrese el costo del producto: "))
        
        inventario[producto] ={"Cantidad":cantidad, "Precio Venta":precio, "Costo":costo} 
        
        continuar = input("¿Desea seguir cargando mas productos al inventario ? (s/n): ")
        if continuar != 's':
            break
        
def recibir_pedido():
    pedido = {}
    while True:
        producto = input("Ingrese el nombre del producto (o 'q' si desea terminar el pedido)")
        if producto == 'q':
            break
        
        cantidad = int(input("Ingrese la cantidad deseada: "))
        pedido[producto] = cantidad
    return pedido
    

def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cargar Inventario") 
        print("2. Registrar Ventas")
        print("3. Ver Resumenes")
        print("4. Salir")   
        
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            cargar_inventario()
            
        elif opcion == '2':
            pedido = recibir_pedido()
            if confirmar_stock(pedido):
                registrar_venta()
            else:  
                print("No hay suficiente stock para completar el pedido")
          
        elif opcion == '3':
            imprimir_resumen()
            
        elif opcion == '4':
            break
        
        else:  
            print("Opcion invalida, intente de nuevo ")  
   
#Me fijo si alcanza la cantidad de producto que tengo en stock         
def confirmar_stock(pedido):
    for producto, cantidad in pedido.items():
        if producto not in inventario or inventario[producto]['Cantidad'] < cantidad:
            return False
    return True


#obtengo el total de la venta y resto la cantidad del inventario
def registrar_venta(pedido):
    total_venta = sum(inventario[producto]['Precio venta'] * cantidad for producto, cantidad in pedido.items())
    for producto, cantidad in pedido.items():
        inventario[producto]['Cantidad'] -= cantidad
    print(f'Venta registrada exitosamente. Total de ventas: {total_venta:2f}') #2f para ponerlo en float con 2 decimales
    
    

def imprimir_resumen():
    while True:
        opcion = input("""Seleccionar una opcion:\n 1)Resumen de inventario\n 2)Resumen de ventas\n 3)Resumen de costos\n 4)Diferencia entre costo y venta\n 5) Salir\nOpcion: """)
        
        if opcion == '1':
            print("\n-----Resumen de Inventario-----")
            for producto, info in inventario.items():
                print(f'''Producto: {producto}, Cantidad: {info['Cantidad']}, Precio de venta: {info['Precio Venta']}
                      , Costo: {info['Costo']}''')
                
        elif opcion == '2':
            print("\n-----Resumen de Ventas-----")
            total_ventas = sum(info['Precio Venta']* info['Cantidad'] for info in inventario.items())
            print(f'Total de ventas: {total_ventas:2f}')
            
        elif opcion == '3':
            print("\n-----Resumen de Costos-----")
            total_costos = sum(info['Costo']* info['Cantidad'] for info in inventario.items())
            print(f'Total de costos: {total_costos:2f}')
            
        elif opcion == '4':
            print("\n-----Diferencia entre costo y venta-----")
            diferencia = sum((info['Precio Venta']- info['Costo'])* info['Cantidad'] for info in inventario.items())
            print(f'Diferencia entre costo y venta: {diferencia:2f}')
            
        elif opcion == '5':
            break
        else:
            print("Opcion invalida, intentelo de nuevo")

#Inicio el sistema
menu()



