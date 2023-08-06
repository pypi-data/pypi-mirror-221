from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mcqgen',
    version='1.0.0',
    packages=find_packages(),
    author='Abhilash Mhaisne',
    author_email='abhilashmhaisne@gmail.com',
    description='Generate Multiple Choice Questions, Choices and Correct Answer in JSON Format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['openai'],
    license='MIT License',
    url='https://github.com/55abhilash/mcqgen'
)
