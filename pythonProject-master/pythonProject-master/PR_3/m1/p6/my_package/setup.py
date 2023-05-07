from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.15.0',
        'pandas>=0.23.4'
    ],
    include_package_data=True
)