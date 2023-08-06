from setuptools import setup

setup(
    name='HABZONEpy',  #nombre del paquete
    version='0.2', #versión
    license = 'MIT',
    author="ignacio solis", #autor
    description="un paquete para encontrar la zona habitable de una estrella", #Breve descripción
    install_requires = ['numpy','matplotlib']
)

