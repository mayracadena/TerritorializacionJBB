import processing



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
    return lyr.name()
        
def select_by_location(layershp01):
    """
    processing.run("qgis:selectbylocation", {
    "INPUT":lyr_input,\
    "PREDICATE":0,\
    "INTERSECT":lyr_intersect,\
    "METHOD":0,\
    "OUTPUT":path}
)
PREDICATE: Where the features (geometric predicate)

    Parameter type: QgsProcessingParameterEnum

    Available values:
        - 0: intersect
        - 1: contain
        - 2: disjoint
        - 3: equal
        - 4: touch
        - 5: overlap
        - 6: are within
        - 7: cross

    Accepted data types:
        - int
        - str: as string representation of int, e.g. '1'
        - QgsProperty
    
    """
    processing.runalg("qgis:selectbylocation", INPUT, INTERSECT, METHOD, OUTPUT)

#valores_atributivos(layershp01)
capas_activas()