import fileinput


allLines = []
for line in fileinput.input():
    allLines.append(line.strip())

numAsig = 0
numProf = 0
numAlum = 0
numAyud = 0
errorFlag = False

while len(allLines) > 0:
    try:
        if(allLines[0].split(' ')[0] != 'Asignatura'):
            errorFlag = True
            break
        else:
            if(len(allLines[0].split(' ')) < 2):
                errorFlag = True
                break
            numAsig += 1
            allLines.pop(0)
            if(allLines[0].split(' ')[0] == 'Asignatura' or allLines[0].split(' ')[0] == 'Ayudante'):
                errorFlag = True
                break
            else:
                numProf += 1
                allLines.pop(0)
                while len(allLines) > 0 and allLines[0].split(' ')[0] != 'Asignatura' and allLines[0].split(' ')[0] != 'Ayudante':
                    numAlum += 1
                    allLines.pop(0)
                if len(allLines) > 0 and allLines[0].split(' ')[0] == 'Ayudante':
                    if(len(allLines[0].split(' ')) < 2):
                        errorFlag = True
                        break
                    numAyud += 1
                    allLines.pop(0)
    except:
        errorFlag = True

if errorFlag:
    print('ERROR EN EL ARCHIVO')
else:
    if(numAsig == 1):
        print(str(numAsig) + ' asignatura')
    else:
        print(str(numAsig) + ' asignaturas')

    if(numProf == 1):
        print(str(numProf) + ' profesor')
    else:
        print(str(numProf) + ' profesores')

    if(numAlum == 1):
        print(str(numAlum) + ' alumno')
    else:
        print(str(numAlum) + ' alumnos')

    if(numAyud == 1):
        print(str(numAyud) + ' ayudante')
    else:
        print(str(numAyud) + ' ayudantes')
