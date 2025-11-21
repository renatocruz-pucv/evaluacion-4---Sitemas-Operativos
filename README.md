## FileHash CLI Tool - Empaquetado y CI/CD

Esta herramienta de línea de comandos (CLI) permite generar un checksum SHA-256 para cualquier archivo, y se distribuye como un instalador nativo de Windows.

1. Guía de Instalación y Uso

La aplicación se ha empaquetado para Windows utilizando PyInstaller e Inno Setup, lo que asegura una instalación profesional y la adición automática al PATH del sistema.

2. Instalación (Vía Artefacto CI/CD)

Diríjase a la pestaña Releases de este repositorio.

Descargue el archivo filehash-installer-1.0.0.exe de la última versión exitosa (Ejemplo: v1.0.8).

Ejecute el instalador. El programa se instalará en C:\Program Files (x86)\FileHashCLI.

Abra una nueva terminal (CMD o PowerShell).

3. Verificación del PATH

Para confirmar que la aplicación se añadió correctamente al PATH global de Windows, ejecute:  filehash --version

4. Uso de la Herramienta (SHA-256)

Para generar el checksum de cualquier archivo, use el siguiente comando:  filehash C:\ruta\completa\a\tu\archivo.txt

5. Desinstalación

La herramienta se puede desinstalar de manera segura a través de la opción estándar de Windows: Panel de Control > Agregar o quitar programas.

6. Matriz de Pruebas y CI/CD (Verificable)

7. Automatización CI/CD

El proceso de build y publicación está completamente automatizado a través de GitHub Actions, garantizando la reproducibilidad y la integridad del instalador. El pipeline se activa con cada nuevo Release publicado.

Prueba de Éxito del Pipeline (CI/CD):

El siguiente registro demuestra la ejecución completa, generación de checksums y publicación de artefactos en la Release v1.0.8.
