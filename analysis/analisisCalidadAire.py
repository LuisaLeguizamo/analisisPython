import pandas as pd
import matplotlib.pyplot as plt

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #Creando un dataFrame
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=['comuna','ica','fecha','id'])
    dataFrameICA.to_csv('datosICA.csv',index=False)
    print(dataFrameICA)

    #Generando grafica de los datos de comuna
    datosOrdenadoPorComuna=dataFrameICA.groupby('comuna')['ica'].mean()
    plt.figure(figsize=(20,20))
    datosOrdenadoPorComuna.plot(kind='bar',color='pink')
    plt.show()

construirDataICA()