# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['C:\KBTU\2nd semester\Wake_Up_Pp2ease'],
    binaries=[],
    datas=[('assets/kelgenbayev/t1.png', 'kelgenbayev'), ('assets/kelgenbayev/t2.png', 'kelgenbayev'), ('assets/kelgenbayev/t3.png', 'kelgenbayev'), ('assets/kelgenbayev/t4.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t5.png', 'kelgenbayev'), ('assets/kelgenbayev/t6.png', 'kelgenbayev'), ('assets/kelgenbayev/t7.png', 'kelgenbayev'), ('assets/kelgenbayev/t8.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t9.png', 'kelgenbayev'), ('assets/kelgenbayev/t10.png', 'kelgenbayev'), ('assets/kelgenbayev/t11.png', 'kelgenbayev'), ('assets/kelgenbayev/t12.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t13.png', 'kelgenbayev'), ('assets/kelgenbayev/t14.png', 'kelgenbayev'), ('assets/kelgenbayev/t15.png', 'kelgenbayev'), ('assets/kelgenbayev/t16.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t17.png', 'kelgenbayev'), ('assets/kelgenbayev/t18.png', 'kelgenbayev'), ('assets/kelgenbayev/t19.png', 'kelgenbayev'), ('assets/kelgenbayev/20.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t21.png', 'kelgenbayev'), ('assets/kelgenbayev/t22.png', 'kelgenbayev'), ('assets/kelgenbayev/t23.png', 'kelgenbayev'), ('assets/kelgenbayev/t24.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t25.png', 'kelgenbayev'), ('assets/kelgenbayev/t26.png', 'kelgenbayev'), ('assets/kelgenbayev/t27.png', 'kelgenbayev'), ('assets/kelgenbayev/t28.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t29.png', 'kelgenbayev'), ('assets/kelgenbayev/t30.png', 'kelgenbayev'), ('assets/kelgenbayev/t31.png', 'kelgenbayev'), ('assets/kelgenbayev/t32.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t33.png', 'kelgenbayev'), ('assets/kelgenbayev/t34.png', 'kelgenbayev'), ('assets/kelgenbayev/t35.png', 'kelgenbayev'), ('assets/kelgenbayev/t36.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t37.png', 'kelgenbayev'), ('assets/kelgenbayev/t38.png', 'kelgenbayev'), ('assets/kelgenbayev/t39.png', 'kelgenbayev'), ('assets/kelgenbayev/t40.png', 'kelgenbayev'),
    ('assets/kelgenbayev/t41.png', 'kelgenbayev'),
    ('assets/mp3/blip.mp3', 'mp3'), ('assets/mp3/c418_lullaby.mp3', 'mp3'), ('assets/mp3/c418_sweden.mp3', 'mp3'), ('assets/mp3/c418_wet.mp3', 'mp3'), ('assets/mp3/evil_morty.mp3', 'mp3'),
    ('assets/mp3/fail.mp3', 'mp3'), ('assets/mp3/jojo.mp3', 'mp3'), ('assets/mp3/lullaby.mp3', 'mp3'), ('assets/mp3/rick_roll.mp3', 'mp3'), ('assets/mp3/success.mp3', 'mp3'), ('assets/mp3/undertale_shop.mp3', 'mp3'),
    ('assets/students/a1.png', 'students'), ('assets/students/a2.png', 'students'), ('assets/students/a3.png', 'students')
    ('assets/students/b1.png', 'students'), ('assets/students/b2.png', 'students'), ('assets/students/b3.png', 'students')
    ('assets/students/c1.png', 'students'), ('assets/students/c2.png', 'students'), ('assets/students/c3.png', 'students')
    ('assets/students/j1.png', 'students'), ('assets/students/j2.png', 'students'), ('assets/students/j3.png', 'students')
    ('assets/students/k1.png', 'students'), ('assets/students/k2.png', 'students'), ('assets/students/k3.png', 'students'),
    ('assets/dogica.ttf', 'font'),
    ('assets/Bg.png', 'bg'), ('assets/button.png', 'bg'), ('assets/fail.png', 'bg'), ('assets/menu.png', 'bg'), ('assets/succeed.png', 'bg'), ('assets/thank_u.png', 'bg'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Wake up, pp2ease!',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, icon='C:\KBTU\2nd semester\Wake_Up_Pp2ease\t1.ico')
