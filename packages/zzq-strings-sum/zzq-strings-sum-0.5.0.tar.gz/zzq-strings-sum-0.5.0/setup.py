from setuptools import setup, find_packages

setup(
    name='zzq-strings-sum',
    version='0.5.0',
    description='A client for Databus API',
    author='zzq',
    author_email='zhaozhiqiang@vikadata.com',
    packages=find_packages(),
    install_requires=['requests'],
)
