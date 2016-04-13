from setuptools import setup

setup(name='Boruta',
      version='0.1.1',
      description='Python Implementation of Boruta Feature Selection',
      url='https://github.com/danielhomola/boruta_py',
      author='Daniel Homola',
      author_email='dani.homola@gmail.com',
      license='BSD 3 clause',
      packages=['boruta'],
      zip_safe=False,
      install_requires=['bottleneck==1.0.0',
                        'numpy==1.10.4',
                        'pandas==0.18.0',
                        'scikit-learn==0.17.1',
                        'scipy==0.17.0',
                        'statsmodels==0.6.1'
                        ])
