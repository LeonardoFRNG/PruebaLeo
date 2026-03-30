import csv

def save_csv(data, ruta="data.csv"):
    if len (data) == 0:
        print("There are no students to save.")
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["identificator", "name", "age", "course", "state"]) #estev es el encabezado
            for students in data:
                writer.writerow([students['identificator'], students['name'], students['age'], students['course'], students['state']])
        print(f"Data saved at {ruta}")
    except:
        print("Error saving file.")
        
