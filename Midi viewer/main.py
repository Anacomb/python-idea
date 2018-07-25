from mido import MidiFile, Message, tempo2bpm, tick2second
import pygame
import pygame.midi
from time import sleep

mid = MidiFile('song.mid')

track = []
meta = []

GRAND_PIANO = 0
CHURCH_ORGAN = 19
RHODES = 85

instrument = GRAND_PIANO


def readTempo(meta):
	tempo = int(str(meta[1][1]).replace("tempo=", ""))
	return tempo2bpm(int(tempo))


def play(instrument):
	pygame.init()
	pygame.midi.init()

	port = pygame.midi.get_default_output_id()
	midi_out = pygame.midi.Output(port, 0)

	try:
		midi_out.set_instrument(instrument)

		midi_out.note_on(72,127)
		midi_out.note_on(76,127)
		midi_out.note_on(79,127)
		sleep(0.5)
		midi_out.note_off(72,127)
		midi_out.note_off(76,127)
		midi_out.note_off(79,127)

	finally:
		del midi_out
		pygame.midi.quit()


def read(mid):
	for msg in mid:
		if (not msg.is_meta):
			if (msg.type == 'note_on'):
				track.append(Message('note_on', note=msg.note, velocity=msg.velocity, time=msg.time))
			elif (msg.type == 'note_off'):
				track.append(Message('note_off', note=msg.note, velocity=msg.velocity, time=msg.time))
		else:
			if set_tempo in str(msg) : 
				#trouver le tempo


read(mid)
for k in meta:
	print(k)
