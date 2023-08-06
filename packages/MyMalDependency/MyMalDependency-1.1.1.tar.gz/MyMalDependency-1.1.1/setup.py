from setuptools import setup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
setup(
    name='MyMalDependency', # 自定义包名
    version='1.1.1', # 包的版本号
    description='test to create package', # 描述信息
    author='1', # 作者
)
