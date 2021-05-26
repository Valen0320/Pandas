import pandas as pd

df_archivoExcel= pd.read_excel('ventas_productos_1.xlsx',index_col="Producto")
df_archivoExcel= df_archivoExcel[:10].copy()
print(df_archivoExcel)

# Grafica Vertical
df_archivoExcel.plot(kind='bar')

# Grafica horizontal
df_archivoExcel.plot(kind='barh')

# Ocupar todo el espacio
df_archivoExcel.plot(kind='barh', width=1) # Cada grupo de barras ocupa todo el espacio

# Grozor de las barras
df_archivoExcel.plot(kind='barh', width=3)

# Grafica Apilada
df_archivoExcel.plot(kind='bar',
                     stacked= 'True',       # Muestra las barras apiladas
                     alpha= 0.4,        # Nivel de transparencia
                     width= 0.9,        # Grosor de las barras para dejar 
                     figsize=(9,4));

# Grafico por una medalla
df_archivoExcel.plot(kind='bar',
                     width=0.8,
                     )