from setuptools import setup, find_packages

setup(
    name='aityz',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'rsa'
    ],
    author='Aityz',
    author_email='itzaityz@gmail.com',
    description='The multipurpose package, built for programmers',
    long_description=open('README.md').read(),
    url='https://github.com/Aityz/Library',
)
