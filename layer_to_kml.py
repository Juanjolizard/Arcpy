####consideraciones : tener cargadas todas las capas que se desea importar. Opciones de geoproceso -> permitir reescribir ficheros de salida
import arcpy
import os

src_folder = 'C:/prueba_python'
dst_folder = 'C:/resultados_python'

###ajustamos el entorno
arcpy.env.workspace = src_folder
#arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 28N")
###bucle for para los ficheros de tipo asc, que además serán listados por la función del paquete arcpy::ListFiles()
for asc in arcpy.ListFiles("*.asc"):
    #print(asc)
    ####proyectar
    spatial_ref = arcpy.Describe(asc).spatialReference
    if spatial_ref.name == "Unknown":
        print("{0} has an unknown spatial reference".format(asc))
    else:
        print("la capa {0} tiene asignado el crs {1}".format(asc,spatial_ref))
    ###asignar nombre a los datasets de salida
    poly_kmz = os.path.join("C:\\resultados_python", os.path.splitext(os.path.basename(asc))[0] + '.kmz')
    #print("el Directorio contiene un total de " + '' + str(count(asc))+ ' ficheros en formato .asc')

    ####ejecución del algoritmo
    arcpy.LayerToKML_conversion (asc, poly_kmz)
    print(asc + " a fichero KMZ........")
    ###final del bucle
print("se ha ejecutado correctamente el script")