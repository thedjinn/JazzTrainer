# JazzTrainer - a tool to learn jazz chords
# Copyright (C) 2010 Emil Loer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
import glob
import os.path

setup(
	name="JazzTrainer",
	version="0.1",
	description="",
	author="Emil Loer",
	author_email="emil@koffietijd.net",
	url="http://www.koffietijd.net/",
	packages=["jazztrainer"],
	scripts=["scripts/jazztrainer"],
	license="GNU GPL v3",
	data_files=[
		(os.path.join("share","jazztrainer"),glob.glob(os.path.join("data","*"))),
	]
)
