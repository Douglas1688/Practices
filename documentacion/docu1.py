from operaciones_matematicas import calculos_generales
class Areas():
    """Esta clase calcula las áreas de diferentes figuras geométricas"""
    def areacuadrado (lado):
        return "el área del cuadrado es: "+str(lado*lado)
    def areaTriangulo(base,altura):
        """Calcula el área de un tríángulo"""
        return "El área del triángulo es: "+str((base*altura)/2)

"""
print(areaTriangulo(2,7))
print(areaTriangulo.__doc__)
"""
help(calculos_generales)