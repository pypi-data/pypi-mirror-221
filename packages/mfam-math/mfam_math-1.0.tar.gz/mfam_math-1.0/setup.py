from setuptools import setup, find_packages

setup(
    name='mfam_math',
    version='1.0',
    packages=find_packages(include=['mfam_math', 'mfam_math.*']),
    description='A small math library',
    author='Manuel Marinho',
    author_email='mfamarinho@gmail.com',
    url='http://github.com/yourusername/mathlib',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)