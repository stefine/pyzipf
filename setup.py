from setuptools import setup


setup(
    name='pyzipf',
    version='0.1.0',
    author='533',
    packages=['pyzipf'],
    install_requires=[
        'matplotlib',
        'pandas',
        'scipy',
        'pytest',
        'pyyaml',
    ],
    entry_points={
        'console_scripts':[
            'countwords = pyzipf.countwords:main',
            'collate = pyzipf.collate:main',
            'plotcounts = pyzipf.plotcounts:main'
        ]
    })
