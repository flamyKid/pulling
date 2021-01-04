from setuptools import setup
from os.path import join, dirname

setup(name='pulling',
      version='1.4.1',
      packages=['pulling'],
      license='Apache License 2.0',
      author='ItYaS',
      author_email='ryaboshapkoseraph@gmail.com',
      url='https://github.com/ItYaS/pulling',
      description='Pulling is an open source python repository for working with files of different extensions.',
      long_description=open(join(dirname(__file__), 'README.txt')).read(),
      zip_safe=False)
