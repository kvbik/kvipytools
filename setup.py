from setuptools import setup
from os import path


VERSION = (0, 1, 3)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(path.join(path.dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()


setup(
    name = 'KviPyTools',
    description = "kvbik's python tools",
    url = "http://github.com/kvbik/kvipytools",
    long_description = long_description,
    version = __versionstr__,
    author = "Jakub Vysoky",
    author_email = "jakub@borka.cz",
    license = "BSD",
    packages = ['kvipytools'],
    scripts = ['scripts/rename.sh'],
    zip_safe = False,
    entry_points = {
        'console_scripts': [
            'rename = kvipytools.rename:main',
            'run = kvipytools.run:main',
        ],
    }
)

