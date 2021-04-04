#!/usr/bin/env python
from re import findall

from setuptools import find_packages, setup

with open("proxygrab/__init__.py", encoding="utf-8") as f:
    version = findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md") as fh:
    long_description = fh.read()


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="ProxyGrab",
    license="MIT",
    version=version,
    packages=find_packages(),
    author="Divkix",
    author_email="techdroidroot@gmail.com",
    description="Asynchronous Library made using Python and aiohttp to get proxies from multiple services!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="proxyscrape proxies proxygrab proxygrab-python proxylist",
    url="http://github.com/Divkix/ProxyGrab/",
    install_requires=requirements,
    python_requires=">=3.7",
    entry_points={"console_scripts": {"proxygrab=proxygrab.cmdline:clicmd"}},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    project_urls={
        "Tracker": "https://github.com/Divkix/ProxyGrab/issues",
        "Community": "https://t.me/DivideProjects",
        "Source": "https://github.com/Divkix/ProxyGrab",
        "Documentation": "https://proxygrab.netlify.app",
    },
)
