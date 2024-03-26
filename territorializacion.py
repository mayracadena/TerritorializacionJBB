import processing
from qgis.core import QgsVectorLayer
import pandas as pd
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
        
    def manejo_excel(terri, datos):
        file_name = 'D:/jbb/trabajo_aparte/20230324_Terri.xlsx'
        h_localidad = 'Localidad'
        colum_localidad = {'A', 'D'}
        # read the second sheet of the Excel file using Pandas
        excel_terri = openpyxl.load_workbook(file_name)
        hoja = excel_terri[h_localidad]
        last_row = hoja.max_row
        # display the first five rows of the DataFrame
        print(last_row)
        for f in range(len(datos)):
            for c in range(len(datos[f])):
                print(datos[f][c])
                last_row =+ 1
                hoja[colum_localidad[f] + last_row] = datos[f][c]

    def valores_atribututos(datos, terri):
        
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
        if terri == 2:
            for se in valores_seleccionados:
                i += 1
                valores.append([se.attribute('LocNombre'),se.attribute('LocCodigo')])
                print(se.attribute('LocNombre'))
        
        return valores
        


        

"""los valores posibles de terri son:
1. UPZ
2. LOCALIDAD
3. CERROS
4. SUBCUENCA
5. MUNICIPIO
6. EEP
"""


seleccionados = Territorializacion.select_by_location(Territorializacion.capa_activa(), 2)
Territorializacion.manejo_excel(2, seleccionados)
#Territorializacion.valores_atribututos(seleccionados, 2)