# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='ds_helper',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Adam Marcus',
      packages=['ds_helper'],
      install_requires=['numpy>=1.18.5'
      'python-dateutil>=2.8.1'
      'pytz>=2020.1'
      'six>=1.15.0'])
