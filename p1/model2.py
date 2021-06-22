# CLASS MODEL2 (mvc for the second activity of the app) task 5
# Authors:
# Miguel Blanco Godón (MiguelBlancoGodon)
# Christian David Outeda García (chrisouteda)

import utils
import concurrent.futures
import locale
import gettext
from pathlib import Path
_ = gettext.gettext

# this class implements the backend part of the application
class Model2:
	
	# class constructor
	def __init__(self, url, path):

		locale.setlocale(locale.LC_ALL,'')

		LOCALE_DIR = Path(__file__).parent /"locale"
		locale.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.textdomain('EMusicLearner')

		# song list
		self.songs = None
		sharp = u"\u266f"
		self.resources = path
		self.url = url
		# list of possible notes
		self.notes = notes = [ 
					(_('Do'), self.resources+'DO.png', self.resources+'DO2.png'), 
					(_('Do')+sharp, self.resources+'DOs.png', self.resources+'DOs2.png'),
					(_('Re'), self.resources+'RE.png', self.resources+'RE2.png'),
					(_('Re')+sharp, self.resources+'REs.png', self.resources+'REs2.png'),
					(_('Mi'), self.resources+'MI.png', self.resources+'MI2.png'),
					(_('Fa'), self.resources+'FA.png', self.resources+'FA2.png'),
					(_('Fa')+sharp, self.resources+'FAs.png', self.resources+'FAs2.png'),
					(_('Sol'), self.resources+'SOL.png', self.resources+'SOL2.png'),
					(_('Sol')+sharp, self.resources+'SOLs.png', self.resources+'SOLs2.png'),
					(_('La'), self.resources+'LA.png', self.resources+'LA2.png'),
					(_('La')+sharp, self.resources+'LAs.png', self.resources+'LAs2.png'),
					(_('Si'), self.resources+'SI.png', self.resources+'SI2.png')
				]
	
	def obtain_songs(self):
		self.songs = utils.get_json_from_url(self.url)

	# note selector algorithm
	def compute_notes(self, asc, length):
		# for simplicity we'll assume fst always 0
		fst = 0
		if asc:
			snd = (fst+length)%12
		else:
			snd = (fst-length)%12
		return (self.notes[fst][0], self.notes[snd][0])
	
	# image selectr algorithm
	def compute_images(self, asc, length):
		# for simplicity we'll assume fst always 0
		fst = 0
		if asc:
			snd = (fst+length)%12
		else:
			snd = (fst-length)%12

		#left image (li); right image (ri)
		if asc:
			li = self.notes[fst][1]
			if fst+length >= 12:
				# needs higher octave
				ri = self.notes[snd][2]
			else:
				ri = self.notes[snd][1]
		else:
			ri = self.notes[snd][1]
			if fst-length < 0:
				li = self.notes[fst][2]
			else:
				li = self.notes[fst][1]

		return li,ri

	
	def get_songs(self):
		return self.songs


	def calculate_tones(self, flong, length):                                                         
		l = ""
		ton = length//2
		hton = length%2
		if ton is not 0:
			if ton is 1:
				l = l+str(ton)+_(" tono")
			else:
				l = l+str(ton)+_(" tonos")
		if l == "":
			if hton is not 0:
				l = l+str(hton)+ _(" semitono")
		else:
			if hton is not 0:
				l = l+_(" y ")+str(hton)+_(" semitono")
		return l

