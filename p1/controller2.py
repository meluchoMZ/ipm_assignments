# CLASS CONTROLLER2 (controller of the second activity of the app on task_5)
# Authors:
# Miguel Blanco Godón (MiguelBlancoGodon)
# Christian David Outeda García (chrisouteda)

import view2
import model2
import gi
from gi.repository import GLib
import threading
import locale
import gettext
from pathlib import Path

_ = gettext.gettext

class Controller2:
	
	# constructor
	def __init__(self, parent_view, url, path,title, asc, length):

		locale.setlocale(locale.LC_ALL,'')

		LOCALE_DIR = Path(__file__).parent /"locale"
		locale.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.bindtextdomain('EMusicLearner', LOCALE_DIR)
		gettext.textdomain('EMusicLearner')
		
		self.model = model2.Model2(url, path)
		self.view = None
		self.path = path
		self.asc = asc
		self.length = length
		self.title = title
		self.parent = parent_view
		threading.Thread(target=self.start, daemon=True).start()

	def start(self):
		try:
			self.model.obtain_songs()
		except:
			GLib.idle_add(self.parent.mostrar_error, _("Error: no se puede abrir la vista de intervalo"))
			return None
		GLib.idle_add(self.start_view)

	def start_view(self):
		self.view = view2.View2()
		#setearíamos aquí as cousas da view
		self.view.set_window_title("EMusicLearner")
		self.view.set_window_icon(self.path+'icon2.png')
		self.view.set_tones(self.model.calculate_tones(self.asc,self.length))
		self.view.set_interval_name(self.title)
		# obtaining notes
		l,r = self.model.compute_notes(self.asc, self.length)
		self.view.set_left_note(l)
		self.view.set_right_note(r)
		# obtaining images
		li,ri = self.model.compute_images(self.asc, self.length)
		self.view.set_left_image(li)
		self.view.set_right_image(ri)
		self.view.set_songs_separator_label(_("Canciones relacionadas"))
		self.view.set_favourites(_("Favoritos"))
		self.view.fill_with_songs(self.model.get_songs())
		self.view.start()
