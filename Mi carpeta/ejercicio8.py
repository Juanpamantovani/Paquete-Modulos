# Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del equipo de recursos humanos de la empresa.
# En el mismo debe existir una primera función que calcule el valor del salario de cada empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
# incremento del 3% por cada año de antigüedad.
# También debe haber una segunda función que calcule la productividad del empleado. La misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de horas de trabajo.
# En tercer lugar debe haber una función que reporte toda la información del empleado
# incluyendo la calculada en las dos funciones anteriores, nombre y edad.


def calcular_salario(horas_trabajadas: float, antiguedad: int) -> float:
    '''
    Calcula el salario de un empleado según las horas trabajadas y su antigüedad

    Parametros:
    
    horas_trabajadas: float
        Cantidad de horas trabajadas por el empleado

    antiguedad: int
        Años de antigüedad del empleado.
        

    Retorna: float
        Salario calculado en base a horas trabajadas y antigüedad
    '''
    salario_base = horas_trabajadas * 10
    incremento_antiguedad = salario_base * (0.03 * antiguedad)
    salario_total = salario_base + incremento_antiguedad
    return salario_total

#Calcula la productividad en base a las horas trabajadas y la produccion del empleado
def calcular_productividad(artefactos_producidos: int, horas_trabajadas: float) -> float:
    '''
    Calcula la productividad del empleado

    Parametros:
    
    artefactos_producidos: int
        Cantidad de artefactos producidos por el empleado

    horas_trabajadas: float
        Cantidad de horas trabajadas por el empleado
        

    Retorna: float
        Productividad calculada como artefactos producidos por hora trabajada
    '''
    productividad_empleado = artefactos_producidos / horas_trabajadas 
    return productividad_empleado

#Muestra la informacion del empleado
def info_empleado(nombre: str, edad: int, salario_total: float, productividad_empleado: float) -> None:
    
    '''
    Reporta toda la información del empleado

    Parametros:
    
    nombre: str
        Nombre del empleado.

    edad: int
        Edad del empleado
        
    salario total: float
        salario total del empleado
    
    productividad del empleado: float
        Cantidad de productividad por parte del empleado
    '''
     
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Salario Total: {salario_total}")
    print(f"Productividad del Empleado: {productividad_empleado} artefactos/hora")
    




    

   
    

    