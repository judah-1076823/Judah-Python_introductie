#Judah Rozendaal 1C
#Containers

geladen_containers = 287
#tijd nodig om te laden in minuten
totale_tijd_laden = 295

#gemiddelde tijd voor het laden van een container in minuten bereken
gemiddelde_tijd_per_container_laden = totale_tijd_laden / geladen_containers

geloste_containers = 331
#tijd nodig om te lossen in minuten
totale_tijd_lossen= 441

#gemiddelde tijd voor het lossen van een container in minuten berekenen
gemiddelde_tijd_per_container_lossen = totale_tijd_laden / geloste_containers

print(f"Gemiddeld zijn ze {gemiddelde_tijd_per_container_lossen} minuten bezig per container tijdens het lossen en {gemiddelde_tijd_per_container_laden} minuten tijdens het laden.\n")

#berekening 1
import math

x = 9.1

stap1 = (3 * x) - 1
stap2 = 1 + x
stap3 = (stap2)**2

y =  math.sqrt(stap1) + stap3
print(f'De waarde van y = {y} als x = {x}\n')

a = 0.87
b = 22.7
c = 5.03

stap1 = b**2
stap2 = 4 * a * c
stap3 = stap1 - stap2
stap4 = math.sqrt(stap3)
stap5 = -b + stap4

stap6 = 2 * a
stap7 = stap5 / stap6 

print(f'De waarde van y = is {stap7} als a = {a}, b = {b} en c = {c}.\n')

#berekening 2

#tijd in uur
t = 4
#lichtsnelheid in m/s
v = 179_875_474.8
#lichtsnelheid in m/s
c = 299_792_458

stap1 = v ** 2 
stap2 = c ** 2
stap3 = stap1 / stap2
stap4 = 1 - stap3
stap5 = v * stap4
stap6 = 1 / stap5
delta = t * stap6
delta == x

print(f'vanaf een komeet gezien zit u {x} uur op de tuinstoel.')
print(f'vanaf een komeet gezien zit u {x * 60.0} minuten op de tuinstoel.')
print(f'vanaf een komeet gezien zit u {x * (60.00 ** 2)} seconden op de tuinstoel.')