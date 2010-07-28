#
# portmidizero - Python bindings for PortMidi using ctypes.
# Copyright (c) 2007 Grant Yoshida
# With bugfixes from Emil Loer
#
"""
portmidizero is a wrapper for PortMidi.
The PortMidi library provides low-level access to MIDI interfaces.
"""
__version__="0.1"

from ctypes import *
from ctypes.util import find_library
import array
import sys

dll_name = ''
if sys.platform == 'darwin':
    dll_name = 'libportmidi.dylib'
elif sys.platform in ('win32', 'cygwin'):
    dll_name = 'portmidi.dll'
else:
    dll_name = find_library('portmidi')

try:
	lib = CDLL(dll_name)
except OSError:
	raise SystemExit("This program requires the portmidi library.")

null = None
false = 0
true = 1

# portmidi.h

PmError = c_int
# PmError enum
pmNoError = 0
pmHostError = -10000
pmInvalidDeviceId = -9999
pmInsufficientMemory = -9989
pmBufferTooSmall = -9979
pmBufferOverflow = -9969
pmBadPtr = -9959
pmBadData = -9994
pmInternalError = -9993
pmBufferMaxSize = -9992

lib.Pm_Initialize.restype = PmError
lib.Pm_Terminate.restype = PmError

PmDeviceID = c_int

PortMidiStreamPtr = c_void_p
PmStreamPtr = PortMidiStreamPtr
PortMidiStreamPtrPtr = POINTER(PortMidiStreamPtr)

lib.Pm_HasHostError.restype = c_int
lib.Pm_HasHostError.argtypes = [PortMidiStreamPtr]

lib.Pm_GetErrorText.restype = c_char_p
lib.Pm_GetErrorText.argtypes = [PmError]

lib.Pm_GetHostErrorText.argtypes = [c_char_p, c_uint]

pmNoDevice = -1

class PmDeviceInfo(Structure):
    _fields_ = [("structVersion", c_int),
                ("interf", c_char_p),
                ("name", c_char_p),
                ("input", c_int),
                ("output", c_int),
                ("opened", c_int)]

PmDeviceInfoPtr = POINTER(PmDeviceInfo)

lib.Pm_CountDevices.restype = c_int
lib.Pm_GetDefaultOutputDeviceID.restype = PmDeviceID
lib.Pm_GetDefaultInputDeviceID.restype = PmDeviceID

PmTimestamp = c_long
PmTimeProcPtr = CFUNCTYPE(PmTimestamp, c_void_p)
NullTimeProcPtr = cast(null, PmTimeProcPtr)

# PmBefore is not defined

lib.Pm_GetDeviceInfo.argtypes = [PmDeviceID]
lib.Pm_GetDeviceInfo.restype = PmDeviceInfoPtr

lib.Pm_OpenInput.restype = PmError
lib.Pm_OpenInput.argtypes = [PortMidiStreamPtrPtr,
                             PmDeviceID,
                             c_void_p,
                             c_long,
                             PmTimeProcPtr,
                             c_void_p]

lib.Pm_OpenOutput.restype = PmError
lib.Pm_OpenOutput.argtypes = [PortMidiStreamPtrPtr,
                             PmDeviceID,
                             c_void_p,
                             c_long,
                             PmTimeProcPtr,
                             c_void_p,
                             c_long]

lib.Pm_SetFilter.restype = PmError
lib.Pm_SetFilter.argtypes = [PortMidiStreamPtr, c_long]

lib.Pm_SetChannelMask.restype = PmError
lib.Pm_SetChannelMask.argtypes = [PortMidiStreamPtr, c_int]

lib.Pm_Abort.restype = PmError
lib.Pm_Abort.argtypes = [PortMidiStreamPtr]

lib.Pm_Close.restype = PmError
lib.Pm_Close.argtypes = [PortMidiStreamPtr]

PmMessage = c_long

class PmEvent(Structure):
    _fields_ = [("message", PmMessage),
                ("timestamp", PmTimestamp)]

