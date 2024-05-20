; Script de Instalador NSIS para Aplicacion

; Configuración del instalador
SetCompressor /FINAL /SOLID lzma

; Define el nombre y la ubicación del instalador
Name "AplicacionInstalador"
OutFile "..\build\AplicacionInstalador.exe" ; Nombre del instalador

; Define el directorio de instalación predeterminado
InstallDir "$PROGRAMFILES\AplicacionInstalador"

; Define las páginas del instalador
!include "MUI2.nsh"

; Página de Bienvenida
!insertmacro MUI_PAGE_WELCOME

; Página de Licencia
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "..\src\license.txt"

; Página de Directorio
!insertmacro MUI_PAGE_DIRECTORY

; Página de Instalación
!insertmacro MUI_PAGE_INSTFILES

; Página Final
!insertmacro MUI_PAGE_FINISH

; Define las páginas del desinstalador
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; Define el idioma del instalador
!insertmacro MUI_LANGUAGE "Spanish"

; Define la sección de instalación
Section "Install"
  ; Establece el directorio de salida
  SetOutPath "$INSTDIR"

  ; Verificar si el archivo existe y eliminarlo
  IfFileExists "$INSTDIR\Aplicacion.exe" eliminar_exe no_existe

  eliminar_exe:
    Delete "$INSTDIR\Aplicacion.exe"
  no_existe:

  ; Copia el ejecutable principal desde el directorio de construcción
  File "..\build\Aplicacion\Aplicacion.exe" ; Asegúrate de que esta ruta es correcta y apunta al ejecutable de tu aplicación

  ; Crea el desinstalador
  WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

; Define la sección de desinstalación
Section "Uninstall"
  ; Elimina los archivos y directorios instalados
  Delete "$INSTDIR\Aplicacion.exe"
  Delete "$INSTDIR\uninstall.exe"
  RMDir /r "$INSTDIR"

  ; Elimina el directorio de instalación si está vacío
  RMDir "$INSTDIR"
SectionEnd
