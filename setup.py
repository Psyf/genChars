from setuptools import setup
setup(
    name = 'genChars',
    version = '0.1.0',
    packages = ['genChars'],
    entry_points = {
        'console_scripts': [
            'genChars = genChars.__main__:main'
        ]
    }, 
    install_requires = [
        'click'    
    ])
