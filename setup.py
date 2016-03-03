#!/usr/bin/env python
from setuptools import setup
import metadata

app_name = metadata.name
version = metadata.version


def read(filename):
    with open(filename) as fp:
        return fp.read()


long_description = read('README.rst')

setup(
    name='django-%s' % app_name,
    version=version,
    packages=['tinymce'],
    include_package_data=True,
    author='Roman Miroshnychenko (fork author)',
    author_email='romanvm@yandex.ua',
    description='A Django application that provides '
                'a fully functional TinyMCE 4 editor widget for models and forms.',
    long_description=long_description,
    license='MIT License',
    keywords='django wysiwyg widget tinymce',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url='https://github.com/romanvm/django-tinymce4-lite',
    install_requires=[
        'Django>=1.8.0',
    ],
    zip_safe=False
)
