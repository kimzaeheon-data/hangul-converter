from setuptools import setup

APP = ['src/main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['rumps', 'pyperclip'],
    'plist': {
        'CFBundleName': '한글 변환기',
        'CFBundleDisplayname': '한글 변환기',
        'CFBundleVersion': '1.0.0',
        'LSUIElement': True,
    }
}

setup(
    app = APP,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app']
)