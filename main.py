# Archivo a analizar
archivodatos = 'data.csv'


# Abro archivo y genero lista con contenido
def datosprimarios(file=archivodatos):
    datos = []
    with open(file) as f:
        next(f)
        for item in f:
            datos.append((list(item[:-1].split(','))))
    return datos


# Genero lista de países del archivo
def maestroPaises(datos):
    paises = []
    for i in datos:
        if i[3] not in paises:
            paises.append(i[3])
    return paises


# Genero lista de ciudades del archivo. Menú 3
def maestroCiudades(datos):
    ciudades = []
    for i in datos:
        if i[3] not in ciudades:
            ciudades.append(i[2])
    return ciudades


# Genero lista de Estudiantes. Menú 0 y 1
def buscaEst(tipo, seleccion, datos):
    if seleccion.isdigit() and int(seleccion) <= len(tipo):
        resultado = []
        if tipo == ciudades:
            resultado = [i[0:2] for i in datos
                         if i[2] == ciudades[int(seleccion)]]
        else:
            resultado = [i[0:2] for i in datos
                         if i[3] == paises[int(seleccion)]]
        return resultado
    else:
        return "Selección incorrecta"


# Estudiantes en un rango de edades. Menú 2
def consultaEdades(r1, r2, universo):
    listaEst = [i[0:2] for i in universo if int(i[4]) >= r1
                and int(i[4]) <= r2]
    return listaEst


# Promedio de edades por carrera. Menú 4
def calcularPromedios(datos):
    listEdadesCarrera = []
    listaCarreras = []
    listaCarrerasRepetidas = [i[5] for i in datos]
    for i in listaCarrerasRepetidas:
        if listaCarreras.count(i) < 1:
            listaCarreras.append(i)
    for ii in listaCarreras:
        listaEdades = [int(i[4]) for i in datos if i[5] == ii]
        promedioEdades = float(sum(listaEdades)/len(listaEdades))
        listEdadesCarrera.append([ii, promedioEdades])
    return listEdadesCarrera


# Lista de estudiantes con edades por encima y debajo del promedio. Menú 5
def listaEstEdad(carreras, datos):
    edadesCarrera = []
    for i in range(0, len(carreras)):
        edadesCarrera = [[carreras[i][0], ii[0] + " " + ii[1], 'encima']
                         if int(ii[4]) >= carreras[i][1]
                         and ii[5] == carreras[i][0]
                         else [carreras[i][0], ii[0] + " " + ii[1], 'debajo']
                         for ii in datos] + edadesCarrera
    return edadesCarrera


# Lista de estudiantes con edades por encima y debajo del promedio. Menú 6
def rangosEstEdad(datos):
    rangoEdades = []
    rangoEdades.append({"18-25": [[ii[0] + " " + ii[1]]
                                  for ii in datos
                                  if 18 <= int(ii[4]) and 25 >= int(ii[4])]})
    rangoEdades.append({"26-35": [[ii[0] + " " + ii[1]]
                                  for ii in datos
                                  if 26 <= int(ii[4]) and 35 >= int(ii[4])]})
    rangoEdades.append({"35 o más": [[ii[0] + " " + ii[1]]
                                     for ii in datos
                                     if 35 >= int(ii[4])]})
    return rangoEdades


# Promedio de edades por carrera. Menú 7
def ciudadCarreras(ciudades, datos):
    listaCarrera = []
    for i in ciudades:
        listaCiudadCarrera = []
        contador = 0
        for ii in datos:
            if ii[2] == i:
                if ii[5] not in listaCiudadCarrera:
                    contador += 1
                    listaCiudadCarrera.append(i)
        listaCarrera.append([i, contador])
    for i in listaCarrera:
        mayorCantidad = 0
        if i[1] > mayorCantidad:
            mayorCantidad = i[1]
            ciudadMayor = i[0]
    return ciudadMayor


