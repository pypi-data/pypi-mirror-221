from setuptools import setup, find_packages

setup(
    name='amvvmath',
    version='1.0',
    packages=find_packages(include=['amvvmath', 'amvvmath.*']),
    description='A small math library',
    author='Angelo Veiga',
    author_email='angelo_veiga@live.com',
    url='http://github.com/banavids/mathlib',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)