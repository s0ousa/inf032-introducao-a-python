# 1.
resto = 10%3
print(resto)

#2
cont = 1 
while cont < 10:
    print('Tabudada 13 *', cont , cont*13)
    cont+=1

#3
meses = 4
semanas = meses *4
aulas = semanas*2
faltasPermitidas = 0.25*aulas
print('Faltas permitidas = ', faltasPermitidas)

#4
pi = 3.14
r = 2
areaDoCirculo = pi * r * r
print(areaDoCirculo)

#5
horas = 3
minutos = 23
segundos = 17

tempoEmSegundos = (horas*3600) + (minutos*60) + segundos
print(tempoEmSegundos)

#6
#aproveitando o codigo anterior ...
qulometrosPercorridos = 65
velocidadeMediaEmMetrosPorSegundo = (65*1000)/tempoEmSegundos
print(velocidadeMediaEmMetrosPorSegundo)

#7
import math

angulo = 80
anguloEmRadianos= math.radians(angulo)

seno = math.sin(anguloEmRadianos)
coseno = math.cos(anguloEmRadianos)
tang = math.tan(anguloEmRadianos)
secante = 1/coseno
cossec = 1/seno
cotang = 1/ tang


#8 
numero = 123
uni = numero%10
dez = ((numero%100) - uni )/10
print(dez)
cen = numero//100
print(cen) 
numeroInvertido = cen*100 + dez * 10 + uni
print(numeroInvertido)


#9

base = 10
altura =5

perimetro = (base*2) + (altura*2)
area = base*altura
diagonal = math.sqrt(base*base + altura*altura)

#10
a = 5
b = 12
a , b = b, a

print(a, b)

#11

gastoCerveja = 75 * 2.20
gastoMacarrao = 2 * 8.73
gastoMolho = 3.45
gastoCebola = 0.420*5.4
gastoAlho = 0.25*30
gastoPao = 0.45 * 25

valorDeCada = (gastoAlho + gastoMacarrao + gastoCerveja + gastoCebola + gastoMolho + gastoPao)/4

#12
volumeDoPoteSorvete = 15*10*13
volumeDeUmaBolinhaQueijo = 4*3.14*1.2*3

volumeDoPoteOcupadoPelasBolinhas = volumeDoPoteSorvete*0.74
quantidadeDeBolinhasQueCabem = volumeDoPoteOcupadoPelasBolinhas/volumeDeUmaBolinhaQueijo
print(quantidadeDeBolinhasQueCabem)