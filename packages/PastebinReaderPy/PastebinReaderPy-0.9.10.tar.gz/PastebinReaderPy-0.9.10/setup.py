import setuptools
with open(r'README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='PastebinReaderPy',
	version='0.9.10',
	author='Dolenko10.0Artem10.0',
	author_email='artemdolenko.ua@gmail.com',
	description='Python Pastebin Library for reading and running pastes',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=['pastebin'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
