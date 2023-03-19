from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'my_script=my_package.module1:main',
        ],
    },
)
