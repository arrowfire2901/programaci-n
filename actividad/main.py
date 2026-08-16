import os
from producto import Producto


def cargar_productos(ruta: str) -> list:
    productos = []
    
    with open(ruta, "r", encoding = "ascii") as archivo:
        lineas = archivo.readlines()
    datos = [linea.strip("\n") for linea in lineas]
    
    for product in datos:
        separar_datos = product.split(",")
        productos.append(Producto(str(separar_datos[0]), int(separar_datos[1]), int(separar_datos[2])))
        
    return productos


def simular_ventas(productos: list) -> None:
    for producto in productos:
        producto.vender()


if __name__ == '__main__':
    ruta = os.path.join('data', 'menu.txt')
    productos = cargar_productos(ruta)
    print('=== DCCafeteria ===')
    for product in productos:
        print(product.descripcion())
    print(f'Productos registrados: {Producto.total_productos}')
    simular_ventas(productos)
    simular_ventas(productos)