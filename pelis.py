import os              
import subprocess
archivo="tv_channels_rZGv5ADgeT_plus.m3u"
user="rZGv5ADgeT"
#urlreplace="http://arboltv.xyz:8080/series/eRgbH6Akxm/6R6tKqKbkj/"            
categoriabuskeda="ESTRENOS 2024"
#tituloreplace='? PELICULAS RETRO",'
#? ESTRENOS 2023",
# ? [ES] ESTRENOS 2024",
#categoria="Breaking Bad"
pathdestino="/home/samba/pelitmp/"
rutapeliculas="/home/samba/peliculas/"
rutaimagenes="/home/samba/imagenes/"
descarga="NO"
c=0
grupo=""
imagen=""
nombre=""
def limpiar(string):    
    string = string.replace('\rn', '')
    string = string.replace('\t', '')
    string = string.replace('\f', '')
    string = string.replace('\n', '')      
    string = string.replace('0A', '')              
    string_new = "".join(char for char in string if char.isalnum())    
    return string_new

with open(archivo, 'r') as f:
    for linea in f:        
        if c>0: 
            if descarga=="SI":
                if linea.find(user)>0:
                    print ("grupo",grupo)
                    print ("nombre",nombre)
                    print ("imagen",imagen)
                    print ("LINK",linea)
                    #DESCARGA PELICULA
                    pelicula = subprocess.Popen(["wget",linea,"--adjust-extension","-P",pathdestino], stdout=subprocess.PIPE)
                    output = pelicula.communicate()[0]                                   
                    contenido = os.listdir(pathdestino)
                    sw=1
                    for fichero in contenido:
                        sw=0
                        parte=fichero.split(".")    
                        rxten=limpiar(parte[1])
                        os.rename(pathdestino+fichero,rutapeliculas+nombre+"."+rxten)
                    if sw==0:
                        #DESCARGA IMAGEN
                        imagen = subprocess.Popen(["wget",imagen,"--adjust-extension","-P",pathdestino], stdout=subprocess.PIPE)
                        output = imagen.communicate()[0]                                   
                        contenido = os.listdir(pathdestino)
                        for fichero in contenido:
                            parte=fichero.split(".")    
                            os.rename(pathdestino+fichero,rutaimagenes+nombre+"."+parte[1])                    
            try:
                arra=linea.split("=")                
                grupo=arra[4]
                imagen=arra[3].replace('" group-title','').replace('"','')
                nombre=arra[2].replace('" tvg-logo','').replace('"','').replace("/","")
                existe=grupo.find(categoriabuskeda)
                if existe>0:
                    descarga="SI"
                else:    
                    descarga="NO"
            except:
                a=1 ��
��������c=c+1