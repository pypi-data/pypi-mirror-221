from setuptools import setup, find_packages

setuptools_kwargs = {
    'zip_safe': False,
    'install_requires': ['pyomo',
                         'coverage',
                         'numpy',
                         'scipy',
                         'pandas',
                         'assimulo'],
    'scripts': [],
    'include_package_data': True
}

setup(name='PharmaTwin',
      version='0.0.1',
      packages=find_packages(),
      package_data={
        'PharmaPy': ['..\data\*.*'],
        'PharmaPy': ['..\tests\integration\*.*']
        },
      author='Daniel Casas-Orozco',
      author_email='dcasasor@purdue.edu',
      license='LICENSE.md',
      url='https://github.com/CryPTSys/PharmaPy',
      test_suite='tests\integration',
      **setuptools_kwargs)
