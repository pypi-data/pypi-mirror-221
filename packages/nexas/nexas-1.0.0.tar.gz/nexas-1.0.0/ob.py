from setuptools import setup, find_packages

setup(
    name='nexas',
    version='1.0.0',
    author='vexin',
    description='twitch aio',
    packages=find_packages(),
    install_requires=[
        'requests',
        'disnake',
    ],
)
