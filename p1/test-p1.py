#! /usr/bin/env python3

import gi
gi.require_version('Atspi','2.0')
from gi.repository import Atspi

import sys
import textwrap
from collections import namedtuple

import funciones_test

Ctx = namedtuple("Ctx", "path process app")
# Implementación de funciones de prueba

lista_intervalos = [("2m", "Segunda menor"),("2M", "Segunda mayor"),("3m", "Tercera menor"),("3M", "Tercera mayor"),
("4j", "Cuarta justa"),("4aum", "Cuarta aumentada"),("5j","Quinta justa"),("6m","Sexta menor"),("6M","Sexta mayor"),("7m","Séptima menor"),
("7M", "Séptima mayor")]#,("8a","Octava")]

def lanzar_aplicacion(context):
	process, app = funciones_test.run(context.path)
	assert app is not None
	return Ctx(path = context.path, process = process, app = app)

def veo_titulo(context):
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'frame' and node.get_name()=='EMusicLearner')
	title = next(gen, None)
	assert title and title.get_name(), title.get_name()
	return context	

def veo_greetings(context):
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name()=='label' and node.get_name()=='SELECCIONE UN INTERVALO Y SU DIRECCIÓN')
	label = next(gen, None)
	assert label and label.get_name(), lable.get_name()
	return context

def veo_intervalos_recientes(context):
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_text(0,-1).startswith("Intervalos"))
	label = next(gen, None)
	assert label and label.get_text(0,-1) == "Intervalos recientes", label.get_text(0,-1)
	return context	

def veo_boton_buscar(context):
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'push button' and node.get_name() == "Find")
	push_b = next(gen,None)
	assert push_b and push_b.get_name() == "Find", push_b.get_name()
	return context

def probar_boton_menu_formato(context):
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'push button' and node.get_name() == "Properties")
	push_b = next(gen,None)
	assert push_b is not None
	funciones_test.do_action(push_b,'click')
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'push button' and node.get_name() == "Formato normal")
	item = next(gen,None)
	assert item and item.get_name() == "Formato normal", item.get_name()
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'push button' and node.get_name() == "Formato corto")
	item_corto = next(gen,None)
	assert item_corto and item_corto.get_name() == "Formato corto", item.get_name()
	funciones_test.do_action(item_corto,'click')	
	for i in lista_intervalos:
		gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'menu item' and node.get_name() == i[0])
		lista = next(gen,None)
		assert lista and lista.get_name() == i[0], lista.get_name()	
	funciones_test.do_action(push_b,'click')
	funciones_test.do_action(item,'click')
	for i in lista_intervalos:
		gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'menu item' and node.get_name() == i[1])
		lista = next(gen,None)
		assert lista and lista.get_name() == i[1], lista.get_name()	
	return context				

def uso_combo_inter(context):
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'menu item' and node.get_name() == "Tercera mayor")
	intervalo = next (gen,None)
	assert intervalo and intervalo.get_name() == "Tercera mayor", intervalo.get_name()

	funciones_test.do_action(intervalo, "click")

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'text' and node.get_text(0,-1).startswith("Tercera"))
	label = next(gen, None)
	assert label and label.get_text(0,-1) == "Tercera mayor", label.get_text(0,-1)
	return context

def uso_combo_asc(context):
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'menu item' and node.get_name() == "ascendente")
	intervalo = next (gen,None)
	assert intervalo and intervalo.get_name() == "ascendente", intervalo.get_name()

	funciones_test.do_action(intervalo, "click")

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'text' and node.get_text(0,-1).startswith("ascendente"))
	label = next(gen, None)
	assert label and label.get_text(0,-1) == "ascendente", label.get_text(0,-1)
	return context



def mostrar_arbol(path):
	app_mia = funciones_test.run(path)
	funciones_test.dump_tree(app_mia[1])	

def probar_vista(funcion):
	context = initial_context
	try:
		context = lanzar_aplicacion(context)
		context = funcion(context)
		funciones_test.show_passed()
	except Exception as e:
		funciones_test.show_not_passed(e)
	funciones_test.stop(context.process)

