from setuptools import setup, find_packages

setup(
    name='autocreateapp',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package requires, e.g., Django
        'Django',
    ],
    entry_points={
        'console_scripts': [
            'autocreateapp=autocreateapp.create_project:create_django_project',
        ],
    },
)
