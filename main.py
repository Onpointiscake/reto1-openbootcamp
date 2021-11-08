import pandas as pd

#Dado un fichero excel con nombres y correos (columna nombre y columna email), realiza un script en Python que devuelva los mails únicos de la columna email.
print(pd.read_excel('open-bootcamp.xlsx', usecols = ['Email']))