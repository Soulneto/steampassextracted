# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
        datas=[
        ('assets/*', 'assets'),
        ('certifi/*', 'certifi'),
        ('charset_normalizer/*', 'charset_normalizer'),
        ('cryptography/*', 'cryptography'),
        ('cryptography-44.0.3.dist-info/*', 'cryptography-44.0.3.dist-info'),
        ('google_api_python_client-2.166.0.dist-info/*', 'google_api_python_client-2.166.0.dist-info'),
        ('googleapiclient/*', 'googleapiclient'),
        ('httplib2/*', 'httplib2'),
        ('markupsafe/*', 'markupsafe'),
        ('MarkupSafe-3.0.2.dist-info/*', 'MarkupSafe-3.0.2.dist-info'),
        ('psutil/*', 'psutil'),
        ('PyQt5/*', 'PyQt5'),
        ('PYZ.pyz_extracted/xmlrpc/*', 'xmlrpc'),
        ('setuptools/*', 'setuptools')
    ],

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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
