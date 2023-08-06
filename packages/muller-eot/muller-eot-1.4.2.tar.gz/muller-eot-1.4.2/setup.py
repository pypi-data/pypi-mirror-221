# -*- coding: utf-8 -*-

# Python Package Setup
from setuptools import setup, find_namespace_packages

VERSION="1.4.2"
DESCRIPTION="A Python package for M. Müller implementation of the 'Equation of Time - Problem in Astronomy' to calculate EOT and the effect of eccentricity/obliquity"

with open("README.md", "r") as f:
	long_description_readme = f.read()

setup(
	name="muller-eot",
	version=VERSION,
	description=DESCRIPTION,
	long_description=long_description_readme,
	long_description_content_type='text/markdown',
	url="https://github.com/cyschneck/Muller-EOT",
	download_url="https://github.com/cyschneck/Muller-EOT/archive/refs/tags/v{0}.tar.gz".format(VERSION),
	author="Cora Schneck (cyschneck)",
	keywords=["astronomy", "python", "eot", "equation of time", "eccentricity", "obliquity", "orbital dynamics"],
	license="MIT",
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Intended Audience :: Education",
		"Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Physics",
		"Topic :: Scientific/Engineering :: Visualization",
		"Topic :: Scientific/Engineering :: Astronomy"
	],
	packages=find_namespace_packages(include=['muller_eot',
											'muller_eot.*']),
	include_package_data=True,
	install_requires=[
		"matplotlib>=3.1.0",
		"numpy>=1.21.6",
	],
	python_requires='>=3.7'
)
