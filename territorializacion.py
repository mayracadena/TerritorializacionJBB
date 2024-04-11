"""
Para instalar librerias de python en qgis seguir estos pasos:
1. abrir OSGeo4W Shell, en esta consola escribir
2. o4w_env
3. instalar libreria de python con el siguiente codigo 
    3.1. pip install openpyxl
    
"""

import processing
from qgis.core import QgsVectorLayer
import pandas as pd
import openpyxl


class Territorializacion:
   
    def __init__(self ):
        #ingrese acá el numero de la investigación
        self.idinvestigacion = "SC_2025000"
        #ingrese aca nombre(s) del investigador(s)
        self.nombres = "Mayra Cadena"
        #año de la investigación
        self.year = "2025"
        #nombre investigacion
        self.nom_inv = "frailejoncitos"
        #linea de investigacion
        self.linea_inves = "Conectividad e Interacciones Ecológicas -  CIE" 
        
    def getNombres(self):
        return self.nombres
        
    def getNom_inv(self):
        return self.nom_inv
        
    def getIdinvestigacion(self):
        return self.idinvestigacion
        
    def getYear(self):
        return self.year
        
    def getLinea_inves(self):
        return self.linea_inves
        
    def manejo_excel(terri, datos):
        #variables globales de la clase
        nombres = Territorializacion().getNombres()
        id = Territorializacion().getIdinvestigacion()
        year = Territorializacion().getYear()
        nomb_inves = Territorializacion().getNom_inv()
        linea_inves = Territorializacion().getLinea_inves()
        
        
        
        #link del archivo de excel
        archivo_excel = 'D:/jbb/trabajo_aparte/20230324_Terri.xlsx'
        excel_terri = openpyxl.load_workbook(archivo_excel)
        h_terri = ''
        if(terri == 1):
            h_terri = 'UPZ_UPR'
        elif(terri == 2):
            h_terri = 'Localidad'
        elif(terri == 3):
            h_terri = 'Cerros'
        elif(terri == 4):
            h_terri = 'Subcuenca'
        elif(terri == 5):
            h_terri = 'Municipio'
        elif(terri == 6):
            h_terri = 'EEP'
            
        
        hoja = excel_terri[h_terri]
        last_row = hoja.max_row 
        
       
        for loc in datos:
            last_row = last_row+1
            nombre_terri = loc[0]
            codigo = loc[1]
            if(terri == 1):
                #1. UPZ
                hoja[f'C{last_row}'] = nombre_terri
                hoja[f'A{last_row}'] = codigo
                hoja[f'I{last_row}'] = id
                hoja[f'J{last_row}'] = nomb_inves
                hoja[f'K{last_row}'] = linea_inves
                hoja[f'L{last_row}'] = year
                hoja[f'M{last_row}'] = nombres
            elif(terri == 2):
                #2. LOCALIDAD
                hoja[f'A{last_row}'] = nombre_terri
                hoja[f'D{last_row}'] = codigo
                hoja[f'E{last_row}'] = id
                hoja[f'F{last_row}'] = nomb_inves
                hoja[f'G{last_row}'] = linea_inves
                hoja[f'H{last_row}'] = year
                hoja[f'I{last_row}'] = nombres
            elif(terri == 3):
                #3. CERROS
                hoja[f'D{last_row}'] = nombre_terri
                hoja[f'A{last_row}'] = codigo
                hoja[f'I{last_row}'] = id
                hoja[f'J{last_row}'] = nomb_inves
                hoja[f'K{last_row}'] = linea_inves
                hoja[f'L{last_row}'] = year
                hoja[f'M{last_row}'] = nombres
            elif(terri == 4):
                #4. SUBCUENCA
                hoja[f'D{last_row}'] = nombre_terri
                hoja[f'A{last_row}'] = codigo
                hoja[f'I{last_row}'] = id
                hoja[f'J{last_row}'] = nomb_inves
                hoja[f'K{last_row}'] = linea_inves
                hoja[f'L{last_row}'] = year
                hoja[f'M{last_row}'] = nombres
            elif(terri == 5):
                #5. MUNICIPIO
                hoja[f'F{last_row}'] = nombre_terri
                hoja[f'E{last_row}'] = codigo
                hoja[f'J{last_row}'] = id
                hoja[f'K{last_row}'] = nomb_inves
                hoja[f'L{last_row}'] = linea_inves
                hoja[f'M{last_row}'] = year
                hoja[f'N{last_row}'] = nombres
            elif(terri == 6):
                #6. EEP
                hoja[f'A{last_row}'] = nombre_terri
                hoja[f'B{last_row}'] = codigo
                hoja[f'C{last_row}'] = id
                hoja[f'D{last_row}'] = nomb_inves
                hoja[f'E{last_row}'] = linea_inves
                hoja[f'F{last_row}'] = year
                hoja[f'G{last_row}'] = nombres
            

   
        excel_terri.save(archivo_excel)
        QgsProject.instance().removeMapLayer(iface.activeLayer())
            
     
    def valores_atribututos(datos, terri):
        
        for f in range(len(datos)):
            for c in range(len(datos[f])):
                print(datos[f][c])
            
            
    def capa_activa():
        lyr = iface.activeLayer()
        return lyr
            
    def select_by_location(lyr_input, terri):
        valores = []
        capa = ''
        nombre_capa = ''
        if(terri == 1):
            capa = ""
            nombre_capa = "UPZ"
        elif(terri == 2):
            capa = "D:/jbb/trabajo_aparte/Loca.shp"
            nombre_capa = "Localidad"
        elif(terri == 3):
            capa = ""
            nombre_capa = "Cerros"
        elif(terri == 4):
            capa = "Subcuenca"
            nombre_capa = "Localidad"
        elif(terri == 5):
            capa = ""
            nombre_capa = "Municipios"
        elif(terri == 6):
            capa = ""
            nombre_capa = "EEP"
            
        
        ubicacion = iface.addVectorLayer(capa, nombre_capa, "ogr")
        parametros = {
        "INPUT":ubicacion,
        "PREDICATE":0,
        "INTERSECT":lyr_input,
        "METHOD":0,
        "OUTPUT":None}
        
        processing.run("qgis:selectbylocation", parametros)
        valores_seleccionados = ubicacion.selectedFeatures()
           
        
        
        for se in valores_seleccionados:
            #if(terri == 1):
                #upz
            if(terri == 2):
                valores.append([se.attribute('LocNombre'),se.attribute('LocCodigo')])
            #elif(terri == 3):
                #Cerros
            #elif(terri == 4):
                #Subcuenca
            #elif(terri == 5):
                #Municipio
            #elif(terri == 6):
                #EEP
            
            
    
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