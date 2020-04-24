from setuptools import setup, find_packages

setup(name='WotAPI',
      version='0.0.1',
      description='Extract data from the World of Tanks PC API',
      author='Gabriel Oana',
      author_email='gabriel.oana91@gmail.com',
      license='MIT',
      zip_safe=False,
      packages=find_packages(),
      install_requires=[
            'requests',
            'sqlalchemy',
      ]
)