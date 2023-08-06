from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()

REQUIRED = [
    'requests',
    'websocket'
]

setup(name='zerocap_api_test',  # 包名
      version='0.1.2',  # 版本号
      description='zerocap_api',
      long_description=long_description,
      author='jiayu.gao',
      author_email='y18362683626@gmail.com',
      url='',
      install_requires=REQUIRED,
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',  # 对python的最低版本要求
      )
