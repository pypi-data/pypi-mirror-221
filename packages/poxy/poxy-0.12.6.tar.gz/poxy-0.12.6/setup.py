#!/usr/bin/env python3
# This file is a part of marzer/poxy and is subject to the the terms of the MIT license.
# Copyright (c) Mark Gillard <mark.gillard@outlook.com.au>
# See https://github.com/marzer/poxy/blob/master/LICENSE.txt for the full license text.
# SPDX-License-Identifier: MIT

# set up based on this: https://thucnc.medium.com/how-to-publish-your-own-python-package-to-pypi-4318868210f9
# windows:
# py setup.py sdist bdist_wheel && twine upload dist/* && rmdir /S /Q dist

import re
from setuptools import setup, find_packages
from pathlib import Path



def enum_subdirs(root):
	root = Path(root).resolve()
	assert root.is_dir()
	subdirs = []
	for p in root.iterdir():
		if p.is_dir():
			subdirs.append(p)
			subdirs = subdirs + enum_subdirs(p)
	return subdirs



package_dir = str(Path(Path(__file__).parent, r'poxy').resolve())
data_dir = Path(package_dir, r'data')
data_subdirs = enum_subdirs(data_dir)
data_subdirs = [str(d)[len(package_dir):].strip('\\/').replace('\\', '/') for d in data_subdirs]
data_subdirs = [rf'{d}/*' for d in data_subdirs]

README = ''
with open(r'README.md', encoding='utf-8') as file:
	README = file.read().strip()

CHANGELOG = ''
with open(r'CHANGELOG.md', encoding='utf-8') as file:
	CHANGELOG = f'\n\n{file.read()}\n\n'
CHANGELOG = re.sub(r'\n#+\s*Changelog\s*?\n', '\n## Changelog\n', CHANGELOG, flags=re.I).strip()

VERSION = ''
with open(Path(data_dir, 'version.txt'), encoding='utf-8') as file:
	VERSION = file.read().strip()

SETUP_ARGS = {
	'name': r'poxy',
	'version': VERSION,
	'description': r'Documentation generator for C++.',
	'long_description_content_type': r'text/markdown',
	'long_description': f'{README}\n<br><br>\n{CHANGELOG}'.strip(),
	'license': r'MIT',
	'packages': find_packages(),
	'author': r'Mark Gillard',
	'author_email': r'mark.gillard@outlook.com.au',
	'keywords': [r'c++', r'doxygen', r'documentation'],
	'url': r'https://github.com/marzer/poxy',
	'download_url': r'https://pypi.org/project/poxy/',
	'classifiers': [
	r'Development Status :: 4 - Beta',  #
	r'License :: OSI Approved :: MIT License',
	r'Programming Language :: C++',
	r'Topic :: Documentation',
	r'Topic :: Software Development :: Documentation',
	r'Topic :: Utilities'
	],
	'project_urls': {
	r'Source': r'https://github.com/marzer/poxy',
	r'Tracker': r'https://github.com/marzer/poxy/issues'
	},
	r'python_requires': r'>=3.7',
	'package_data': {
	r'poxy': [r'data/*', *data_subdirs]
	},
	'exclude_package_data': {
	r'poxy': [
	r'.git*',
	r'.istanbul.yaml',
	r'*.rst',
	r'*.pyc',
	r'data/m.css/artwork/*',
	r'data/m.css/doc/*',
	r'data/m.css/documentation/test/*',
	r'data/m.css/documentation/test_doxygen/*',
	r'data/m.css/documentation/test_python/*',
	r'data/m.css/documentation/templates/python/*',
	r'data/m.css/package/*',
	r'data/m.css/plugins/m/test/*',
	r'data/m.css/site/*',
	]
	},
	'entry_points': {
	r'console_scripts': [
	r'poxy = poxy.main:main',  #
	r'poxyblog = poxy.main:main_blog_post'
	]
	}
}

REQUIRES = None
with open(r'requirements.txt', encoding='utf-8') as file:
	REQUIRES = file.read().strip().split()

if __name__ == '__main__':
	setup(**SETUP_ARGS, install_requires=REQUIRES)
