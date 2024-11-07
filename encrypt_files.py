import requests
from cryptography.fernet import Fernet
import os

# Configuración del servidor de licencias
LICENSE_SERVER_URL = "http://127.0.0.1:8001/get-key"  # URL del servidor de licencias
LICENSE_ID = "ridePro"  # ID de licencia del cliente

def get_encryption_key():
    """Obtiene la clave de encriptación del servidor de licencias."""
    response = requests.post(LICENSE_SERVER_URL, json={"license_id": LICENSE_ID})
    if response.status_code == 200:
        return response.json()["key"]
    else:
        raise Exception("No se pudo obtener la clave de encriptación. Verifique su licencia.")

# Obtiene la clave de encriptación desde el servidor de licencias
ENCRYPTION_KEY = get_encryption_key()
cipher_suite = Fernet(ENCRYPTION_KEY.encode())

# Ruta de la aplicación Django que quieres encriptar
APP_PATH = "blog"  # Cambia esto al nombre de tu aplicación Django

def encrypt_file(file_path):
    """Encripta un archivo Python (.py) usando la clave de encriptación proporcionada."""
    with open(file_path, "rb") as f:
        file_data = f.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    # Guarda el archivo encriptado con extensión .py.enc
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as ef:
        ef.write(encrypted_data)
    
    print(f"Archivo encriptado: {encrypted_file_path}")

def encrypt_app_directory(app_path):
    """Encripta todos los archivos .py en el directorio especificado de la aplicación Django."""
    for root, dirs, files in os.walk(app_path):
        for file in files:
            if file.endswith(".py") and not file.endswith("encrypt_django_app.py"):
                file_path = os.path.join(root, file)
                encrypt_file(file_path)

# Ejecuta el proceso de encriptación
if __name__ == "__main__":
    encrypt_app_directory(APP_PATH)
    print("Encriptación completada.")