PmEventPtr = POINTER(PmEvent)

lib.Pm_Read.restype = PmError
lib.Pm_Read.argtypes = [PortMidiStreamPtr, PmEventPtr, c_long]

lib.Pm_Poll.restype = PmError
lib.Pm_Poll.argtypes = [PortMidiStreamPtr]

lib.Pm_Write.restype = PmError
lib.Pm_Write.argtypes = [PortMidiStreamPtr, PmEventPtr, c_long]

lib.Pm_WriteShort.restype = PmError
lib.Pm_WriteShort.argtypes = [PortMidiStreamPtr, PmTimestamp, c_long]

lib.Pm_WriteSysEx.restype = PmError
lib.Pm_WriteSysEx.argtypes = [PortMidiStreamPtr, PmTimestamp, c_char_p]

# porttime.h

# PtError enum
PtError = c_int
ptNoError = 0
ptHostError = -10000
ptAlreadyStarted = -9999
ptAlreadyStopped = -9998
ptInsufficientMemory = -9997

PtTimestamp = c_long
PtCallback = CFUNCTYPE(PmTimestamp, c_void_p)

lib.Pt_Start.restype = PtError
lib.Pt_Start.argtypes = [c_int, PtCallback, c_void_p]

lib.Pt_Stop.restype = PtError
lib.Pt_Started.restype = c_int
lib.Pt_Time.restype = PtTimestamp

def Initialize():
    """
    Initialize: call this first
    """
    lib.Pm_Initialize()
    lib.Pt_Start(1, NullTimeProcPtr, null)  # equiv to TIME_START: start timer w/ ms accuracy

def Terminate():
    """
    Terminate: call this to clean up Midi streams when done.
    If you do not call this on Windows machines when you are
    done with MIDI, your system may crash.
    """
    lib.Pm_Terminate()

def GetDefaultInputDeviceID():
    return lib.Pm_GetDefaultInputDeviceID()

def GetDefaultOutputDeviceID():
    return lib.Pm_GetDefaultOutputDeviceID()

def CountDevices():
    return lib.Pm_CountDevices()

def GetDeviceInfo(i):
    """
    GetDeviceInfo(<device number>): returns 5 parameters
    - underlying MIDI API
    - device name
    - TRUE iff input is available
    - TRUE iff output is available
    - TRUE iff device stream is already open
    """
    info_ptr = lib.Pm_GetDeviceInfo(i)
    if info_ptr:
        info = info_ptr.contents
        return info.interf, info.name, info.input, info.output, info.opened

def Time():
    """
    Time() returns the current time in ms
    of the PortMidi timer
    """
    return lib.Pt_Time()

def GetErrorText(err):
    """
    GetErrorText(<err num>) returns human-readable error
    messages translated from error numbers
    """
    return lib.Pm_GetErrorText(err)

def Channel(chan):
    """
    Channel(<chan>) is used with ChannelMask on input MIDI streams.
    Example: to receive input on channels 1 and 10 on a MIDI
             stream called MidiIn:
    MidiIn.SetChannelMask(pm.Channel(1) | pm.Channel(10))

    note: Channel function has been altered from
          the original PortMidi c call to correct for what
          seems to be a bug --- i.e. channel filters were
          all numbered from 0 to 15 instead of 1 to 16.
    """
    return lib.Pm_Channel(chan-1)

def Pt_Time(time_info):
    """
    For compatibility
    """
    return lib.Pt_Time(time_info)

def CheckErr(err):
    if err < 0:
        raise Exception, lib.Pm_GetErrorText(err)

