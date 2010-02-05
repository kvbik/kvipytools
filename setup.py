from setuptools import setup

setup(
    name='KviPyTools',
    version='0.1.0',
    packages = ['kvipytools'],
    scripts=['scripts/rename.sh'],
    entry_points = {
        'console_scripts': [
            'rename.py = kvipytools.rename:main',
            'run.py = kvipytools.run:main',
        ],
    }
)

