#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Steve Barnes",
    author_email='gadgetsteve@hotmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Arch Tool is intended to provide an archive type independent interface for performing operations on archives, (.zip, .tar.gz, etc), including adding, searching, viewing, extracting or getting hashes from files within the archive.",
    entry_points={
        'console_scripts': [
            'arch_tool=arch_tool.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='arch_tool',
    name='arch_tool',
    packages=find_packages(include=['arch_tool', 'arch_tool.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/GadgetSteve/arch_tool',
    # This section is to trigger the use of setuptools_scm to automate version numbers.
    use_scm_version=True,
    setup_requires=[
        "setuptools_scm",
    ],
    zip_safe=False,
)
