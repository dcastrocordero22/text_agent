import csv
from string import punctuation, digits 
STOPWORDS = {
    "la", "el", "y", "es", "un", "una", "de", "que", "en", "a", "por", "con"
}

class TextAgent:
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo
        self.frecuencias = {}
        self.lineas = self.leer_textos_csv()
        textos = self.separa_lineas()
        textos = self.normalizar_textos(textos)
        self.construye_diccionario_frecuencias(textos)

    #Lee el archivo con los texts 
    def leer_textos_csv(self):
        lineas= []
        with open(self.ruta, encoding= 'utf-8') as archivo:
            lineas = archivo.read().splitlines()
        return lineas[1:]

    #separa las lineas en dos partes y retorna una lista de palabras eliminando el id 
    def separa_lineas (self):
        textos=[]
        for linea in self.lineas: 
            partes = linea.split(",",1)
            textos.append(partes[1])
        return textos

    #noramaliza los textos cambiando palabras a minúscula y eliminando signos de puntuación
    def normalizar_textos (self,lista):
        lista_normalizada = []
        for oracion in lista:
            texto_nomralizado = oracion.lower().translate(str.maketrans("","",punctuation + digits ))
            lista_normalizada.append(texto_nomralizado)
        return lista_normalizada



    #dada una lista crea un diccionario cuya llave es la palabra y el valor la cantidad de veces que aparece la palabra recibe la oracion y el diccionario donde deja las frecuencias
    def construir_frecuencia_palabras(self,lista):
        #obtiene todas las palabra
        lista = lista.split()
        #crea el diccionario
        
        for palabra in lista:
            if palabra not in STOPWORDS:
                if palabra in self.frecuencias:
                    self.frecuencias[palabra] += 1
                else:
                    self.frecuencias[palabra] = 1
       
    # dada una lista de oraciones construye un diccionario 
    def construye_diccionario_frecuencias(self,lista_oraciones):
        for oracion in lista_oraciones:
           self.construir_frecuencia_palabras(oracion)
        
    # ordena los itmes de un diccionario por frecuencia de aparicion 

    def ordenar_por_frecuencia(self, descendente=True):
        return sorted(
            self.frecuencias.items(),
            key=lambda x: x[1],
            reverse=descendente
        )
    #retorna las n palabras mas comunes
    def top_palabras(self,n):
        ordenadas= self.ordenar_por_frecuencia()
        return ordenadas[:n]
    #retorna las frecuencia de una palabra especifica si no existe retorna none
    def frecuencia_palabra(self,palabra):
        return self.frecuencias.get(palabra.lower())
    # retorna la cantidad de palabras distitas encoentradas en el archivo
    def total_palabras_distintas(self):
        return len(self.frecuencias) 
    # retorna la cantidad de tokenss o palabras procesadas excluye los stopwords
    def total_palabras_procesadas(self):
        return sum(self.frecuencias.values()) 





if __name__ == "__main__":
    agent = TextAgent("data/input.csv")
    top = agent.top_palabras(5)
    print(top)
    top= agent.frecuencia_palabra("Verdader")
    print(top)
    top=agent.total_palabras_distintas()
    print(top)
    top=agent.total_palabras_procesadas()
    print(top)