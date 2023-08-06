#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-subcommandir',
    version='0.3.0',
    description='Django subcommands in subdirectories',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sergei Pikhovkin',
    author_email='s@pikhovkin.ru',
    url='https://github.com/pikhovkin/django-subcommandir',
    packages=[
        'subcommandir',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=3.1,<4.2',
    ],
    python_requires='>=3.7,<4.0',
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords=[
        'django', 'command', 'commands', 'django-commands', 'django-subcommands',
    ],
)
