# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['wxHelloWorld.py'],
             pathex=['D:\\zhangzs\\study\\code\\python\\999-随便玩玩\\2-pyinstaller生成可执行文件\\3-wxpython图形界面-pipenv处理'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='wxHelloWorld',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
