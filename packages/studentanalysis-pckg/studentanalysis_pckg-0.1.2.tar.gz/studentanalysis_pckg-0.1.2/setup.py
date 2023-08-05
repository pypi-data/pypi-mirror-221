from setuptools import setup

setup(
    name='studentanalysis_pckg',
    version='0.1.2',
    author='Nora Hunger, Laurenz Gilbert, Rado Nomena Radimilahy',
    packages=['studentanalysis_pckg'],
    install_requires=['matplotlib',
        	          'seaborn',
                      'tabulate',
                      'pandas',
    ],
)