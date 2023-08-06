from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='telegram-api-robot',
  version='1.0.0',
  author='mr nick and missis name',
  description='',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  python_requires='>=3.7'
)