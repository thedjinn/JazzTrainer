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

import os
import sys

APPNAME="JazzTrainer"
APPVERSION="0.1"
APPAUTHORS=["Emil Loer"]
APPSHORTDESC="A tool to learn jazz piano voicings."
APPCOPYRIGHT=u"Copyright \u00a9 2010 Emil Loer"
APPWEBSITE="http://www.koffietijd.net/"

if os.path.exists("./data") and os.path.exists("./jazztrainer"):
	DATADIR="./data/"
elif os.path.exists("/usr/local/share/jazztrainer"): # Python 2.6 on Ubuntu wants this
	DATADIR="/usr/local/share/jazztrainer/"
else:
	DATADIR=os.path.join(sys.prefix,"share","jazztrainer","")
