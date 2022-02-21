# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*
"""
Initial setup
"""

from setuptools import setup, find_packages

p={}

with open("reddit_webscrapping/__init__.py", 'r') as f:
    exec(f.read(), p)
    V = p['__version__']
    
setup(
        name="reddit_webscrapping",
        version=V,
        description="reddit webscrapping to get popular stocks TICKER",
        author="Anjali",
        author_email="anjali94venu@gmail.com",
        license="proprietary",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[],
        zip_safe=False
)
