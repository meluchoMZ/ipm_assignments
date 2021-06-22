##!/usr/bin/env python3

import gi
import utils
import sys
import threading
import concurrent.futures

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

import sys
class View1():

	def __init__ (self):
		
		
		self.window = Gtk.Window(title = 'default')
		self.window.set_default_icon_from_file('./resources/icon2.png')
		self.intervalos_musicales_store = None
		self.asc_desc_store = None
		self.vbox = None
		self.greetings = None
		self.hbox = None
		self.intervalos = None
		self.asc_desc = None
		self.format_long = True
		self.buscar = None
		self.image_find = None
		self.menu_formato = None
		self.boton_normal = None
		self.boton_corto = None
		self.vbox2 = None
		self.vbox3 = None
		self.separator=None
		self.titulo_recientes = None
		self.lista_intervalos_recientes = []
		
		
	def start(self):
		Gtk.main()

	def show(self):
		self.window.show_all()

	def set_boxes(self):
		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.vbox.pack_start(self.greetings, False, False, 0)
		self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		self.vbox.pack_start(self.hbox,True, False,0)
		
		self.window.add(self.vbox)

		self.hbox.pack_start(self.boton_formato, False, True, 0)

		self.hbox.pack_start(self.intervalos, True, False, 10)

		self.hbox.pack_start(self.asc_desc, True, False ,40)

		self.hbox.pack_start(self.buscar, False, False,0)

		self.menu_formato = Gtk.Popover()

		self.vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.vbox2.pack_start(self.boton_normal, False, True, 10)
		self.vbox2.pack_start(self.boton_corto, False, True, 10)
		self.menu_formato.add(self.vbox2)
		self.menu_formato.set_position(Gtk.PositionType.BOTTOM)

		self.vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.vbox.pack_start(self.vbox3,True,True,0)

		self.separator=Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
		self.vbox3.pack_start(self.separator, True, True, 8)

		self.vbox3.pack_start(self.titulo_recientes, True, True, 0)


	def set_window(self, title):
		self.window.set_title(title)
		self.window.set_border_width(50)
		self.window.set_default_size(500, 300)
		self.window.connect('delete-event',Gtk.main_quit)

	def get_format(self):
		return self.format_long

	def set_greetings_markup(self,greet):
		self.greetings = Gtk.Label()
		self.greetings.set_markup('<big><b>'+greet+'</b></big>')

	def set_boton_formato(self,icon,IconSize):
		self.boton_formato = Gtk.Button.new_from_icon_name(icon,IconSize)
		self.boton_formato.connect('clicked', self.desplegar_menu_formato)

	def set_titulos_recientes(self,label):
		self.titulo_recientes = Gtk.Label()	
		self.titulo_recientes.set_markup('<b>'+label+'</b>')

	def set_stores(self):
		self.intervalos_musicales_store = Gtk.ListStore(str, str)
		self.asc_desc_store = Gtk.ListStore(str,str)	

	def set_boton_buscar(self, handler):
		self.buscar = Gtk.Button()
		self.image_find = Gtk.Image()
		self.image_find.set_from_stock(Gtk.STOCK_FIND, Gtk.IconSize.BUTTON)
		self.buscar.set_image(self.image_find)
		self.buscar.connect('clicked',handler)	

	def set_boton_normal(self,label):
		self.boton_normal = Gtk.ModelButton()
		self.boton_normal.set_label(label)
		self.boton_normal.connect("clicked", self.cambiar_formato_largo)	

	def set_boton_corto(self,label):
		self.boton_corto = Gtk.ModelButton()
		self.boton_corto.set_label(label)
		self.boton_corto.connect("clicked", self.cambiar_formato_corto)

	def set_vistas_recientes (self):
		for i in range(0,4):
			label=Gtk.Label()
			self.vbox3.pack_start(label, False, False, 2)
			self.lista_intervalos_recientes.append(label)	

	def pasar_lista_store (self,store, lista):
		intmus = []
		for i in lista:
			intmus.append((i[0], i[1]))
		self.add_list(store, intmus)

	def set_combo_intervalos (self,model):
		self.intervalos = Gtk.ComboBox.new_with_model_and_entry(model)
		self.intervalos.set_entry_text_column(1)

	def set_combo_asc_desc(self,model):	
		self.asc_desc = Gtk.ComboBox.new_with_model_and_entry(model)
		self.asc_desc.set_entry_text_column(1)	

	#Funcion para añadir los items a las list store
	def add_list(self,widget,list):
		for i in list :
			widget.append(i)    

	def desplegar_menu_formato(self, button):
		self.menu_formato.set_relative_to(button)
		self.menu_formato.show_all()
		self.menu_formato.popup()		

	def cambiar_formato_largo(self,num):
		self.asc_desc.set_entry_text_column(1)
		self.intervalos.set_entry_text_column(1)  
		actint, actdir = self.intervalos.get_active(), self.asc_desc.get_active()
		self.intervalos.set_active(-1)
		self.asc_desc.set_active(-1)
		self.intervalos.set_active(actint)
		self.asc_desc.set_active(actdir)
		self.format_long=True

	#Funcion para cambiar el formato a corto, primer objeto de las tuplas de las opciones de búsqueda
	def cambiar_formato_corto(self,num):
		self.asc_desc.set_entry_text_column(0)
		self.intervalos.set_entry_text_column(0)
		actint, actdir = self.intervalos.get_active(), self.asc_desc.get_active()
		self.intervalos.set_active(-1)
		self.asc_desc.set_active(-1)
		self.intervalos.set_active(actint)
		self.asc_desc.set_active(actdir)
		self.format_long=False

	def on_clicked_buscar(self, handler):
		self.buscar.connect('clicked', handler)
	
	def get_combobox_status(self):
		return self.intervalos.get_active(), self.asc_desc.get_active()

	def mostrar_error(self, message):
		dialog = Gtk.MessageDialog(parent=self.window, message_type=Gtk.MessageType.ERROR, buttons=Gtk.ButtonsType.OK, text=message)
		dialog.run()
		dialog.destroy()

	def actualizar_lista_recientes(self, lista):
		top = 0
		for label in self.lista_intervalos_recientes:
			if top == len(lista):
				break
			label.set_label(lista[top])
			top = top+1
