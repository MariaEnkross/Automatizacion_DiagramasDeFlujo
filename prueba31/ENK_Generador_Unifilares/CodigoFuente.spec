# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['CodigoFuente.pyw'],
    pathex=[],
    binaries=[],
    datas=[('ENK_Generador_Unifilares/images/isotipo48_48.ico', 'ENK_Generador_Unifilares/images'), ('ENK_Generador_Unifilares/images/icon_help.png', 'ENK_Generador_Unifilares/images'), ('ENK_Generador_Unifilares/docs/ayuda/ManualUso.pdf', 'ENK_Generador_Unifilares/docs/ayuda')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CodigoFuente',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ENK_Generador_Unifilares\\images\\isotipo48_48.ico'],
)
