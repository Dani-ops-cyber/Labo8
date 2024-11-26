import cv2
import numpy as np

# Configuración de la cámara y grabación del video
def grabar_video(nombre_archivo="video_grabado.avi", duracion=10):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error al abrir la cámara.")
        return
    
    # Definir el códec y crear el objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(nombre_archivo, fourcc, 20.0, (640, 480))

    # Grabar video durante la duración especificada
    print("Grabando...")
    for _ in range(int(duracion * 20)):  # 20 FPS * duración
        ret, frame = cap.read()
        if not ret:
            print("No se pudo capturar el fotograma.")
            break
        out.write(frame)
    
    # Liberar los recursos
    cap.release()
    out.release()
    print(f"Video guardado como {nombre_archivo}")

# Reproducir el video
def reproducir_video(nombre_archivo="video_grabado.avi"):
    cap = cv2.VideoCapture(nombre_archivo)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Reproduciendo Video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Cambiar tamaño del video
def cambiar_tamano_video(nombre_archivo="video_grabado.avi", ancho=400, alto=600):
    cap = cv2.VideoCapture(nombre_archivo)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = cv2.resize(frame, (ancho, alto))
        cv2.imshow('Video Redimensionado', frame_resized)
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
        edges = cv2.Canny(frame, 100, 200)
        cv2.imshow('Detector de Bordes', edges)
        if cv2.waitKey(30) & 0xFF == ord('q'):
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
        mitad_izquierda = frame[:, :frame.shape[1] // 2]
        mitad_derecha = frame[:, frame.shape[1] // 2:]
        
        # Mostrar cada mitad en una ventana separada
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