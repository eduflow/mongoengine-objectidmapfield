# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

DESCRIPTION = "A MongoEngine MapField that allows and requires ObjectIds as " \
              "keys."

try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name='mongoengine-objectidmapfield',
    version='0.0.1',
    packages=find_packages(),
    author='Malthe Jørgensen',
    author_email='malthe.jorgensen@gmail.com',
    url='https://github.com/peergradeio/mongoengine-objectidmapfield',
    license='BSD 3-Clause',
    include_package_data=True,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: BSD 3-clause',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['mongoengine', 'six'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    test_suite='tests',
)
