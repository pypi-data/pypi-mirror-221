from setuptools import setup


def read_file(fname):
    with open(fname) as f:
        return f.read()


setup(
    name='fd_test_rail',
    description='pytest plugin for creating TestRail runs and adding results self',
    long_description=read_file('README.rst'),
    version='1.0.0',
    
    
  
    packages=[
        'pytest_testrail',
    ],
    package_dir={'pytest_testrail': 'pytest_testrail'},
    install_requires=[
        'pytest>=3.6',
        'requests>=2.20.0',
    ],
    include_package_data=True,
    entry_points={'pytest11': ['pytest-testrail = pytest_testrail.conftest']},
)