class Output:
    """
    class Output:
    define an output MIDI stream. Takes the form:
      x = pm.Output(MidiOutputDevice, latency)
    latency is in ms.
    If latency = 0 then timestamps for output are ignored.
    """

    def __init__(self, OutputDevice, latency):
        self.i = OutputDevice
        self.midi = PortMidiStreamPtr()

        if latency > 0:
            time_proc = PmTimeProcPtr(Pt_Time)
        else:
            time_proc = NullTimeProcPtr()

        print "Opening MIDI output"

        err = lib.Pm_OpenOutput(byref(self.midi), self.i, null, 0,
                                time_proc, null, latency)
        CheckErr(err)

    def __dealloc__(self):
        print "Closing MIDI output stream and destroying instance"
        err = lib.Pm_Abort(self.midi)
        CheckErr(err)
        err = lib.Pm_Close(self.midi)
        CheckErr(err)

    def Write(self, data):
        """
        Write(data)
          output a series of MIDI information in the form of a list:
               Write([[[status <,data1><,data2><,data3>],timestamp],
                      [[status <,data1><,data2><,data3>],timestamp],...])
          <data> fields are optional
          example: choose program change 1 at time 20000 and
          send note 65 with velocity 100 500 ms later.
               Write([[[0xc0,0,0],20000],[[0x90,60,100],20500]])
          notes:
            1. timestamps will be ignored if latency = 0.
            2. To get a note to play immediately, send MIDI info with
               timestamp read from function Time.
            3. understanding optional data fields:
                 Write([[[0xc0,0,0],20000]]) is equivalent to
                 Write([[[0xc0],20000]])
        """
        if len(data) > 1024: raise IndexError, 'maximum list length is 1024'

        BufferType = PmEvent * 1024
        buffer = BufferType()

        for i, message in enumerate(data):
            msg = message[0]
            if len(msg) > 4 or len(msg) < 1:
                raise IndexError, str(len(msg)) + ' arguments in event list'
            buffer[i].message = 0
            for j, data_part in enumerate(msg):
                buffer[i].message += ((data_part & 0xFF) << (8*j))
            buffer[i].timestamp = message[1]
            print i, " : ", buffer[i].message, " : ", buffer[i].timestamp
        print "writing to midi buffer"
        err = lib.Pm_Write(self.midi, buffer, len(data))
        CheckErr(err)

    def WriteShort(self, status, data1 = 0, data2 = 0):
        """
        WriteShort(status <, data1><, data2>)
         output MIDI information of 3 bytes or less.
         data fields are optional
         status byte could be:
              0xc0 = program change
              0x90 = note on
              etc.
              data bytes are optional and assumed 0 if omitted
         example: note 65 on with velocity 100
              WriteShort(0x90,65,100)
        """
        buffer = PmEvent()

        buffer.timestamp = lib.Pt_Time()
        buffer.message = ((((data2) << 16) & 0xFF0000) | (((data1) << 8) & 0xFF00) | ((status) & 0xFF))
        print "Writing to MIDI buffer"
        err = lib.Pm_Write(self.midi, buffer, 1)
        CheckErr(err)

    def WriteSysEx(self, when, msg):
        """
        WriteSysEx(<timestamp>,<msg>)
        writes a timestamped system-exclusive midi message.
        <msg> can be a *list* or a *string*
        example:
            (assuming y is an input MIDI stream)
            y.WriteSysEx(0,'\\xF0\\x7D\\x10\\x11\\x12\\x13\\xF7')
                              is equivalent to
            y.WriteSysEx(pypm.Time,
            [0xF0, 0x7D, 0x10, 0x11, 0x12, 0x13, 0xF7])
        """

        if type(msg) is list:
            msg = array.array('B', msg).tostring()
        CurTime = lib.Pt_Time()
        err = lib.Pm_WriteSysEx(self.midi, when, msg)
        CheckErr(err)
        while lib.Pt_Time() == CurTime:
            pass


