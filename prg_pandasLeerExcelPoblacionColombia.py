import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo excel
archivoExcel=pd.read_excel('PoblacionAreaColombia.xlsx')
dep= archivoExcel['Departamento']
pob= archivoExcel['Poblacion']
area= archivoExcel['Area']

def area_col():
    total_area=archivoExcel['Area'].sum()
    return total_area

def prom_pers_d():
    total_p= archivoExcel['Poblacion'].sum()
    prom_p= total_p/len(dep)
    return prom_p

def prom_area_d():
    prom_d= area_col()/len(dep)
    return prom_d

def numero_mayor():
    d_mayor=0
    for x in range(len(dep)):
        index_d= archivoExcel.loc[x,'Poblacion']
        if index_d>d_mayor:
            d_mayor=index_d
    return d_mayor

def numero_menor():
    d_menor= numero_mayor()
    for i in range(len(dep)):
        index_d2= archivoExcel.loc[i,'Poblacion']
        if index_d2<d_menor:
            d_menor=index_d2
    return d_menor

def nombre_mayor():
    d_mayor=0
    for x in range(len(dep)):
        index_d= archivoExcel.loc[x,'Poblacion']
        index_n= archivoExcel.loc[x,'Departamento']
        if index_d>d_mayor:
            d_mayor=index_d
            nombre_M=index_n
    return nombre_M

def nombre_menor():
    d_menor= numero_mayor()
    for m in range(len(dep)):
        index_d2= archivoExcel.loc[m,'Poblacion']
        index_n= archivoExcel.loc[m,'Departamento']
        if index_d2<d_menor:
            d_menor=index_d2
            nombre_m=index_n
    return nombre_m

print("El area total de Colombia es: %i km2"%(area_col()))
print("El promedio de area por departamento es: %i km2"%(prom_area_d()))
print("El departamento con mayor poblacion es: %s con %i habitantes"%(nombre_mayor(),numero_mayor()))
print("El departamento con menor poblacion es: %s con %i habitantes"%(nombre_menor(),numero_menor()))
print("El promedio de poblacion por departamento es: %i p/km2"%(prom_pers_d()))

fig, ax = plt.subplots() 
ax.set_title("Departamento y Poblacion", fontdict = {'fontsize':18, 'color':'tab:purple'})
ax.set_xlabel('Departamento')
ax.set_ylabel("Poblacion")
plt.bar(archivoExcel['Departamento'],archivoExcel['Poblacion'])
plt.show()

fig, ax= plt.subplots()
ax.set_title("Departamento y Area", fontdict = {'fontsize':18, 'color':'tab:purple'})
ax.set_xlabel("Departamento")
ax.set_ylabel("Area")
plt.bar(archivoExcel['Departamento'],archivoExcel['Area'])
plt.show()

fig, ax= plt.subplots()
ax.set_title("Departamento y Poblacion", fontdict = {'fontsize':18, 'color':'tab:purple'})
ax.set_ylabel("Departamento")
ax.set_xlabel("Poblacion")
plt.barh(archivoExcel['Departamento'],archivoExcel['Poblacion'])
plt.show()

fig, ax= plt.subplots()
ax.set_title("Departamento y Area", fontdict = {'fontsize':18, 'color':'tab:purple'})
ax.set_ylabel("Departamento")
ax.set_xlabel("Area")
plt.barh(archivoExcel['Departamento'],archivoExcel['Area'])
plt.show()

fig, ax= plt.subplots()
ax.set_title("Departamento y Poblacion", fontdict = {'fontsize':18, 'color':'tab:purple'})
plt.pie(archivoExcel['Poblacion'],labels=archivoExcel['Departamento'])
plt.show()

fig, ax= plt.subplots()
ax.set_title("Departamento y Area", fontdict = {'fontsize':18, 'color':'tab:purple'})
plt.pie(archivoExcel['Area'],labels=archivoExcel['Departamento'])
plt.show()