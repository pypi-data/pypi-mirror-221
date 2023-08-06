from setuptools import find_packages, setup

# To upload in pypi, 
# python -m twine upload dist/*

setup(
    name='tablemap',
    version='0.3.7',
    description='sql not knowing sql',
    packages=find_packages(),
    long_description='',
    url='https://github.com/nalssee/tablemap.git',
    author='nalssee',
    author_email='jinisrolling@gmail.com',
    license='MIT',

)
