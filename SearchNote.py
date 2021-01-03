#DeleteClip.py
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface # Central base class for scripts based on the new Framework
from _Framework.ButtonElement import ButtonElement # Class representing a button on the controller
from _Framework.InputControlElement import * # for MIDI_NOTE_TYPE

IS_MOMENTARY=True
STATUS_MASK = 0xF0
CHAN_MASK =  0x0F

class DeleteClip(ControlSurface):

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
        	self.log_message("DeleteClip started")
		self.buttons = []
		for channel in range(16):
      for note in range(128):
        button = ButtonElement(IS_MOMENTARY, MIDI_NOTE_TYPE, channel, note)
              button.add_value_listener(self._delete_clip,identify_sender= False)
        self.buttons.append(button)
    
    def _delete_clip(self, value):
        self.log_message('Deleting clip')

    def receive_midi(self, midi_bytes):
        channel = (midi_bytes[0] & CHAN_MASK)
        status = (midi_bytes[0] & STATUS_MASK)
        key = midi_bytes[1]
        value = midi_bytes[2]

	      self.log_message("receive_midi on channel %d, status %d, key %d, value %d" % (channel, status, key, value))
