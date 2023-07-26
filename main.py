# This is a sample Python script.
import datetime

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import json


def create_json_structure():
    dictionary = {
        "projectFileVersion": "{}".format(datetime.datetime.today().date()),
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
            "classes": []
        },
        "documents": []
    }
    return dictionary

def parse_xls(nombre_archivo,dicionario):
    df = pd.read_excel(nombre_archivo)
    for index in df.index:
        print("{} {}".format(index, df["Razón LTR"][index]))
        f = open("Archivos entrenamiento\{}.txt".format(index),"w")
        f.writelines(df["Razón LTR"][index])

        f.close()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dictionary = create_json_structure()
    parse_xls('Detractores 2018.xlsx',dictionary)
    # dictionary = create_json_structure()
    # json_object = json.dumps(dictionary, indent=4)
    # with open("sample.json", "w") as outfile:
    #     outfile.write(json_object)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
