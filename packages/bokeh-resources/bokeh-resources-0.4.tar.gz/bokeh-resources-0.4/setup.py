#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bokeh-resources",
    version="0.4",
    author='Lev Maximov',
    author_email='lev.maximov@gmail.com',
    url='https://github.com/axil/bokeh-resources',
    description="Jupyter extension to serve bokeh resources (js and css files).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['bokeh', 'notebook', 'jupyter_contrib_nbextensions'],
    packages=['bokeh_resources', 'bokeh_resources.bokeh_resources'],
    package_data={'': ['*.js']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT License",
    zip_safe=False,
    keywords=['bokeh', 'jupyter', 'notebook'],
)
