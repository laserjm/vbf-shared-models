from setuptools import setup, find_packages

setup(
    name='VbfSharedModels',
    version='0.1',
    packages=find_packages(),
    install_requires=['pydantic'],
    author='Jan-Michael Laser',
    author_email='jmlaser@web.com',
    description='A package for sharing models',
    url='https://github.com/laserjm/vbf-shared-models'
)
