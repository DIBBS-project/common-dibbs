from setuptools import setup, find_packages

setup(
    name='common-dibbs',
    version='0.2.0a1',
    packages=find_packages(),
    install_requires=[
        'pyjwt>=1.4.2',
    ],
)
