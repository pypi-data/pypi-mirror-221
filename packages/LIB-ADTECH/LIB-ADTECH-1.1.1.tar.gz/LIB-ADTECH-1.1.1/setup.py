from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()


setup(
    name='LIB-ADTECH',
    version='1.1.1',
    license='MIT License',
    author='Alan, Fabiano e Yan',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='driverWait, librarySelenium',
    description=u'Funcoes uteis para desenvolvimento web.',
    packages=['Adlib'],
    install_requires=['requests'],
)
