def cargar_datos(ruta_archivo:str)->list:
    congresistas=[]
    with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
        archivo.readline().strip().split(',')
        #print(titulos)
        linea = archivo.readline().strip()
        while len(linea) > 0:
            aux = True
            datos = linea.split(',')
            for x in range(len(congresistas)):
                if congresistas[x]['congresista'] == datos[0]:
                    congresistas[x]['asistencia'][datos[3]] = datos[4]
                    aux = False
            if aux:
                congresista = {}
                congresista['congresista'] = datos[0]
                congresista['movimiento'] = datos[1]
                congresista['circunscripcion'] = datos[2]
                congresista['asistencia'] = {datos[3]:datos[4]}
                congresistas.append(congresista)
            linea = archivo.readline().strip()
    return congresistas



ruta = 'C:\\Users\\Steve\\Downloads\\asistencia_congreso_v2.csv'
lista_c = cargar_datos(ruta)

def mas_inasistencias(congresista:list)->str:

    faltas=[]
    for con in lista_c:
        asistencia=0
        for y in con["asistencia"]:
            if con["asistencia"][y]=="SIN EXCUSA":
                asistencia+=1
        faltas.append(asistencia)        
    
    posicion=faltas.index(max(faltas))
    return lista_c[posicion]["congresista"]," falto ",faltas[posicion],"de forma injustificada",


def mas_asistencias(congresista:list)->str:
    asistencias=[]
    for congre in lista_c:
        asistencia=0
        for y in congre["asistencia"]:
            if congre["asistencia"][y]=="ASISTIÓ":
                asistencia+=1
                
        asistencias.append(asistencia)
    posicion=asistencias.index(max(asistencias))
    
    return "el congresista",lista_c[posicion]["congresista"],"asistio",asistencias[posicion],"veces a sesiones de la Cámara de Representantes" 



def porcentaje_asistencias(lista_c:list)->list:
   porcentajes=[]
   asistencias=[]
   for congre in lista_c:
        asistencia=0
        for y in congre["asistencia"]:
            if congre["asistencia"][y]=="ASISTIÓ":
                asistencia+=1
        asistencias.append(asistencia)
   for porce in range(len(asistencias)):
        porcentaje=round(asistencias[porce]/len(lista_c[porce]["asistencia"]),2)
        porcentajes.append({
            "nombre":lista_c[porce]["congresista"],
            "porcentaje_asistencia": porcentaje
        })
   return porcentajes

      

def Circunscripción_con_más_fallas(asistencia:list)->str:
    circu=[]
    faltas_circu=[]
    faltas = []
    for con in lista_c:
        asistencia=0
        for y in con["asistencia"]:
            if not (con["asistencia"][y]=="ASISTIÓ"):
                asistencia+=1
        faltas.append(asistencia)
    for x in range(len(lista_c)):
        if lista_c[x]["circunscripcion"] in circu:
            faltas_circu[circu.index(lista_c[x]["circunscripcion"])] += faltas[x]
        else:
            circu.append(lista_c[x]["circunscripcion"])
            faltas_circu.append(faltas[x])
    posicion = faltas_circu.index(max(faltas_circu))
    return "La circunscripción {} acumuló {}".format(circu[posicion],faltas_circu[posicion])

#print(Circunscripción_con_más_fallas(lista_c))

def mas_inasistencias_excusa_medica(lista_c:list)->str:
    faltas_medicas=[]
    for con in lista_c:
        asistencia=0
        for y in con["asistencia"]:
            if con["asistencia"][y]=="EX. MÉDICA":
                asistencia+=1
        faltas_medicas.append(asistencia)        
    
    posicion=faltas_medicas.index(max(faltas_medicas))
    return "El congresista",lista_c[posicion]["congresista"], "falló",faltas_medicas[posicion], "veces con excusa médica”."



def mas_X_inasistencias_7(lista_c:list,numero:int)->dict:
    faltas={}
    for congre in lista_c:
        asistencia=0
        for y in congre["asistencia"]:
            if congre["asistencia"][y]=="SIN EXCUSA" or congre["asistencia"][y]=="OTRAS EXCUSAS" or congre["asistencia"][y]=="EX. MÉDICA":
                asistencia+=1
        if asistencia > numero:
            faltas[congre["congresista"]]=asistencia
    return faltas

def asistencias_partido_veces(lista_c:list)->dict:
    
    pass
    
    

def mes_con_mas_sesiones(lista_c:list)->str:
    fechas = []
    cantidad = []
    for fecha in lista_c[0]["asistencia"]:
        aux=fecha[fecha.index("/")+1:len(fecha)]
        if aux in fechas:
            cantidad[fechas.index(aux)] += 1
        else:
            fechas.append(aux)
            cantidad.append(1)   
    posicion = cantidad.index(max(cantidad))
    return "En el mes {} hubo {} sesiones".format(fechas[posicion],cantidad[posicion])         
    
#print(mes_con_mas_sesiones(lista_c))

def promedio_asistencia_por_partido(lista_c:list)->dict:
    partidos = []
    promedio = {} #diccionario final
    for congre in lista_c:
        asistencia=0
        sesiones = 0
        aux = True
        for y in congre["asistencia"]:
            if congre["asistencia"][y]=="ASISTIÓ":
                asistencia+=1
            sesiones += 1
        for x in range(len(partidos)):
            if partidos[x]["movimiento"] == congre["movimiento"]:
                partidos[x]["cantidad_sesiones"] += sesiones
                partidos[x]["asistencias"] +=asistencia
                aux = False
        if aux:
            partidos.append({
                "movimiento":congre["movimiento"],
                "cantidad_sesiones": sesiones,
                "asistencias": asistencia
            })
    for x in partidos:
        promedio[x["movimiento"]] = round(x["asistencias"]/x["cantidad_sesiones"],2)
    return promedio

print(promedio_asistencia_por_partido(lista_c))

    
