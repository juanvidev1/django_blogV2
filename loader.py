import requests
import os
from cryptography.fernet import Fernet

LICENSE_SERVER_URL = "http://127.0.0.1:8001/get-key"  # URL del servidor de licencias
LICENSE_ID = "ridePro"  # ID de licencia del cliente

def get_encryption_key():
    """Obtiene la clave de encriptación del servidor de licencias."""
    response = requests.post(LICENSE_SERVER_URL, json={"license_id": LICENSE_ID})
    if response.status_code == 200:
        return response.json()["key"]
    else:
        raise Exception("No se pudo obtener la clave de encriptación. Verifique su licencia.")

# Obtiene la clave de encriptación del servidor
encryption_key = get_encryption_key()
cipher_suite = Fernet(encryption_key.encode())

ENCRYPTED_APP_PATH = "blog"  # Ruta de la app encriptada

def load_and_exec_encrypted_module(file_path):
    """Desencripta y ejecuta un módulo encriptado."""
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    # Desencripta el contenido
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Ejecuta el código desencriptado en el contexto de globals()
    exec(decrypted_data, globals())

def load_encrypted_app(app_path):
    """Carga todos los archivos .py.enc en el directorio de la app Django."""
    for root, dirs, files in os.walk(app_path):
        for file in files:
            if file.endswith(".py.enc"):
                file_path = os.path.join(root, file)
                load_and_exec_encrypted_module(file_path)

# Ejecuta los archivos encriptados
if __name__ == "__main__":
    load_encrypted_app(ENCRYPTED_APP_PATH)
    print("Aplicación Django cargada y desencriptada.")
