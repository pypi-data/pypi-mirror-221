from setuptools import setup
import os

setup(
    name='pytreexo',
    version='0.1.0',
    description='Python bindings for rustreexo',
    long_description="Python bindings for rustreexo",
    author='Davidson Souza',
    author_email='davidson.lucas.souza@outlook.com',
    license='MIT',
    py_modules=['pytreexo', '_pytreexo.bindings', '_pytreexo.proof', '_pytreexo.stump'],
    install_requires=[],
    zip_safe=True,
    url="https://github.com/mit-dci/rustreexo",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Security :: Cryptography"
    ]
)
