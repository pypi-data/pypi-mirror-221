# setup.py
from setuptools import setup, find_packages

setup(
    name='youtube-transcriber1',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytube',
        'whisper',
    ],
    entry_points={
        'console_scripts': [
            'youtube-transcriber = main:main'
        ]
    },
)
