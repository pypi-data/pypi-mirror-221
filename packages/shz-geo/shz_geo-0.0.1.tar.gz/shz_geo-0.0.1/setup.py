from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

project_name = 'shz_geo'

setup(name=project_name,
    version='0.0.1',
    license='MIT License',
    author='Eliseu Brito',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='eliseubrito776@gmail.com',
    keywords='shz geo shz_geo shzgeo',
    description=u'Personal support tools in the development of geospatial projects',
    packages=['shz_geo'],
    install_requires=['modis_tools==1.1.1'],)