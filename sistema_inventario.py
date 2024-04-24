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
            
def confirmar_stock(pedido):
    pass

def registrar_venta(pedido):
    pass

def imprimir_resumen():
    print("Resumen")

#Inicio el sistema
menu()



