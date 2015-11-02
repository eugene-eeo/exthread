import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'test']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='exthread',
    version='0.1.1',
    description='Supercharged threads',
    long_description=open('README.rst', 'rb').read().decode('utf8'),
    author='Eeo Jun',
    author_email='packwolf58@gmail.com',
    url='https://github.com/eugene-eeo/exthread/',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    package_data={'exthread': ['LICENSE', 'README.rst']},
    py_modules=['exthread'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    platforms='any',
    zip_safe=False,
)
