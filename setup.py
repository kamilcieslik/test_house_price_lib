from setuptools import setup, find_packages

setup(
    name='house-price-calculator',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Library designed for calculating house prices.',
    long_description=open('README.md').read(),
    install_requires=['googlemaps'],
    url='https://github.com/kamilcieslik/house_price_calculator',
    author='Kamil Cieślik',
    author_email='mrfarinq@hotmail.com'
)