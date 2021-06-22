# This class implements the model of the first view of the app
# Authors:
# Miguel Blanco Godón (MiguelBlancoGodon)
# Christian David Outeda García (chrisouteda)

# -*- coding: utf-8 -*-

import utils
import sys
import threading
import concurrent.futures
import locale
import gettext
from pathlib import Path

_ = gettext.gettext

class Model1:
	
	# Constructor
	def __init__(self):

		locale.setlocale(locale.LC_ALL,'')

		LOCALE_DIR = Path(__file__).parent /"locale"
		locale.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.textdomain('EMusicLearner')

		self.rpath = './resources/'
		self.int_url = 'http://localhost:5000/intervals'
		self.bd_intervalos = {
											'2' : _('Segunda'),
											'3' : _('Tercera'),
											'4' : _('Cuarta'),
											'5' : _('Quinta'),
											'6' : _('Sexta'),
											'7' : _('Séptima'),
											'8' : _('Octava'),
											'M' : _('mayor'),
											'm' : _('menor'),
											'j' : _('justa'),
											'a' : "",
											'aum' : _('aumentada'),
											'1ST' : 1,
											'1T' : 2,
											'1T1ST' : 3,
											'2T' : 4,
											'2T1ST' : 5,
											'3T' : 6,
											'3T1ST' : 7,
											'4T' : 8,
											'4T1ST' : 9,
											'5T' : 10,
											'5T1ST' : 11,
											'6T' : 12
										}
		self.asc_des_list = [("asc", _("ascendente")), ("des", _("descendente"))]
		self.intervalos_musicales = None
		self.lista_recientes = []

	def get_intervalos_musicales(self):
		return self.intervalos_musicales

	def get_orientation_list(self):
		return self.asc_des_list
	
	def get_icon(self):
		return self.rpath+'icon2.png'

	# throws exception
	def start_model(self):
		json = utils.get_json_from_url(self.int_url)
		intlist = utils.get_dict_list(json)
		l = []

		if locale.getdefaultlocale() == ('en_US', 'UTF-8'):
			for i in intlist:
				l.append((i[0], self.bd_intervalos[i[0][1:]]+" "+self.bd_intervalos[i[0][0]], self.bd_intervalos[i[1]]))
		else :
			for i in intlist:
				l.append((i[0], self.bd_intervalos[i[0][0]]+" "+self.bd_intervalos[i[0][1:]], self.bd_intervalos[i[1]]))	
		
		self.intervalos_musicales = l


	def get_int_length_dir(self, active_int, active_dir, flong):
		ret_len, ret_dir = None, None
		title = ""
		if active_int is not -1:
			ret_len = self.intervalos_musicales[active_int][2]
			if flong:
				title = title+self.intervalos_musicales[active_int][1]+" "
			else:
				title = title+self.intervalos_musicales[active_int][0]+" "


		if active_dir is not -1:
			ret_dir = self.asc_des_list[active_dir][0]
			if flong:
				title = title+self.asc_des_list[active_dir][1]
			else:
				title = title+self.asc_des_list[active_dir][0]
		url = 'http://localhost:5000/songs/'+self.intervalos_musicales[active_int][0]+"/"+self.asc_des_list[active_dir][0]
		return ret_len, ret_dir, title, url, self.rpath
		
	def actualizar_recientes(self):
		try:
			fich = open('./resources/recent.txt', 'r')
		except:
			fich = open('./resources/recent.txt', 'w+')
			fich.write('\n')
		finally:
			fich.close()
		
		fich = open('./resources/recent.txt','r')
		linhas = len(fich.readlines())
		tope = min(4, linhas)
		current = 0
		fich.close()
		fich=open('./resources/recent.txt', 'r')
		l = []
		for i in range(0,4):
			if current==tope:
				break
			l.append(fich.readline())
			current=current+1
		fich.close()
		
		self.lista_recientes = l[::-1]

	def actualizar_ficheiro(self, title, dist):
		fich = open('./resources/recent.txt', 'r')
		linhas = len(fich.readlines())
		fich.close()
		if linhas is 4:
			with open('./resources/recent.txt', 'r') as fich:
				datos = fich.read().splitlines(True)
			with open('./resources/recent.txt', 'w') as fich:
				fich.writelines(datos[1:])

		info=title+_(", con una distancia de ")+str(dist/2)+_(" tonos\n")
		with open('./resources/recent.txt', 'a') as fich:
			fich.write(info)

		
		self.actualizar_recientes()

