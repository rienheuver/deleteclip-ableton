#DeleteClip.py
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface # Central base class for scripts based on the new Framework
from _Framework.ButtonElement import ButtonElement # Class representing a button on the controller
from _Framework.InputControlElement import * # for MIDI_NOTE_TYPE

IS_MOMENTARY = True
STATUS_MASK = 0xF0
CHAN_MASK =  0x0F

class DeleteClip(ControlSurface):

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self.log_message("DeleteClip started")
            self.show_message('DeleteClip started')
            self.DeleteButton = ButtonElement(IS_MOMENTARY, MIDI_NOTE_TYPE, 8, 39)
            self.DeleteButton.add_value_listener(self._delete_clip,identify_sender= False)
    
    def _delete_clip(self, value):
        self.log_message('Deleting clip')
        CurrentSlot = self.song().view.highlighted_clip_slot
        if CurrentSlot.has_clip:
            CurrentSlot.delete_clip()
