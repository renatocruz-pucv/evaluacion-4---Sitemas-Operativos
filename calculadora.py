import hashlib
import sys
import argparse

def calculate_sha256(filepath):
    """Calcula el hash SHA-256 de un archivo grande."""
    sha256 = hashlib.sha256()
    try:
        # Abre el archivo en modo binario ('rb')
        with open(filepath, 'rb') as f:
            # Lee el archivo en trozos para manejar archivos grandes eficientemente
            while True:
                chunk = f.read(4096) 
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None # Devuelve None si el archivo no existe
    except Exception as e:
        return f"Error de lectura: {e}"

def main():
    """Función principal del CLI, maneja los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Herramienta CLI para calcular el Hash SHA-256 de un archivo."
    )
    
    # Soporte para --version (requisito de verificación post-instalación) [cite: 41]
    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s 1.0.0', 
        help="Muestra la versión del programa."
    )

    # Argumento posicional para la ruta del archivo
    parser.add_argument(
        'ruta', 
        type=str, 
        help="Ruta completa al archivo cuyo hash SHA-256 se quiere calcular."
    )

    args = parser.parse_args()
    
    # Calcular el hash
    file_hash = calculate_sha256(args.ruta)

    if file_hash is None:
        # Sale con un mensaje de error si el archivo no se encuentra
        sys.exit(f"Error: Archivo no encontrado en la ruta: {args.ruta}")
    elif "Error de lectura" in str(file_hash):
        # Sale con un mensaje de error si hay un problema de permiso/lectura
        sys.exit(f"Error: {file_hash}")
    else:
        # Muestra el resultado
        print("-" * 50)
        print(f"ARCHIVO: {args.ruta}")
        print(f"HASH SHA-256: {file_hash}")
        print("-" * 50)

if __name__ == '__main__':
    main()