class Input:
    """
    class Input:
      define an input MIDI stream. Takes the form:
          x = pm.Input(MidiInputDevice)
    """

    def __init__(self, InputDevice):
        self.i = InputDevice
        self.midi = PortMidiStreamPtr()

        err = lib.Pm_OpenInput(byref(self.midi), self.i, null, 100,
                               NullTimeProcPtr, null)
        CheckErr(err)
        print "MIDI input opened"

    def __del__(self):
        print "Closing MIDI input stream and destroying instance"
        #err = lib.Pm_Abort(self.midi)
        #CheckErr(err)
        err = lib.Pm_Close(self.midi)
        CheckErr(err)

    def SetFilter(self, filters):
        """
        SetFilter(<filters>) sets filters on an open input stream
        to drop selected input types. By default, only active sensing
        messages are filtered. To prohibit, say, active sensing and
        sysex messages, call
        SetFilter(stream, FILT_ACTIVE | FILT_SYSEX);

        Filtering is useful when midi routing or midi thru functionality
        is being provided by the user application.
        For example, you may want to exclude timing messages
        (clock, MTC, start/stop/continue), while allowing note-related
        messages to pass. Or you may be using a sequencer or drum-machine
        for MIDI clock information but want to exclude any notes
        it may play.

        Note: SetFilter empties the buffer after setting the filter,
        just in case anything got through.
        """

        buffer = PmEvent()

        err = lib.Pm_SetFilter(self.midi, filters)
        CheckErr(err)

        while lib.Pm_Poll(self.midi) != 0:
            err = Pm_Read(self.midi, buffer, 1)
            CheckErr(err)

    def SetChannelMask(self, mask):
        """
        SetChannelMask(<mask>) filters incoming messages based on channel.
        The mask is a 16-bit bitfield corresponding to appropriate channels
        Channel(<channel>) can assist in calling this function.
        i.e. to set receive only input on channel 1, call with
        SetChannelMask(Channel(1))
        Multiple channels should be OR'd together, like
        SetChannelMask(Channel(10) | Channel(11))
        note: PyPortMidi Channel function has been altered from
              the original PortMidi c call to correct for what
              seems to be a bug --- i.e. channel filters were
              all numbered from 0 to 15 instead of 1 to 16.
        """
        err = lib.Pm_SetChannelMask(self.midi, mask)
        CheckErr(err)

    def Poll(self):
        """
        Poll tests whether input is available,
        returning TRUE, FALSE, or an error value.
        Raises an exception on error.
        """
        err = lib.Pm_Poll(self.midi)
        CheckErr(err)
        return err

    def Read(self, length):
        """
        Read(length): returns up to <length> midi events stored in
        the buffer and returns them as a list:
        [[[status,data1,data2,data3],timestamp],
         [[status,data1,data2,data3],timestamp],...]
        example: Read(50) returns all the events in the buffer,
                 up to 50 events.
        """
        BufferType = PmEvent * 1024;
        buffer = BufferType()

        if length > 1024: raise IndexError, 'maximum buffer length is 1024'
        if length < 1: raise IndexError, 'minimum buffer length is 1'
        num_events = lib.Pm_Read(self.midi, buffer, length)
        CheckErr(num_events)
        x = []
        for loop in range(num_events):
            part = buffer[loop]
            x.append([[part.message & 0xff, (part.message >> 8) & 0xFF,
                       (part.message >> 16) & 0xFF, (part.message >> 24) & 0xFF],
                        part.timestamp])
        return x

# Filters
FILT_ACTIVE=0x1
FILT_SYSEX=0x2
FILT_CLOCK=0x4
FILT_PLAY=0x8
FILT_F9=0x10
FILT_TICK=0x10
FILT_FD=0x20
FILT_UNDEFINED=0x30
FILT_RESET=0x40
FILT_REALTIME=0x7F
FILT_NOTE=0x80
FILT_CHANNEL_AFTERTOUCH=0x100
FILT_POLY_AFTERTOUCH=0x200
FILT_AFTERTOUCH=0x300
FILT_PROGRAM=0x400
FILT_CONTROL=0x800
FILT_PITCHBEND=0x1000
FILT_MTC=0x2000
FILT_SONG_POSITION=0x4000
FILT_SONG_SELECT=0x8000
FILT_TUNE=0x10000
