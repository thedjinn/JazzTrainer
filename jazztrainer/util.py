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

import gtk

def falsify(fun,*args,**kwargs):
	def wrap():
		fun(*args,**kwargs)
		return False
	return wrap
	
def showmessage(parent,message):
	dlg=gtk.MessageDialog(parent,gtk.DIALOG_MODAL|gtk.DIALOG_DESTROY_WITH_PARENT,gtk.MESSAGE_INFO,gtk.BUTTONS_OK,message)
	dlg.run()
	dlg.destroy()
