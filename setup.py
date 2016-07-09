from distutils.core import setup
with open('README.rst') as file:
    long_description = file.read()

setup(name='qtrotate',
      version='2.1.2',
      url='https://github.com/evgenity/qtrotate',
      author='evgenity',
      author_email='evgenity.dev@gmail.com',
      py_modules=['qtrotate'],
      long_description=long_description
      )
