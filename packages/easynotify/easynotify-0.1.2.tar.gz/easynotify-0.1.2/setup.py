from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='easynotify',
    version='0.1.2',
    descripton='This package allows you to post messages with bots easily.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CauchyComplete/EasyNotify',
    author='CauchyComplete',
    author_email='corundum240@gmail.com',
    license='MIT',
    packages=['easynotify'],
    install_requires=[
        'requests>=2.0'
    ],
)


