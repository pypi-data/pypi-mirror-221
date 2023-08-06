from setuptools import find_packages, setup

setup(
    name='gauth_python_package',
    packages=find_packages(include=['gauth_python_package']),
    version='0.1.2',
    description='Python sdk from Gauth.',
    author='Noh Gaseong',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)

