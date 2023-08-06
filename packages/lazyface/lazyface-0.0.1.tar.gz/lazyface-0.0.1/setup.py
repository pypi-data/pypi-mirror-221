from setuptools import setup

setup(
  name = 'lazyface',
  packages = ['lazyface'],
  version = '0.0.1',
  description = 'lazyface',
  long_description = 'Lazyme, lazyface',
  author = '',
  url = 'https://github.com/alvations/lazyface',
  keywords = [],
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires = ['requests', 'transformers', 'evaluate', 'datasets', 'setfit', 'trl', 'accelerate'],
)
