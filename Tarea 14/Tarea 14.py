#función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función
monto_1 = 1000  # Monto total de la primera compra
descuento_1 = calcular_descuento(monto_1)  # Usando el porcentaje por defecto (10%)
monto_final_1 = monto_1 - descuento_1

monto_2 = 1500  # Monto total de la segunda compra
porcentaje_descuento_2 = 20  # Porcentaje de descuento especificado
descuento_2 = calcular_descuento(monto_2, porcentaje_descuento_2)
monto_final_2 = monto_2 - descuento_2

# Resultados
descuento_1, monto_final_1, descuento_2, monto_final_2
