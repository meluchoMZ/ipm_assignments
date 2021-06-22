#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import view1
import model1
import controller2
import threading
import concurrent.futures
import locale
import gettext
from pathlib import Path

_ = gettext.gettext

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class Controller1:
	
	# constructor
	def __init__(self):

		locale.setlocale(locale.LC_ALL,'')

		LOCALE_DIR = Path(__file__).parent /"locale"
		locale.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.textdomain('EMusicLearner')

		self.model = model1.Model1()

		self.view = view1.View1()
		threading.Thread(target=self.start, daemon=True).start()
		self.view.start()	

	def start(self):
		try:
			self.model.start_model()
		except:
			GLib.idle_add(self.view.mostrar_error, _("No se puede conectar al servidor. Inténtelo más tarde"))
			GLib.idle_add(Gtk.main_quit)
			return None

		GLib.idle_add(self.start_view)

		try:
			self.model.actualizar_recientes()
		except: 
			GLib.idle_add(self.view.mostrar_error, _("Error al actualizar la lista de intervalos recientes"))
			return None
		
		GLib.idle_add(self.view.actualizar_lista_recientes, self.model.lista_recientes)

	def start_view(self):	
		
		self.view.set_window("EMusicLearner")
		self.view.set_greetings_markup(_("SELECCIONE UN INTERVALO Y SU DIRECCIÓN"))
		self.view.set_boton_formato("document-properties",2)
		self.view.set_titulos_recientes(_("Intervalos recientes"))
		self.view.set_stores()
		self.view.set_boton_buscar(self.buscar_handler)
		self.view.pasar_lista_store(self.view.intervalos_musicales_store,self.model.intervalos_musicales)
		self.view.pasar_lista_store(self.view.asc_desc_store,self.model.asc_des_list)
		self.view.set_boton_normal(_("Formato normal"))
		self.view.set_boton_corto(_("Formato corto"))
		self.view.set_combo_intervalos(self.view.intervalos_musicales_store)
		self.view.set_combo_asc_desc(self.view.asc_desc_store)
		self.view.set_boxes()
		self.view.set_vistas_recientes()
		#actualizar as vistas recientes
		self.view.show()

	def buscar_handler(self, button):
		i,ad = self.view.get_combobox_status()
		reti, retad, title, url, path = self.model.get_int_length_dir(i, ad, self.view.get_format())
		# Condicións de fallo
		if reti is None and retad is None:
			self.view.mostrar_error(_("Por favor, seleccione un intervalo y su dirección"))
			return None
		if reti is None:
			self.view.mostrar_error(_("Por favor, seleccione un intervalo"))
			return None
		if retad is None:
			self.view.mostrar_error(_("Por favor, seleccione la dirección del intervalo seleccionado"))
			return None
		
		controller2.Controller2(self.view, url, path, title, retad=="asc", reti)

		# actualizar ficheiro
		try:
			threading.Thread(target=self.asinc_actualizar, args=(title, reti,), daemon=True).start()
		except:
			self.view.mostrar_error(_("Error al actualizar la lista de intervalos recientes"))
			return None


	def asinc_actualizar(self, title, length):
		try:
			self.model.actualizar_ficheiro(title, length)
		except:
			GLib.idle_add(self.view.mostrar_error, _("Error al actualizar la lista de intervalos recientes"))
			return None
		# xa teño o modelo actualizado
		GLib.idle_add(self.view.actualizar_lista_recientes, self.model.lista_recientes)
