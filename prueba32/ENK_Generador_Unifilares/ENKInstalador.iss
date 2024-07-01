[Setup]
AppName=ENK Generador de Unifilares
AppVersion=1.0
DefaultDirName={pf}\ENK_Generador_Unifilares
DefaultGroupName=ENK_Generador_Unifilares
OutputBaseFilename=ENK_Generador_Unifilares_Installer
UninstallFilesDir={app}\Uninstall
OutputDir=.

[Files]
Source: "dist\ENK_Generador_Unifilares\ENK_Generador_Unifilares.exe"; DestDir: "{app}"
Source: "dist\ENK_Generador_Unifilares\_internal\*"; DestDir: "{app}\_internal"; Flags: recursesubdirs createallsubdirs
Source: "ENK_Generador_Unifilares\docs\ayuda\ManualUso.pdf"; DestDir: "{app}\docs"; Flags: recursesubdirs createallsubdirs
Source: "ENK_Generador_Unifilares\docs\LB.ENK_PY_Mangueras_v1.xml"; DestDir: "{app}\docs"; Flags: recursesubdirs createallsubdirs
Source: "ENK_Generador_Unifilares\images\*"; DestDir: "{app}\images"; Flags: recursesubdirs createallsubdirs
Source: "ENK_Generador_Unifilares\licenses\*"; DestDir: "{app}\licenses"; Flags: recursesubdirs createallsubdirs
Source: "readme.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ENK Generador de Unifilares"; Filename: "{app}\ENK_Generador_Unifilares.exe"; WorkingDir: "{app}\_internal"
Name: "{commondesktop}\ENK Generador de Unifilares"; Filename: "{app}\ENK_Generador_Unifilares.exe"; WorkingDir: "{app}\_internal"

[Code]
function InitializeSetup(): Boolean;
begin
  Result := True;
end;