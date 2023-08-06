from setuptools import setup, find_packages

setup(
    name='dmrmath',
    version='1.0',
    packages=find_packages(include=['dmrmath', 'dmrmath.*']),
    description='A small math library',
    author='Daniel Rodrigues',
    author_email='danielrodrigues.ps3@gmail.com',
    url='http://github.com/yourusername/mathlib',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)