import re
import csv

lista = []

with open("NACMAR.txt", "r", newline=None) as fd:
    for line in fd:
        line = line.replace("\n", "")
        salida_id = re.findall('[A-Z]{3}[0-9]{6}',line)
        lista.append(salida_id)
        salida_texto = re.findall('[A-Z]{3}[0-9]{6}(.*$)',line)
        lista.append(salida_texto)

print(lista)


file = open('nacmar.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file)
    write.writerow(["nacmar"]) 
    write.writerows(lista) 