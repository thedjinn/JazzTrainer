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

import threading
import time 

import gobject

import portmidizero as pm
from util import falsify

class MidiThread(threading.Thread):
	stopthread=threading.Event()

	def __init__(self,deviceid,handler):
		threading.Thread.__init__(self)
		self.daemon=True
		self.deviceid=deviceid
		self.handler=handler

	def run(self):
		midiin=pm.Input(self.deviceid)
		while not self.stopthread.isSet():
			if not midiin.Poll(): 
				time.sleep(0.001)
				continue
			data=midiin.Read(1)

			timestamp=data[0][1]
			data=data[0][0]
			mtype=data[0]>>4
			channel=data[0]&0x0f
			if mtype==8: # note off
				key=data[1]
				velocity=data[2]
				self.handler.notes.remove(key)
			elif mtype==9: # note on
				key=data[1]
				velocity=data[2]
				self.handler.notes.add(key)
			elif mtype==10: # poly aftertouch
				key=data[1]
				value=data[2]
				pass
			elif mtype==11: # control change
				control=data[1]
				value=data[2]
				pass
			elif mtype==12: # program change
				program=data[1]
				pass
			elif mtype==13: # channel aftertouch
				value=data[1]
				pass
			elif mtype==14: # pitch bend
				value=float(((data[2]<<7)|data[1])-0x2000)/0x2000 # normalize between -1.0 and 1.0
				pass
			elif mtype==15: # system message
				pass # ignore this

			self.handler.resettimer()
		del midiin

	def stop(self):
		self.stopthread.set()

class MidiHandler():
	statedelay=200
	thread=None
	deviceid=-1
	notes=set()
	callback=None
	timerid=None

	def __init__(self):
		pm.Initialize()

	def __del__(self):
		if self.thread:
			self.stopthread()
		pm.Terminate()

	def getinputs(self):
		defaultin=pm.GetDefaultInputDeviceID()
		numdev=pm.CountDevices()
		for loop in range(numdev):
			interf,name,inp,outp,opened=pm.GetDeviceInfo(loop)
			if inp==1:
				yield (name,loop)

	def getoutputs(self):
		defaultout=pm.GetDefaultOutputDeviceID()
		numdev=pm.CountDevices()
		for loop in range(numdev):
			interf,name,inp,outp,opened=pm.GetDeviceInfo(loop)
			if outp==1:
				yield (name,loop)

	def getdevice(self):
		return self.deviceid

	def changedevice(self,newdev):
		if self.thread:
			self.stopthread()
			self.deviceid=newdev
			self.startthread()
		else:
			self.deviceid=newdev

	def changedelay(self,newdelay):
		pass # TODO

	def resettimer(self):
		if self.callback:
			if self.timerid is not None:
				gobject.source_remove(self.timerid)
			self.timerid=gobject.timeout_add(self.statedelay,falsify(self.callback,self.notes))

	def startthread(self):
		if self.thread==None:
			self.thread=MidiThread(self.deviceid,self)
			self.thread.start()

	def stopthread(self):
		if self.thread:
			self.thread.stop()
			self.thread.join()
			del self.thread
		if self.timerid is not None:
			gobject.source_remove(self.timerid)
			self.timerid=None
		self.callback=None
