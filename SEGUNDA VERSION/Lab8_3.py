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

        # Capturar el cuadro
        ret, frame = cap.read()
        if ret:
            image_path = os.path.join(self.output_dir, f"imagen{self.image_count}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Imagen guardada en: {image_path}")
            self.image_count += 1
        else:
            print("Error: No se pudo capturar la imagen.")

        cap.release()
        return image_path if ret else None
    
    def apply_grayscale_and_quadrants(self, image_path):
        # Cargar la imagen en color
        color_image = cv2.imread(image_path)
        if color_image is None:
            print("Error: No se pudo cargar la imagen.")
            return

        # Convertir la imagen a escala de grises
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        height, width = gray_image.shape
        half_height, half_width = height // 2, width // 2

        # Dividir en cuadrantes
        quadrants = {
            "top_left": gray_image[:half_height, :half_width],
            "top_right": gray_image[:half_height, half_width:],
            "bottom_left": gray_image[half_height:, :half_width],
            "bottom_right": gray_image[half_height:, half_width:]
        }

        # Guardar cada cuadrante
        for name, quadrant in quadrants.items():
            quadrant_path = os.path.join(self.output_dir, f"{name}_{os.path.basename(image_path)}")
            cv2.imwrite(quadrant_path, quadrant)
            print(f"{name} guardado en: {quadrant_path}")

    def process(self):
        image_path = self.capture_image()
        if image_path:
            self.apply_grayscale_and_quadrants(image_path)

# Ejecución del proceso
if __name__ == "__main__":
    capturer = ImageCapture()
    capturer.process()