# Menú de selección de ciudades y países
def menuCiudadPais(ciudades, paises):
    indiceCiudades = [i for i in range(len(ciudades))]
    indicePaises = [i for i in range(len(paises))]
    menuCiudad = ([str(indiceCiudades[i]) + ": " + ciudades[i]
                   for i in range(len(ciudades))])
    menuPais = ([str(indicePaises[i]) + ": " + paises[i]
                 for i in range(len(paises))])
    return menuCiudad, menuPais


# Respuesta en pantalla de listas
def impresion(respuesta):
    if respuesta == "Selección incorrecta":
        print("")
        print("Selección incorrecta")
        print("")
    else:
        print("")
        for i in respuesta:
            print(i)
        print("")


# Respuesta en pantalla de diccionarios
def impresionDict(respuesta):
    print("")
    for i in respuesta:
        for ii in (i.keys()):
            print(ii)
        b = i.values()
        for ii in b:
            for iii in ii:
                print(iii)
    print("")


universo = datosprimarios()
paises = maestroPaises(universo)
ciudades = maestroCiudades(universo)
menuCiudad, menuPais = menuCiudadPais(ciudades, paises)
promedioEdades = calcularPromedios(universo)

while True:
    print('0 - Estudiantes que pertenezcan a una ciudad dada.')
    print('1 - Estudiantes que vivan en un país dado.')
    print('2 - Estudiantes que estén dentro de un rango de edades dado.')
    print('3 - Ciudades de residencia de los estudiantes.')
    print('4 - Edad promedio por carrera.')
    print('5 - Estudiante por encima o por debajo del promedio de edad por carrera.')
    print('6 - Estudiantes en rangos de edad (18-25, 26-35, mayores de 35).')
    print('7 - Ciudad que tienen la mayor variedad de carreras universitarias.')
    print('8 - Salir.')
    consulta = input('Escoja un número de consulta: ')


# Verifico que la elección cumpla condición 0 a 7
    if consulta.isdigit():
        if int(consulta) in range(0, 9):
            consulta = int(consulta)
        else:
            continue
    else:
        continue


# Opción 0
    if consulta == 0:
        print(menuCiudad)
        indSelect = input('Elije el número índice de ciudad deseado: ')
        estudiantesCiudad = buscaEst(ciudades, indSelect, universo)
        impresion(estudiantesCiudad)


# Opción 1
    elif consulta == 1:
        print(menuPais)
        indSelect = input('Elije el número índice de país deseado: ')
        estudiantesPais = buscaEst(paises, indSelect, universo)
        impresion(estudiantesPais)


# Opción 2
    elif consulta == 2:
        print('Las edades a consultar incluyen los extremos')
        print('Usar el siguiente formato: 18-20')
        consulta = input('Ingrese el rango: ')
        # Valido información ingresada y ejecuto
        consulta = consulta.split('-')
        if len(consulta) == 2 and consulta[0].isdigit()\
              and consulta[1].isdigit():
            r1 = int(consulta[0])
            r2 = int(consulta[1])
            if r1 > r2:
                r1, r2 = r2, r1
            rangoEdades = consultaEdades(r1, r2, universo)
            print(f'Los estudiantes de entre {r1} y {r2} anos son:')
            impresion(rangoEdades)
        else:
            print('El rango indicado el el formato es inválido')


# Opción 3
    elif consulta == 3:
        print('Los estudiantes son de las siguiente ciudades:')
        impresion(ciudades)


# Opción 4
    elif consulta == 4:
        print('Las edades promedio por cada carrera son:')
        impresion(promedioEdades)


# Opción 5
    elif consulta == 5:
        print('Estudiantes por encima y debajo de edad promedio por cada carrera:')
        estudiantesXedad = listaEstEdad(promedioEdades, universo)
        impresion(estudiantesXedad)


# Opcion 6
    elif consulta == 6:
        edadexrango = rangosEstEdad(universo)
        impresionDict(edadexrango)


# Opcion 7
    elif consulta == 7:
        mayorCarrearas = ciudadCarreras(ciudades, universo)
        print("")
        print(f'La ciudad con mayor cantidad de carreras es: {mayorCarrearas}')
        print("")

# Opcion 8
    elif consulta == 8:
        break

    else:
        print('Error no contemplado')
        break
