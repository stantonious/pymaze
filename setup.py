from distutils.core import setup
import os

version = os.environ.get("pymaze", "0.0.0")

setup(name='pymaze',
      version=version,
      description='''nifty code to generator mazes. ''',
      author='',
      author_email='',
      scripts=[],
      package_data={},
      packages=['pymaze'],
      package_dir={'pymaze': 'pymaze'},
      install_requires=[
      ],
      )

