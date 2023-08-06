from setuptools import setup, find_packages

setup(
    name='zlgsendcan',
    version='1.0.0',
    author='liuzhong',
    author_email='liuzhong@autolink.com.cn',
    description='zlg send canmsg',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'cantools',
        'yaml'
    ],
)