from setuptools import setup
packages = ['zlgsendcan']# 唯一的包名，自己取名
setup(
    name='zlgsendcan',
    version='1.1.7',
    author='liuzhong',
    author_email='liuzhong@autolink.com.cn',
    description='zlg send canmsg',
    packages=packages,
    include_package_data=True,
    package_data={'zlgsendcan': ['kerneldlls/*','*.dll','*.yml']},
    install_requires=[
        'PyQt5',
        'cantools',
        'PyYAML'
    ],
)