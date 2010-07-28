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

# this is a gtkbuilder window wrapper

import logging

import gtk
import glib

import util

class GladeWrapper:
	def __init__(self,gladefile):
		builder=gtk.Builder()

		try:
			builder.add_from_file(gladefile)
		except glib.GError, e:
			util.showmessage(None,str(e))
			raise SystemExit(str(e))

		builder.connect_signals(self)

		for e in builder.get_objects():
			if issubclass(type(e),gtk.Buildable):
				setattr(self,gtk.Buildable.get_name(e),e)
			else:
				logging.debug("WARNING: can not get name for '%s'"%e)

	def run(self):
		try:
			gtk.main()
		except KeyboardInterrupt:
			self.on_keyboard_interrupt()

	def on_keyboard_interrupt(self):
		pass
