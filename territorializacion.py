import processing
from qgis.core import QgsVectorLayer


"""layershp01 = iface.addVectorLayer("D:/jbb/trabajo_aparte/Loca.shp", "Localidad", "ogr")
if not layershp01:
    print("el layer %s no se pudo cargar"%layershp01.name())
 """   


    #manejo de geometrias
def tipo_geometria(features):
    features = layershp01.getFeatures()
    for feature in features:
        geom = feature.geometry()
        print("Feature ID: ", feature.id())
        #show some information about feacture
        if geom.wkbType()== QgsWkbTypes.Point:
            x = geom.asPoint()
            print("Point:" ,x)
        elif geom.wkbType == QgsWkbTypes.LineString: 
            x = geom.asPolyline()
            print('Line:',x,'points','length', geom.length())
        elif geom.wkbType() == QgsWkbTypes.MultiPolygon:
            x = geom.asMultiPolygon()
            print("Polygon:",x,"Area: ", geom.area())
        else:
            print("Unknown")
            print(geom.wkbType())
        

def valores_atributivos(layershp01):
    print("-VALORES ATRIBUTIVOS-")
    features = layershp01.getFeatures()
    for feature in features:
        attrs =feature.attributes()
        #attrs is a list. It contanisn all the attribute values of this feacture
        print(attrs)
        
def capas_activas():
    lyr = iface.activeLayer()
    print(lyr.name())
    return lyr
        
def select_by_location(lyr_input):
    localidades = iface.addVectorLayer("D:/jbb/trabajo_aparte/Loca.shp", "Localidad", "ogr")
    parametros = {
    "INPUT":lyr_input,
    "PREDICATE":0,
    "INTERSECT":localidades,
    "METHOD":0,
    "OUTPUT":None}
    
    processing.run("qgis:selectbylocation", parametros)
    valores_seleccionados = lyr_input.selectedFeatures()
    i = 0
    for se in valores_seleccionados:
        i += 1
        print(f"seleccionados {i} {se.geometry()}")
    


    


seleccionados = select_by_location(iface.activeLayer())
#valores_atributivos(seleccionados)