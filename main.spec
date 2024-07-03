# -*- mode: python ; coding: utf-8 -*-

# The path to your project directory
project_dir = r'C:\Users\USER\python_project'

a = Analysis(
    ['main.py'],
    pathex=[project_dir],
    binaries=[],
    datas=[
        (os.path.join(project_dir, 'icons', 'favicon.ico'), 'icons')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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
    icon=os.path.join(project_dir, 'icons', 'favicon.ico'),
)
