"""
Setuptools based setup module
"""
from setuptools import setup, find_packages
import versioneer

setup(
    name='pyworkerqueue',
    version=versioneer.get_version(),
    description='pyworkerqueue - A multiprocessing pool with asynchronous queue',
    long_description='pyworkerqueue simplifies the parallel execution of a growing list of objects.',

    url='https://github.com/pyiron/pyworkerqueue',
    author='Jan Janssen',
    author_email='janssen@mpie.de',
    license='BSD',

    classifiers=['Development Status :: 5 - Production/Stable',
                 'Topic :: Scientific/Engineering :: Physics',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Science/Research',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9'
                ],

    keywords='pyworkerqueue',
    packages=find_packages(exclude=["*tests*", "*binder*", "*notebooks*"]),
    cmdclass=versioneer.get_cmdclass(),
    )
