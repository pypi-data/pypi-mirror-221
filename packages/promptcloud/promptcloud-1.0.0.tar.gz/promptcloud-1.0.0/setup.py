from setuptools import setup, find_packages

setup(
    name='promptcloud',  
    version='1.0.0',
    description='Python SDK for the PromptCloud API',
    author='Matty Hogan',
    author_email='matthewhogan63@gmail.com',
    url='https://github.com/mattyhogan/PromptCloudPythonSDK',
    packages=find_packages(),
    install_requires=[
        'requests',
        'openai'
    ],
)