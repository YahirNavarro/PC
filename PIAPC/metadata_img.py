# -*- encoding: utf-8 -*-

import os, sys, traceback

try:
    from PIL.ExifTags import TAGS, GPSTAGS
    from PIL import Image
except ImportError:
    os.system('pip install -r requirements.txt')
    print('Espere un momento, se estan instalando los paquetes necesarios.')
    print('Se necesita ejecutar el script nuevamente.')
    exit()


def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMeta(route):
    try:
        os.chdir(route)
        print("Verificando imagenes...")
        loadarchive = open("repmet.txt","w")
        loadarchive.write("Se ha extraido la metadata de cada imagen:")
        loadarchive.close()

        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                name = os.path.join(root, name)
                loadarchive = open("repmet.txt","a+")
                loadarchive.write("Imagen: %s\n" %name)
                loadarchive.close()
                try:
                    exifData = {}
                    exif = get_exif_metadata(name)
                    for metadata in exif:
                        loadarchive = open("repmet.txt","a+")
                        loadarchive.write("Metadata: %s - Value: %s \n" %(metadata, exif[metadata]))
                        loadarchive.close()
                except:
                    loadarchive = open("repmet.txt","a+")
                    loadarchive.write("No se han detectado imagenes")
                    loadarchive.close()
        print("El reporte se encuentra en la carpeta analizada")
    except:
        traceback.print_exc(file=sys.stdout)
        print("No es posible acceder a la ruta. Proceso invalido.")
