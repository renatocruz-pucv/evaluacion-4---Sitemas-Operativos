; Script para el instalador del programa FileHash CLI Tool
; [cite_start]Cumple con los requisitos de la EV4: Instalador EXE/MSI, añade al PATH[cite: 40].

[Setup]
; Información General del Instalador
AppName=FileHash CLI Tool
AppVersion=1.0.0
DefaultDirName={autopf}\FileHashCLI
DefaultGroupName=FileHash CLI
OutputBaseFilename=filehash-installer-1.0.0
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

; Archivo de salida (El instalador .exe)
OutputDir=.\InstallerOutput
UninstallDisplayIcon={app}\filehash.exe
; SetupIconFile=.\filehash.ico ; Opcional: si tienes un icono

[Files]
; RUTA CORRECTA para GitHub Actions
Source: "dist\filehash.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Crea un atajo en el menú de inicio
Name: "{group}\FileHash CLI Tool"; Filename: "{app}\filehash.exe"

[Run]
; CUMPLIMIENTO DE REQUISITO: Añade la ruta de instalación al PATH de Windows.
; [cite_start]Esto permite ejecutar 'filehash --version' desde cualquier terminal[cite: 40, 41].
Filename: "{sys}\setx.exe"; Parameters: "PATH ""{app};%PATH%"""; Flags: runhidden
; CUMPLIMIENTO DE REQUISITO: Ejecuta el comando de verificación post-instalación.
Filename: "{app}\filehash.exe"; Parameters: "--version"; WorkingDir: "{app}"; Flags: postinstall skipifsilent