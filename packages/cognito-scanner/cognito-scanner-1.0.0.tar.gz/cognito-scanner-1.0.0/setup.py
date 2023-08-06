from setuptools import setup, find_packages

setup(
    name='cognito-scanner',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "boto3", "typer"
    ],
    entry_points={
        'console_scripts': [
            'cognito-scanner = scanner.scanner:cli',
        ],
    },
    authors = [ { 'name': "Thibault Lengagne", 'email': 'thibaultl@padok.fr' }, { 'name':"Clement Fgs", 'email':'clementfa@padok.fr' }, ],
    description="A simple script which implements different Cognito attacks such as Account Oracle or Priviledge Escalation",
    readme="README.md",
    author_email='thibaultl@padok.fr',
    url='https://github.com/padok-team/cognito-scanner',
    license='Apache2',
)
