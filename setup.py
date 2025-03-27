from setuptools import find_packages, setup

setup(
    name='alphavantage',
    packages=find_packages(include=['alphavantage']),
    version='0.1.0',
    description='Alpha Vantage API library - sixth street coding assessment',
    author='Ayan Patel',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)