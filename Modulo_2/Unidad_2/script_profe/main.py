# 1) IMPORTAR LIBRERIAS
import pandas as pd
from matplotlib import pyplot as plt

# 2) CARGAR DATOS
dat = pd.read_excel("temperaturas.xlsx")
print(dat)
print(dat.dia)
print(dat.temperatura)

# ) GRAFICAR
x = dat.dia
y = dat.temperatura
plt.plot(x, y)
plt.show()
