from setuptools import setup, find_packages
with open('README.md', 'r') as r_file:
    desc = r_file.read()

LICENSE_TEXT = "License :: OSI Approved :: "
LICENSE_TEXT += "GNU Library or Lesser General Public License (LGPL)"

setup(
    name="recursive_size",
    version="1.0",
    packages=find_packages(),

    author="Deuteronomy Works",
    author_email="deutworks@gmail.com",
    description="An alternative to qmlscene",
    long_description=desc,
    long_description_content_type="text/markdown",
    keywords="size, get_size, get size, recursive size, recursive_size",
    url="https://github.com/deuteronomy-works/recursive_size",
    project_urls={
        "Bug Tracker": 
        "https://github.com/deuteronomy-works/recursive_size/issues",
        "Documentation": 
        "https://github.com/deuteronomy-works/recursive_size/wiki",
        "Source Code": "https://github.com/deuteronomy-works/recursive_size",
    },
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        LICENSE_TEXT,
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
