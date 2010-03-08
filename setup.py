from setuptools import setup

setup(
    name = 'KviPyTools',
    description = "kvbik's python tools",
    url = "http://github.com/kvbik/python-scripts",
    version = '0.1.1',
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