def probar_boton_de_busqueda(context):
	uso_combo_asc(context)
	uso_combo_inter(context)
	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'push button' and node.get_name() == "Find")
	push_b = next(gen,None)
	assert push_b and push_b.get_name() == "Find", push_b.get_name()
	funciones_test.do_action(push_b, 'click')
	import time
	time.sleep(2)

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Tercera mayor ascendente")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Do")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Mi")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Canciones relacionadas")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Favoritos")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "La primavera (Vivaldi)")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Oh when the saints go marching in")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Blister in the sun (Violent Femmes)")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Blue Danube")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Ob-la-di Ob-la-da (The Beatles)")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Kumbaya")
	label = next(gen, None)
	assert label and label.get_name(),  label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "Sweet Child O'Mine - Bass riff intro (Guns N' Roses)")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'push button' and node.get_name() == "Escúchame!")
	push_b = next(gen, None)
	assert push_b and push_b.get_name(), push_b.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "NO")
	label = next(gen, None)
	assert label and label.get_name(), label.get_name()

	gen = (node for _path, node in funciones_test.tree(context.app) if node.get_role_name() == 'label' and node.get_name() == "SI")
	label = next(gen, None)
	assert not (label and label.get_name()), label.get_name()

	return context


if __name__ == '__main__':
	sut_path = sys.argv[1]
	initial_context = Ctx(path = sut_path, process = None, app = None)

	funciones_test.show("""
	GIVEN he lanzado la aplicación
	THEN veo el título "EMusicLearner"
	""")
	probar_vista(veo_titulo)

	funciones_test.show("""
	GIVEN he lanzado la aplicación
	THEN veo el texto "SELECCIONE UN INTERVALO Y SU DIRECCIÓN"
	""")
	probar_vista(veo_greetings)

	funciones_test.show("""
	GIVEN he lanzado la aplicacion
	THEN veo el texto "Intervalos recientes"
	""")
	probar_vista(veo_intervalos_recientes)
	
	funciones_test.show("""
	GIVEN he lanzado la aplicacion
	THEN veo el boton de busqueda
	""")
	probar_vista(veo_boton_buscar)

	funciones_test.show("""
	GIVEN presiono el boton de formato y la opcion formato corto
	THEN veo lista de intervalos disponiblesen formato corto
	GIVEN presiono el boton formato normal
	THEN veo lista de intervalos disponibles en formato normal
	""")
	probar_vista(probar_boton_menu_formato)

	funciones_test.show("""
	GIVEN presiono Tercera mayor
	THEN veo el texto Tercera mayor en el combobox
	""")

	probar_vista(uso_combo_inter)

	funciones_test.show("""
	GIVEN presiono ascendente
	THEN veo el texto ascendente en el combobox
	""")

	probar_vista(uso_combo_asc)

	funciones_test.show("""
	GIVEN he lanzado la aplicación
	WHEN presiono "Tercera mayor"
	WHEN presiono "ascendente"
	WHEN presiono el botón de buscar
	THEN veo la vista del intervalo
	THEN veo el título EMusicLearner2
	THEN veo el texto "Tercera mayor ascendente"
	THEN veo el texto "Do"
	THEN veo el texto "Mi"
	THEN veo el texto "Canciones relacionadas"
	THEN veo el texto "Favoritos"
	THEN veo el texto "La primavera (Vivaldi)"
	THEN veo el texto "Oh when the saints go marching in"
	THEN veo el texto "Blister in the sun (Violent Femmes)
	THEN veo el texto "Blue Danube"
	THEN veo el texto "Ob-la-di Ob-la-da (The Beatles)"
	THEN veo el texto "Kumbaya"
	THEN veo el texto "Sweet Child O'Mine-Bass riff intro (Guns N'Roses)"
	THEN veo el botón "Escúchame!"
	THEN veo el texto "NO"
	THEN no veo el texto "SI"
	""")

	probar_vista(probar_boton_de_busqueda)

	
