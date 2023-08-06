from setuptools import setup, find_packages
 
 
setup(
  name='kafkaproducerself',
  version='0.0.4',
  description='produce events to kafka',
  long_description='Boiler Functions for kafka push' + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abhishek Borana',
  author_email='tracer.domanik@fixedfor.com',
  license='MIT', 
  keywords='kafka', 
  packages=find_packages(),
  install_requires=['kafka-python'] 
)