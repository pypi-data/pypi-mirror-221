# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='autocreateapp',
    version='0.4',  # Update the version number to 0.2 (or any desired version)
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    entry_points={
        'console_scripts': [
            'autocreateapp=autocreateapp.create_project:create_django_project',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify the content type as Markdown
)
