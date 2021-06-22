# CLASS VIEW2 (mvc for the second activity of the app) task_5
# Authors: 
# Miguel Blanco Godón (MiguelBlancoGodon)
# Christian David Outeda García (chrisouteda)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import locale
import gettext
_ = gettext.gettext

class View2:

	# class constructor
	# the view is completely passive
	# we tried to made it the most dependency free that we could
	def __init__(self):
		
		self.window = Gtk.Window(title='default')
		# TO BE SET FROM OUT

		# VBOX so we can pack more than one item
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.window.add(vbox)

		# Widgets
		self.interval_name_label = Gtk.Label(label='default')
		vbox.pack_start(self.interval_name_label, expand=False, fill=False, padding=16)
		# Interval tones and hemitones
		self.tones = Gtk.Label('tones')
		vbox.pack_start(self.tones, expand=True, fill=False, padding=0)
		
		# Gtk Frame for images and names
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		vbox.pack_start(hbox, expand=True, fill=False, padding=0)
		vbox.set_spacing(0)

		self.left_frame = Gtk.Frame()
		self.right_frame = Gtk.Frame()
		
		hbox.pack_start(self.left_frame, expand=False, fill=False, padding=0)
		hbox.pack_start(self.right_frame, expand=False, fill=False, padding=0)
		hbox.set_homogeneous(True)

		# images
		self.left_image = Gtk.Image()

		self.right_image = Gtk.Image()

		labelhbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		vbox.pack_start(labelhbox, expand=True, fill=True, padding=0)
		# label for related songs
		self.related_songs_label = Gtk.Label(label='default')
		# set markup dende model
		labelhbox.pack_start(self.related_songs_label, expand=True, fill=False, padding=8)
		self.favourites = Gtk.Label(label='default')
		# set markup dende model
		labelhbox.pack_start(self.favourites, expand=False, fill=False, padding=75)


		# Songs menu:
		scrolled_window = Gtk.ScrolledWindow()
		vbox.pack_start(scrolled_window, expand=True, fill=True, padding=0)
		self.songsvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		scrolled_window.add(self.songsvbox)
		scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

		# Implements related songs from function
	
	# in order to start any graphical component, we have to start Gtk library
	# this should be the last method called on de view
	def start(self):
		GLib.idle_add(self.window.show_all)


	# various setters
	
	def set_window_title(self, title):
		self.window.set_title(title)

	def set_window_icon(self, icon_path):
		self.window.set_default_icon_from_file(icon_path)

	def set_tones(self, tones):
		self.tones.set_label(tones)
	def set_interval_name(self, name):
		self.interval_name_label.set_markup("<big><b>"+_(name)+"</b></big>")

	def set_left_note(self, note):
		self.left_frame.set_label(note)
		self.left_frame.set_label_align(0.5, 0.5)
	
	def set_right_note(self, note):
		self.right_frame.set_label(note)
		self.right_frame.set_label_align(0.5, 0.5)

	def set_left_image(self, image_path):
		self.left_image.set_from_file(image_path)
		self.left_frame.add(self.left_image)

	def set_right_image(self, image_path):
		self.right_image.set_from_file(image_path)
		self.right_frame.add(self.right_image)
	
	def set_songs_separator_label(self, lable):
		self.related_songs_label.set_markup('<b>'+_(lable)+'</b>')

	def set_favourites(self, strfav):
		self.favourites.set_markup('<b>'+_(strfav)+'</b>')

	# For fulfill with songs the songs list
	def fill_with_songs(self, songs_list):
		for (song, link, fav) in songs_list:
			# add a hbox to vbox inside scrolled window
			fhbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
			self.songsvbox.pack_start(fhbox, expand=True, fill=True, padding=0)
			# add a vbox inside hbox to show title and link to the song
			fvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
			fhbox.pack_start(fvbox, expand=True, fill=False, padding=0)
			# Song title
			songlabel = Gtk.Label(label=song)
			fvbox.pack_start(songlabel, expand=True, fill=True, padding=4)
			# Song link
			songlink = Gtk.LinkButton(uri=link, label=_('Escúchame!'))
			fvbox.pack_start(songlink, expand=True, fill=True, padding=4)
			# Fav
			favlabel = Gtk.Label()
			favlabel.set_markup('<b>'+_(fav)+'</b>')
			fhbox.pack_start(favlabel, expand=False, fill=False, padding=80)


	def mostrar_error(self, error):
		dialog = Gtk.MessageDialog(parent=self, message_type=Gtk.MessageType.ERROR, buttons=Gtk.ButtonsType.OK, text=error)
		dialog.run()
		dialog.destroy()
