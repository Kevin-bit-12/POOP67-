import time

def guardar_lectura(temperatura, humedad, nombre_archivo="lecturas.txt"):
    linea = "Temp: " + str(temperatura) + " C, Humedad: " + str(humedad) + " %, Tiempo: " + time.ctime() + "\n"
    archivo = open(nombre_archivo, "a")
    archivo.write(linea)
    archivo.close()
    print("Lectura guardada en", nombre_archivo)

def leer_archivo(nombre_archivo="lecturas.txt"):
    print("\nContenido del archivo", nombre_archivo)
    try:
        archivo = open(nombre_archivo, "r")
        contenido = archivo.read()
        archivo.close()
        print(contenido)
    except FileNotFoundError:
        print("El archivo no existe todavía.")

if __name__ == "__main__":
    guardar_lectura(25, 50)
    time.sleep(1)
    guardar_lectura(26, 55)
    time.sleep(1)
    guardar_lectura(27, 60)

    leer_archivo()
