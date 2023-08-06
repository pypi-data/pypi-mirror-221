from setuptools import setup

from beehiiv.__version__ import __version__

with open('README.md', 'r',) as f:
    readme = f.read()

setup(
    name='beehiiv',
    version=__version__,
    install_requires=['requests'],
    packages=['beehiiv'],
    url='https://github.com/abrihter/beehiiv',
    long_description_content_type="text/markdown",
    long_description=readme,
    license='MIT',
    author='abrihter',
    author_email='',
    description='Python wrapper for the BeeHiiv API',
    keywords=['BEEHIIV', 'API', 'WRAPPER'],
    download_url='https://github.com/abrihter/beehiiv/archive/refs/tags/v0.1b.tar.gz',  # noqa E501
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
