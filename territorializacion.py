import processing
from qgis.core import QgsVectorLayer
import openpyxl


class Territorializacion:
    #ingrese acá el numero de la investigación
    codigo = ""
    #ingrese aca nombre(s) del investigador(s)
    nombres = ""
    #año de la investigación
    year= "2024"
    
    
    def __init__(self, codigo, nombres, year):
        self.codigo = codigo
        self.nombres = nombres
        self.year = year
        


    def valores_atribututos(datos, terri):
        print("-VALORES PARA EL EXCEL DE TERRITORIALIZACIÓN-")
        #features = layershp01.getFeatures()
        for f in range(len(datos)):
            for c in range(len(datos[f])):
                print(datos[f][c])
            
            
    def capa_activa():
        lyr = iface.activeLayer()
        print(lyr.name())
        return lyr
            
    def select_by_location(lyr_input, terri):
        localidades = iface.addVectorLayer("D:/jbb/trabajo_aparte/Loca.shp", "Localidad", "ogr")
        parametros = {
        "INPUT":localidades,
        "PREDICATE":0,
        "INTERSECT":lyr_input,
        "METHOD":0,
        "OUTPUT":None}
        
        processing.run("qgis:selectbylocation", parametros)
        valores_seleccionados = localidades.selectedFeatures()
           
        i = 0
        valores = []
        if terri == 1:
            for se in valores_seleccionados:
                i += 1
                valores.append([se.attribute('LocNombre'),se.attribute('LocCodigo')])
                print(se.attribute('LocNombre'))
        
        return valores
        


        

"""los valores posibles de terri son:
1. LOCALIDAD
2. UPZ
3. CERROS
4. SUBCUENCA
5. MUNICIPIO
6. EEP
"""
seleccionados = Territorializacion.select_by_location(capa_activa(), 1)
Territorializacion.valores_atribututos(seleccionados, 1)