class GestionPedidos:
    def procesar_pedido(self):
        subtotal_pedido = 0
        nombres_productos = ["Laptop", "Mouse", "Laptop", "Mouse"]
        precios_productos = [10.5, 20.0, 10.5, 20.0]
        cantidades_productos = [1, 2, 1, 2]

        for indice_producto in range(len(nombres_productos)):
            if nombres_productos[indice_producto] == "Laptop":
                print(f"Producto: Laptop cuesta: {precios_productos[indice_producto]}")
                subtotal_pedido += precios_productos[indice_producto] * cantidades_productos[indice_producto]

            if nombres_productos[indice_producto] == "Mouse":
                print(f"Producto: Mouse cuesta: {precios_productos[indice_producto]}")
                subtotal_pedido += precios_productos[indice_producto] * cantidades_productos[indice_producto]

        monto_impuesto = subtotal_pedido * 0.18
        monto_descuento = 0

        if subtotal_pedido > 100:
            monto_descuento = subtotal_pedido * 0.1

        if subtotal_pedido > 200:
            monto_descuento = subtotal_pedido * 0.2

        print(f"TOTAL FINAL: {subtotal_pedido + monto_impuesto - monto_descuento}")

        tipo_cliente = "VIP"
        if tipo_cliente == "VIP":
            print("Enviar email VIP a cliente")

    def mostrar_mensaje_prueba(self):
        print("Nunca me llaman")

