from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()

REQUIRED = [
    'websocket'
]

setup(name='zerocap_websocket_test',  # 包名
      version='1.0.2',  # 版本号
      description='websocket_test',
      long_description=long_description,
      author='gaogao',
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
