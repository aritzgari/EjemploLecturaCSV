# Imports
import pandas as pd

# Lectura y comprobación de datos
datos = pd.read_csv(
    "/home/aritz/Público/csv_a_html/Pruebas.csv", sep=";", engine="python")

# Renombrar columnas
dict = {'Europe/Madrid_datetime': 'datetime', 'Rodion 1, tachometer pulses': 'tachometer1', 'Rodion 1, temperature': 'temperature1',
        'Rodion 2, tachometer pulses': 'tachometer2', 'Rodion 2, temperature': 'temperature2', 'Rodion 3, tachometer pulses': 'tachometer3', 'Rodion 3, temperature': 'temperature3'}
datos.rename(columns=dict, inplace=True)

# cambiar tipo de dato object a datetime
datos['datetime'] = pd.to_datetime(
    datos['datetime'], format='%d/%m/%Y %H:%M:%S')

# set timestamp as index
datos = datos.set_index('timestamp')

# Eliminación de datos vacios
datos = datos.dropna()

# Dropear minutos duplicados
datos['datetime'] = datos['datetime'].dt.floor('Min')
datos = datos.drop_duplicates(subset=['datetime'])

# dropear datos de 0
datos = datos[datos.tachometer1 != 0.0]

print(datos)

