from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='torrent-hound',          # This is the name of your PyPI-package.
    version='2.1.1',                 # Update the version number for new releases
    scripts=['torrent-hound'],     # The name of your scipt, and also the command you'll be using for calling it
    description='Search torrents from multiple websites via the CLI',
    long_description=readme(),
    python_requires = '>=3',
    url='https://github.com/baddymaster/torrent-hound',
    install_requires=[
        'bs4',
        'requests',
        'clint',
        'pyperclip',
        'humanize',
        'VeryPrettyTable',
        'cfscrape'
    ],
    author='Yashovardhan Sharma',
    author_email='yash.s@tuta.io',
    license='AGPL-3.0',
)