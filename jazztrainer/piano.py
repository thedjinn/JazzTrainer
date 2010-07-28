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

# TODO: transform to a real widget to enable interaction
# TODO: more highlighting options, i.e. [(note,color,style)]
# TODO: internal storage of notes to minimize repaint regions. Remote X11 likes this. 

class PianoError(Exception):
	pass

#class Piano:
#	""" This is a class which renders a set of piano piano keys on a gtk.Image. Individual keys can be highlighted. """
#	def __init__(self,image,filename):
#		""" Initialize the piano to draw on a given gtk.Image """
#		black=[(x,42,10,32) for x in [32,68,140,176,211]]
#		white=[(x,100,20,32) for x in [8,44,80,116,152,188,224]]
#		self.keys=[white[0],black[0],white[1],black[1],white[2],white[3],black[2],white[4],black[3],white[5],black[4],white[6]]
#		self.keys+=[(x+252,y,w,h) for (x,y,w,h) in self.keys]+[(x+504,y,w,h) for (x,y,w,h) in self.keys]
#
#		self.image=image
#		self.pianoimage=gtk.gdk.pixbuf_new_from_file(filename)
#		self.pianocanvas=gtk.gdk.Pixmap(None,self.pianoimage.get_width(),self.pianoimage.get_height(),24)
#		self.pianocontext=self.pianocanvas.cairo_create()
#		self.image.set_from_pixmap(self.pianocanvas,None)
#		self.draw()
#
#	def draw(self,notes=[]):
#		""" Draw a list of highlighted notes on the piano """
#		self.pianocontext.new_path()
##		self.pianocontext.set_source_color(self.pianoroll.style.bg[gtk.STATE_NORMAL])
##		self.pianocontext.paint()
#		self.pianocontext.set_source_pixbuf(self.pianoimage,0,0)
#		self.pianocontext.paint()
#		
#		self.pianocontext.set_source_rgb(1, 0, 0)
#		try:
#			for (x,y,w,h) in [self.keys[n] for n in notes]:
#				self.pianocontext.rectangle(x,y,w,h)
#		except IndexError,e:
#			raise PianoError("The given set of notes did not fit on the piano")
#		
#		self.pianocontext.fill()
#		self.image.queue_draw()

class Piano(gtk.Image):
	""" This is a class which renders a set of piano piano keys on a gtk.Image. Individual keys can be highlighted. """
	def __init__(self,filename):
		gtk.Image.__init__(self)
		black=[(x,42,10,32) for x in [32,68,140,176,211]]
		white=[(x,100,20,32) for x in [8,44,80,116,152,188,224]]
		self.keys=[white[0],black[0],white[1],black[1],white[2],white[3],black[2],white[4],black[3],white[5],black[4],white[6]]
		self.keys+=[(x+252,y,w,h) for (x,y,w,h) in self.keys]+[(x+504,y,w,h) for (x,y,w,h) in self.keys]

		self.pianoimage=gtk.gdk.pixbuf_new_from_file(filename)
		self.pianocanvas=gtk.gdk.Pixmap(None,self.pianoimage.get_width(),self.pianoimage.get_height(),24)
		self.pianocontext=self.pianocanvas.cairo_create()
		self.set_from_pixmap(self.pianocanvas,None)
		self.set_size_request(self.pianoimage.get_width(),self.pianoimage.get_height())
		self.draw()

	def draw(self,notes=[]):
		""" Draw a list of highlighted notes on the piano """
		self.pianocontext.new_path()
#		self.pianocontext.set_source_color(self.pianoroll.style.bg[gtk.STATE_NORMAL])
#		self.pianocontext.paint()
		self.pianocontext.set_source_pixbuf(self.pianoimage,0,0)
		self.pianocontext.paint()
		
		self.pianocontext.set_source_rgb(1, 0, 0)
		try:
			for (x,y,w,h) in [self.keys[n] for n in notes]:
				self.pianocontext.rectangle(x,y,w,h)
		except IndexError,e:
			raise PianoError("The given set of notes did not fit on the piano")
		
		self.pianocontext.fill()
		self.queue_draw()
