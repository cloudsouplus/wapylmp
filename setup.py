"""
This file is part of lammps-pythonic-wrapper.
Copyright (C) 2017  Takayuki Kobayashi

lammps-pythonic-wrapper is free software:
you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option)
any later version.

lammps-pythonic-wrapper is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with lammps-pythonic-wrapper.
If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

setup(
    name="lammps-pythonic-wrapper",
    version="0.0.1",
    description="To use Lammps Python Wrapper in more Python-Like way.",
    author="Takayuki Kobayashi",
    author_email="iris.takayuki@gmail.com",
    install_requires=[],
    url="https://github.com/irisTa56/lammps-pythonic-wrapper.git",
    license="GPL",
    py_modules=['lammps_pythonic_wrapper']
)
