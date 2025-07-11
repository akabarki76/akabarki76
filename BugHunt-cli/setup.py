
from setuptools import setup, find_packages

setup(
    name='BugHunt-cli',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bughunt = main:main',
        ],
    },
    install_requires=[
        # Add dependencies here
    ],
)
