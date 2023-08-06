from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mcqgen',
    version='0.1.0',
    packages=find_packages(),
    author='Abhilash Mhaisne',
    description='Generate Multiple Choice Questions, Choices and Correct Answer in JSON Format',
    long_description=long_description,
    install_requires=['openai'],
    license='MIT License'
)
