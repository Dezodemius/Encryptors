from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Encryptors',
    version='1.0',
    packages=find_packages(),
    url='',
    license='GNU General Public License v3.0',
    author='Yehor Hladkov',
    author_email='gladkovyegor@gmail.com',
    description='Package contains a set of encryption/decryption modules.',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
