##Ejer 2
##  Generar un programa que permita habilitar la cámara y seleccionar uno de los 3 filtros
#   posibles, cuando se selecciona un filtro la pantalla de la cámara debe implementar el filtro
#   seleccionado. Utilizar programación orientada a objetos.
##################################################################################
import cv2
import numpy as np

def salt_and_pepper(image, salt_prob: float, pepper_prob: float):
    noisy_image = np.copy(image)

    # Sal
    num_salt = np.ceil(salt_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255  # Sal

    # Pimienta Saturacion de los pixeles, invirtiendo los valores, simulando un ruido feo en la imagen
    num_pepper = np.ceil(pepper_prob * image.size)#funcion numpy redondear valores de pixeles
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape] # valores randomicos en la matriz del frame
    noisy_image[coords[0], coords[1]] = 0  # Pimienta

    return noisy_image

def gaussian_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)

def to_hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def main():
    # Inicializa la captura de video desde la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    # Variables bandera de no usarse hasta llamarlos
    modo_grises = False
    aplicar_salt_pepper = False
    aplicar_gaussian_blur = False
    aplicar_hsv = False

    try:
        while True:
            # Captura frame a frame
            ret, frame = cap.read()

            if not ret:
                print("Error: No se pudo leer el frame.")
                break

            # Cambia la imagen a  grises si modo_grises es True
            if modo_grises:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Aplica el filtro de sal y pimienta si aplicar_salt_pepper es True
            if aplicar_salt_pepper:
                frame = salt_and_pepper(frame, salt_prob=0.02, pepper_prob=0.02)

            # Aplica el filtro de desenfoque gaussiano si aplicar_gaussian_blur es True
            if aplicar_gaussian_blur:
                frame = gaussian_blur(frame)

            # Aplica el filtro HSV si aplicar_hsv es True
            if aplicar_hsv:
                frame = to_hsv(frame)

            # Muestra la imagen en una ventana
            cv2.imshow('Video', frame)

            # Espera a que el usuario presione una tecla
            key = cv2.waitKey(1) & 0xFF

            # Cambia entre modo RGB y escala de grises
            if key == ord('g'):
                modo_grises = True#cambios de valor bandera
            elif key == ord('r'):
                modo_grises = False
            elif key == ord('p'):
                aplicar_salt_pepper = not aplicar_salt_pepper  # Activa o desactiva el filtro de sal y pimienta
            elif key == ord('o'):
                aplicar_gaussian_blur = not aplicar_gaussian_blur  # Activa o desactiva el desenfoque gaussiano
            elif key == ord('i'):
                aplicar_hsv = not aplicar_hsv  # Activa o desactiva el filtro HSV
            elif key == 27:  # Tecla 'Esc' para salir
                break

    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")
    
    finally:
        # Libera la captura y cierra todas las ventanas
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":##programa dentro de un programa principal o importando,
    main()
