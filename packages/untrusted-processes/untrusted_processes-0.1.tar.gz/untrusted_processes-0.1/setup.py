from setuptools import setup, find_packages

setup(
    name='untrusted_processes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
    ],
)
