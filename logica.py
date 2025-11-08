from probador_orange_hrm import ProbadorOrangeHRM
import asyncio
import json

class Logica:

    def __init__(self):
        # Cargar archivo json de parametros a probar
        with open('pruebas_a_realizar.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        self.probador_orange = ProbadorOrangeHRM()
        asyncio.run(self.probador_orange.run(datos))

if __name__ == "__main__":
    app = Logica()

