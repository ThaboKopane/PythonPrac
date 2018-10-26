try:
	from setuptools import setup

except ImportError:
	from distutils import setup

config = {
	'description': 'exercie 47',
	'author': 'Thabo Kopane',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'kpntha001@myuct.ac.za',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'exercise47'
}

setup(**config)