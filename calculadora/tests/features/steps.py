# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import calculadora

@step(u'Dado que tengo el numero "([^"]*)" y "([^"]*)"')
def dado_que_tengo_los_operados_group1_y_group1(step, num1, num2):
    cal = Calculadora()
    world.resultado = cal.suma(int(num1), int(num2))

@step(u'cuand realizo la suma')
def cuand_realizo_la_suma(step):
    pass

@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_group1(step, esperado):
    assert int(esperado) == world.resultado, 'El resultado '+esperado+ 'no es ' + str(world.resultado)
