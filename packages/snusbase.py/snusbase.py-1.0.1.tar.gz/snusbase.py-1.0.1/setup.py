from setuptools import setup, find_packages
from re import search, MULTILINE
from pathlib import Path


def get_version():
    version = ''
    with open(Path('snusbase') / '__init__.py', 'r', encoding='utf-8') as f:
        version = search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), MULTILINE
        ).group(1)
    return version


def read_requirements(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


setup(
    name='snusbase.py',
    author='igna',
    project_urls={
        'Website': 'https://snusbase.com',
        'Issue tracker': 'https://github.com/obstructive/snusbase.py',
    },
    version=get_version(),
    packages=find_packages(),
    license='MIT',
    description='an un-official async wrapper for the Snusbase API',
    long_description=Path('README.rst').read_text(encoding='utf-8'),
    include_package_data=True,
    install_requires=read_requirements('requirements.txt'),
    python_requires='>=3.6.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
