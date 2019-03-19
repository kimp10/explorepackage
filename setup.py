from setuptools import setup, find_packages

setup(
    name='explore_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/kimp10/explore_package',
    author='khutso',
    author_email='khutsomphelo@gmail.com'
)
