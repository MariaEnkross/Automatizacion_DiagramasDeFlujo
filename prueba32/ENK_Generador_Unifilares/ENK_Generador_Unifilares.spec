# ENK_Generador_Unifilares.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['CodigoFuente.pyw'],
    pathex=['.'],  # Asegúrate de que la ruta sea correcta
    binaries=[],
    datas=[
        ('ENK_Generador_Unifilares/images/isotipo48_48.ico', 'ENK_Generador_Unifilares/images'),
        ('ENK_Generador_Unifilares/images/icon_help.png', 'ENK_Generador_Unifilares/images'),
        ('ENK_Generador_Unifilares/docs/ayuda/ManualUso.pdf', 'ENK_Generador_Unifilares/docs/ayuda')
    ],
    hiddenimports=['matplotlib.backends.backend_pdf'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ENK_Generador_Unifilares',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Cambia a True si quieres una consola
    icon='ENK_Generador_Unifilares/images/isotipo48_48.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ENK_Generador_Unifilares',
)

