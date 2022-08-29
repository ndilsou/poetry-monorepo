# Python Monorepo example

This repo is a possible starter solution for of a monorepo setup in Python using [Poetry](https://python-poetry.org/)

## Structure

### root

base folder containing shared dotfiles

#### /apps

contains individual deployable packages like `api`, `workers`, etc...

#### /libs

contains shared libraries that can be installed locally into other packages.

##### /libs/devel

a special libs package containing the common dev dependencies like `pylint`, `flake8`, etc... It simplifies locking their versions across packages.

#### /tools

contains internal tools and cli used across the project.
