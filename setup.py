from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='okay',
      version='0.1',
      description='Everything is just okay',
      long_discription='A Programming Language inspired by Brainfuck and believe me it is okay',
      classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Compilers :: Programming',
      ],
      url='http://github.com/omarayad1/okay',
      author='Omar Ayad',
      author_email='omarayad1@gmail.com',
      keywords='compilers brainfuck programming REPL',
      scripts=['bin/okay'],
      license='MIT',
      packages=['okay'],
      zip_safe=False)