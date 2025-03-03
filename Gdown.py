import gdown

# Reemplaza 'FILE_ID' con el ID real del archivo en Google Drive
file_id = "1ek6gfuhp4Buuc8w3xiMy6JHyYIcs7m6a"
output = "dataset1.zip"  # Cambia la extensión si es otro tipo de archivo

# URL de descarga pública de Google Drive
url = f"https://drive.google.com/uc?id={file_id}"

# Descargar el archivo
gdown.download(url, output, quiet=False)

print(f"Archivo descargado: {output}")
