import cv2
import numpy as np
import time

class DetectorDeColor:
    def __init__(self):
        # Definir los rangos de colores en HSV y mensajes
        self.rangos = {
            'Verde': [(40, 100, 100), (80, 255, 255), "Rápido al 100"],
            'Azul': [(100, 100, 100), (140, 255, 255), "Velocidad media 25"],
            'Rojo': [(0, 100, 100), (10, 255, 255), "Parando el sistema"]
        }

    def detectar_color(self, hsv_frame):
        # Iterar por cada color y mostrar mensaje si se detecta
        for color, (lower, upper, mensaje) in self.rangos.items():
            mascara = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))
            if cv2.countNonZero(mascara) > 0:
                return mensaje
        return None

class Camara:
    def __init__(self):
        self.detector = DetectorDeColor()
        self.cap = cv2.VideoCapture(0)  # Inicia la cámara web
        self.tiempo_ultimo_mensaje = time.time()  # Marca de tiempo inicial

    def iniciar(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("No se pudo abrir la cámara.")
                break

            # Convertir el frame a HSV
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            #5 segundos desde el último mensaje
            if time.time() - self.tiempo_ultimo_mensaje >= 5:
                mensaje = self.detector.detectar_color(hsv_frame)
                if mensaje:
                    print(mensaje)
                    self.tiempo_ultimo_mensaje = time.time()  # Actualizar tiempo del último mensaje
            
            # Mostrar el frame
            cv2.imshow("Camara", frame)
            
            # Presionar 'q' para salir
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def liberar(self):
        self.cap.release()
        cv2.destroyAllWindows()

# Ejecutar el programa
if __name__ == "__main__":
    camara = Camara()
    camara.iniciar()
    camara.liberar()
