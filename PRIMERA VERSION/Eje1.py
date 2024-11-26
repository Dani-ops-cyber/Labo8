## ejercicio 1
## 1. Cargue un vídeo con OpenCV y realice las siguientes operaciones:
#     • Reproducir el vídeo con OpenCV.
#     • Cambiar el tamaño del vídeo a 400x600 (ancho, alto).
#     • Crea un detector de bordes para el vídeo y muéstralo.
#     • Divida el vídeo en dos mitades y reprodúzcalo.
#     • Divida el vídeo en cuadrantes y reprodúzcalo mostrando los cuatro
#        cuadrantes.
######################################################################################
import cv2
import numpy as np

# Configuración de la cámara y grabación del video
def grabar_video(nombre_archivo="video_grabado.avi", duracion=10):#definimos en . avi por facilidad de tratamiento con open cv
    cap = cv2.VideoCapture(0)#utiliza la primera camara conectada
    if not cap.isOpened(): # verifica si se habilita la camarita
        print("Error al abrir la cámara.")
        return
    
    ## escrib
    fourcc = cv2.VideoWriter_fourcc(*'XVID')#comprime los fotogramas  a un video como tal usando codec XVID, el codec convierte el fotograma en .avi 
    out = cv2.VideoWriter(nombre_archivo, fourcc, 20.0, (640, 480))# Guarda el avi en un video de tamano de 640 por 480

    # Grabar video durante la duración especificada
    print("Grabando...")
    for _ in range(int(duracion * 20)):  # 20 FPS * duración 
        ret, frame = cap.read()#Funcion para leer el fotograma del video
        if not ret:
            print("No se pudo capturar el fotograma.")
            break
        out.write(frame)# escribir y guardar el fotograma 
    
    # liberacion de los recursos 
    cap.release() #cierra conexxion con camara
    out.release() #cierra el video y guarda bien
    print(f"Video guardado como {nombre_archivo}") #escribe mauuu

# Reproduce
def reproducir_video(nombre_archivo="video_grabado.avi"):
    cap = cv2.VideoCapture(nombre_archivo)#busca el archivo con la terminacion .avi
    while cap.isOpened():#al abrir el archivo hace lo siguiente
        ret, frame = cap.read()#lee el  video, lectura de fotograma, 
        if not ret:#si alguno de los fotogramas no funciona se lee el video se congela
            break
        cv2.imshow('Reproduciendo', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):#interrupcion por teclao
            break# sale del fotograma
    cap.release() # limpia
    cv2.destroyAllWindows()# cierra ventanas

# Cambiar tamaño del video
def cambiar_tamano_video(nombre_archivo="video_grabado.avi", ancho=400, alto=600):
    cap = cv2.VideoCapture(nombre_archivo)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = cv2.resize(frame, (ancho, alto))#reacondicionamiento del tamano
        cv2.imshow('Video Redimensionado', frame_resized)#muestra directamente la lectura de frames en tama;o dimensionado
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Aplicar detector de bordes al video
def detectar_bordes_video(nombre_archivo="video_grabado.avi"):
    cap = cv2.VideoCapture(nombre_archivo)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        edges = cv2.Canny(frame, 100, 200)# canny es un metodo de segmetacion para detectar bordes
        cv2.imshow('Detector de Bordes', edges) # muestra en una ventana los fotogramas  segmentaos
        if cv2.waitKey(30) & 0xFF == ord('q'):#Si se presiona la letra q 
            break
    cap.release()
    cv2.destroyAllWindows()

# Dividir el video en dos mitades y mostrarlas en ventanas separadas
def dividir_mitad_video(nombre_archivo="video_grabado.avi"):
    cap = cv2.VideoCapture(nombre_archivo)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Dividir el fotograma en mitades izquierda y derecha
        mitad_izquierda = frame[:, :frame.shape[1] // 2]# divide la imagen en mitad usando logica de matrices
        mitad_derecha = frame[:, frame.shape[1] // 2:]#guarda en las variables las dos mitades para poder mostrarlaspor separado
        
        # ventana separadas muestran los fotogramas
        cv2.imshow('Mitad Izquierda', mitad_izquierda)
        cv2.imshow('Mitad Derecha', mitad_derecha)
        
        # Salir con 'q'
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Dividir el video en cuadrantes y mostrarlos en ventanas separadas
def dividir_cuadrantes_video(nombre_archivo="video_grabado.avi"):
    cap = cv2.VideoCapture(nombre_archivo)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        alto, ancho = frame.shape[:2]
        
        # Dividir el fotograma en cuatro cuadrantes
        cuadrante_1 = frame[:alto // 2, :ancho // 2]  # Superior izquierdo
        cuadrante_2 = frame[:alto // 2, ancho // 2:]  # Superior derecho
        cuadrante_3 = frame[alto // 2:, :ancho // 2]  # Inferior izquierdo
        cuadrante_4 = frame[alto // 2:, ancho // 2:]  # Inferior derecho
        
        # Mostrar cada cuadrante en una ventana separada
        cv2.imshow('Cuadrante 1 (Superior Izquierdo)', cuadrante_1)
        cv2.imshow('Cuadrante 2 (Superior Derecho)', cuadrante_2)
        cv2.imshow('Cuadrante 3 (Inferior Izquierdo)', cuadrante_3)
        cv2.imshow('Cuadrante 4 (Inferior Derecho)', cuadrante_4)
        
        # Salir con 'q'
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Menú de opciones
def menu():
    grabar_video()
    while True:
        print("\nMenú de opciones:")
        print("1. Reproducir el vídeo")
        print("2. Cambiar el tamaño del vídeo a 400x600")
        print("3. Aplicar detector de bordes y mostrar el vídeo")
        print("4. Dividir el vídeo en dos mitades y reproducir en ventanas separadas")
        print("5. Dividir el vídeo en cuadrantes y reproducir en ventanas separadas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            reproducir_video()
        elif opcion == '2':
            cambiar_tamano_video()
        elif opcion == '3':
            detectar_bordes_video()
        elif opcion == '4':
            dividir_mitad_video()
        elif opcion == '5':
            dividir_cuadrantes_video()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
