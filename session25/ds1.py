#ETL : Extract Transform Load

import pandas as pd

#Extraer
salarios = pd.read_csv('salaries.csv') #dataframe

#explorar
print(salarios.head())


print(salarios.info())

print("Media de salarios:", salarios['BasePay'].mean())

print(salarios[salarios['EmployeeName'] == 'NATHANIEL FORD']['JobTitle'])

print(salarios.groupby('Year').mean()['BasePay'])

def chief_string(title: str) -> bool:
    if 'chief' in title.lower():
        return True
    else:
        return False

print("Sumatorio:", sum(salarios['JobTitle'].apply(lambda x: chief_string(x))))

salarios['longitud_titulo'] = salarios['JobTitle'].apply(len)

print(salarios.tail(10))
