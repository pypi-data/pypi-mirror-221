from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zzq-strings-sum',
    version='0.5.3',
    description='A client for Databus API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='zzq',
    author_email='zhaozhiqiang@vikadata.com',
    packages=find_packages(),
    install_requires=['requests'],
)
