#!/usr/bin/env python
import setuptools


with open("README.md") as fh:
    long_description = fh.read()


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="ProxyGrab",
    license="MIT",
    version="0.2.3",
    packages=setuptools.find_packages(),
    author="Skuzzy xD",
    author_email="techdroidroot@gmail.com",
    description="A simple package made using Python and requests to get proxies from multiple sites!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="proxyscrape proxies proxygrab proxygrab-python proxylist",
    url="http://github.com/SkuzzyxD/ProxyGrab/",
    install_requires=requirements,
    python_requires=">=3.6",
    entry_points="""
        [console_scripts]
        proxygrab=proxygrab.cmdline:clicmd""",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
