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

from gladewrapper import GladeWrapper
from version import *
from piano import Piano
import util
import gtk
import glib

# A view for the chord trainer logic

class PianoPanel(GladeWrapper):
	def __init__(self):
		GladeWrapper.__init__(self,os.path.join(DATADIR,"pianopanel.glade"))
		
		try:
			self.piano=Piano(os.path.join(DATADIR,"pianoroll.png"))
		except glib.GError, e:
			util.showmessage(None,str(e))
			raise SystemExit(str(e))
		
		self.piano.show()
		self.pianobox.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color('#000'))
		self.pianobox.add(self.piano)

	def setmarkup(self,markup):
		self.chordlabel.set_markup(markup)
	
	def redbg(self):
		self.chordlabelbox.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color('#f00'))

	def greenbg(self):
		self.chordlabelbox.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color('#0f0'))

	def nobg(self):
		self.chordlabelbox.modify_bg(gtk.STATE_NORMAL,None)

	def run(self):
		# TODO: build a window and insert toplevel
		pass
