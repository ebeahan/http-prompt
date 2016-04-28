try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import codecs
import os
import re


here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string')


def read_description(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        return f.read()


requirements = [
    # TODO
    'click>=5.0',
    'httpie>=0.9.0',
    'parsimonious>=0.6.2',
    'prompt-toolkit>=0.60',
    'Pygments>=2.1.0',
]

test_requirements = [
    # TODO
    'pytest',
    'pytest-cov',
]

setup(
    name='http-prompt',
    version=find_version('http_prompt', '__init__.py'),
    url='https://github.com/eliangcs/http-prompt',
    description='An interactive HTTP command-line client',
    long_description=read_description('README.rst'),
    author='Chang-Hung Liang',
    author_email='eliang.cs@gmail.com',
    license='MIT',
    packages=['http_prompt'],
    entry_points="""
        [console_scripts]
        http-prompt=http_prompt.cli:cli
    """,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    test_suites='tests',
    test_requires=test_requirements
)