# Django Blog

Este blog sólo es un ejemplo para mostrar el funcionamiento del servidor de licencias. Todos los archivos de python están encriptados, así que no se puede modificar el código a menos que se modifique la app original y se vuelva a pasar por el encriptator. Tenemmos dos archivos clave:

- encrypt_files.py
- loader.py

## encrypt_files.py

Este archivo se encarga de encriptar los archivos del proyecto utilizando la llave de encriptación que se encuentra dentro del servidor de licencias, siempre y cuando la licencia se encuentre activa y sea válida. Es de un solo uso a menos que se requiera una encriptación constante. No es necesario mantenerlo aunque se recomienda no eliminarlo.

## loader.py

Este es el archivo clave ya que será en encargado de desencriptar todos los módulos de python en la app de django para que pueda correr de manera efectiva. Este archivo consulta al servidor de licencias y si es activa desencripta toda la aplicación, de lo contrario arroja un error y no permite la ejecución.

## manage.py

Dentro de blog se mantiene el archivo manage.py, pero con algunas variaciones. La principal es que ahora va a llamar a la función de desencriptación de la app para que esta pueda correr de fomra normal. La función se llama load_encrypted_app y recibe como parámetro el APP_PATH para el correcto funcionamiento de la misma.

# Correr la aplicación

Se hace de la manera tradicional ubicándose en la ruta donde se encuentra el archivo manage.py y se ejecuta el comando

```
python manage.py runserver
```

Si la licencia es válida y está activa la app debería correr con normalidad, de lo contrario debería arrojar un error indicando que la licencia no es válida o no está activa.
