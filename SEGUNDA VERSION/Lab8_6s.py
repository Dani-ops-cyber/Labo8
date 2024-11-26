import cv2
import os

class ImageCapture:
    def __init__(self, output_dir="Capturas"):
        self.output_dir = output_dir
        self.image_count = 1
        os.makedirs(self.output_dir, exist_ok=True)
    
    def capture_image(self):
        # Inicializar la webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: No se pudo abrir la cámara.")
            return

        print("Presiona 'f' para capturar una imagen o 'q' para salir.")
        while True:
            # Leer un cuadro de la cámara
            ret, frame = cap.read()
            if not ret:
                print("Error: No se pudo capturar el cuadro.")
                break

            # Mostrar el cuadro en pantalla
            cv2.imshow("Presiona 'f' para capturar, 'q' para salir", frame)

            # Esperar a que se presione una tecla
            key = cv2.waitKey(1) & 0xFF
            if key == ord('f'):  # Capturar la imagen si se presiona 'f'
                image_path = os.path.join(self.output_dir, f"imagen{self.image_count}.jpg")
                cv2.imwrite(image_path, frame)
                print(f"Imagen guardada en: {image_path}")
                self.image_count += 1
                cap.release()
                cv2.destroyAllWindows()
                return image_path
            elif key == ord('q'):  # Salir si se presiona 'q'
                break

        # Liberar recursos
        cap.release()
        cv2.destroyAllWindows()
        return None

    def detect_and_draw_contours(self, image_path):
        # Cargar la imagen en escala de grises
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detectar los contornos
        _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dibujar los contornos en la imagen original
        contour_image = image.copy()
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Dibuja en color verde

        # Mostrar la imagen con contornos
        cv2.imshow("Contornos detectados", contour_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def process(self):
        image_path = self.capture_image()
        if image_path:
            self.detect_and_draw_contours(image_path)

# Ejecución del proceso
if __name__ == "__main__":
    capturer = ImageCapture()
    capturer.process()
