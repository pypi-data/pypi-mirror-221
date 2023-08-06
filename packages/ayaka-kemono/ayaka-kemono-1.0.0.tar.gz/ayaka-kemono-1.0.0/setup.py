from setuptools import setup, find_packages

setup(
    name='ayaka-kemono',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'console_scripts': ['ayaka=ayaka.ayaka:main'],
    },
    author='Joshua James',
    author_email='joshjms1607@gmail.com',
    description='Pixiv Fanbox Downloader from Kemono.party',
    url='https://github.com/joshjms/ayaka',
)
