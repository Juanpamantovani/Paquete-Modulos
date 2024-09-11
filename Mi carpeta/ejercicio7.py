# Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
# productos con impuestos para una determinada empresa:
# La respuesta de chatgpt es: def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
# resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
# resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
# resultado_final = resultado_nacional + resultado_exportaciones
# return resultado_final
# ¿Considera que cumple con los objetivos de una función?
# Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario, documente y denomine correctamente.
# Función para calcular el valor de exportaciones con las retenciones


def calcular_ventas_exportaciones(valor_exportaciones: float, retenciones: float = 15) -> float:
    '''
    Calcula el valor de ventas por exportaciones aplicando las retenciones.
    
    Parametros:
    
    valor_exportaciones: float
        El valor bruto total de las exportaciones
        
    retenciones: float
        Porcentaje de retenciones a aplicar
        
    Retorna: float
        Valor neto de las exportaciones después de aplicar las retenciones
    '''
    resultado_exportaciones = valor_exportaciones * (1 - (retenciones / 100))
    return resultado_exportaciones

#funcion para calcular el valor de ventas nacionales con IVA
def calcular_ventas_nacionales_con_iva(valor_ventas_nacionales: float, iva: float = 21) -> float:
    '''
    Calcula el valor de las ventas nacionales incluyendo el IVA
    
    Parámetros:
    
    
    valor_ventas_nacionales: float
        El valor bruto total de las ventas nacionales
        
    iva: float
        Porcentaje de IVA a aplicar 
        
    Retorna: float
        Valor de las ventas nacionales + IVA
    '''
    resultado_nacional = valor_ventas_nacionales * (1 + (iva / 100))
    return resultado_nacional

#Función para calcular el total de las ventas nacionales y de exportación con impuestos
def calcular_total_ventas_con_impuestos(valor_exportaciones: float, valor_ventas_nacionales: float, iva: float = 21, retenciones: float = 15) -> float:
    '''
    Calcula el valor total de las ventas sumando ventas nacionales y exportaciones

    Parametros:
    
    valor_exportaciones: float
        El valor bruto total de las exportaciones
        
    valor_ventas_nacionales: float
        El valor bruto total de las ventas nacionales
        
    iva: float
        Porcentaje de IVA a aplicar a las ventas nacionales
        
    retenciones: float
        Porcentaje de retenciones a aplicar a las exportaciones

    Retorna: float
        Valor final total de ventas nacionales (con IVA) y exportaciones
    '''
    total_nacional = calcular_ventas_nacionales_con_iva(valor_ventas_nacionales, iva)
    
    total_exportaciones = calcular_ventas_exportaciones(valor_exportaciones, retenciones)

    #Sumar ambos valores
    resultado_total = total_nacional + total_exportaciones
    return resultado_total

#Solicitud de datos al usuario
def main():
    valor_exportaciones = float(input("Introduce el valor bruto de las exportaciones: "))
    valor_ventas_nacionales = float(input("Introduce el valor bruto de las ventas nacionales: "))
    
    iva = float(input("Introduce el porcentaje de IVA (por defecto 21%): ") or 21)
    retenciones = float(input("Introduce el porcentaje de retenciones (por defecto 15%): ") or 15)

    total = calcular_total_ventas_con_impuestos(valor_exportaciones, valor_ventas_nacionales, iva, retenciones)
    print(f"El valor total de ventas nacionales y exportaciones con retenciones es: {total}")

if __name__ == "__main__":
    main()