# This is a sample Python script.
import datetime

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import json
import numpy as np

def create_json_structure():
    dictionary = {
        "projectFileVersion": "2022-05-01",
        "stringIndexType": "Utf16CodeUnit",
        "metadata": {
            "projectKind": "CustomMultiLabelClassification",
            "storageInputContainerName": "example-data",
            "projectName": "Encuestas",
            "multilingual": False,
            "description": "Project-description",
            "language": "en",
            "settings": {}
        },
        "assets": {
            "projectKind": "customMultiLabelClassification",
            "classes": [],
            "documents": []
        },

    }
    return dictionary

def add_file_classifcation(index,clase1, clase2, clase3):
    def add_file_classes(clase1, clase2, clase3):
        lista = []

        if clase1 is not None:
            lista.append({"category": "{}".format(clase1)})
        if clase2 is not None:
            lista.append({"category": "{}".format(clase2)})
        if clase3 is not None:
            lista.append({"category": "{}".format(clase3)})
        return lista
    json_part = {
        "location": "{}.txt".format(index),
        "language": "es-es",
        "classes": []
      }
    lista = add_file_classes(clase1, clase2, clase3)

    json_part["classes"] = lista

    return json_part

def parse_xls(nombre_archivo,dicionario):
    conjunto_clases = set()
    lista_caracteres_reemplazar = [":","$","&","%","*","(",")","+","?","~","#","/","?"]
    df = pd.read_excel(nombre_archivo)
    df = df.replace(np.nan, None)
    for index in df.index:
        # if index <=50:
        lista_clases = [df["Nivel 3"][index]]
        if lista_clases[0] is not None:
            # = 'nan' and lista_clases[1] != 'nan' and lista_clases[2] != 'nan'
            f = open("Archivos entrenamiento/{}.txt".format(index), "w")
            print(df["Razón LTR"][index])
            f.writelines(df["Razón LTR"][index])
            f.close()
            print(lista_clases)
            for i in range(0, len(lista_clases)):
                for carcater in lista_caracteres_reemplazar:
                    lista_clases[i] = lista_clases[i].replace(carcater, "-")
                print(lista_clases[i])
                lista_clases[i] = lista_clases[i][0:49]
            print(lista_clases)

            dicionario["assets"]["documents"].append(add_file_classifcation(index, None, None, lista_clases[0]))
            conjunto_clases.add(lista_clases[0])
            print("------------------------------------")
    for elemento in conjunto_clases:
        print(elemento)
        dicionario["assets"]["classes"].append({"category": "{}".format(elemento)})
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dictionary = create_json_structure()
    parse_xls('Detractores 2018.xlsx', dictionary)
    with open("sample.json", "w") as outfile:
         json.dump(dictionary, indent=4, fp=outfile, ensure_ascii=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
