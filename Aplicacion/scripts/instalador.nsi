; Script de Instalador NSIS para Aplicacion

; Configuración del instalador
SetCompressor /FINAL /SOLID lzma

; Define el nombre y la ubicación del instalador
Name "Aplicacion"
OutFile "..\build\Aplicacion\Aplicacion.exe"

; Define el directorio de instalación predeterminado
InstallDir "$PROGRAMFILES\Aplicacion"

; Define las páginas del instalador
!include "MUI2.nsh"
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "..\src\license.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
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

  ; Copia el ejecutable principal desde el directorio de construcción
 File "..\build\Aplicacion\Aplicacion.exe"

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
