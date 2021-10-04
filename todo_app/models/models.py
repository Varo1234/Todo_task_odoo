# -*- coding: utf-8 -*-
from odoo import models, fields, api


class aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'

    name = fields.Char('Direccion', required=True)
    plazas = fields.Integer(string='Plazas', required=True)

    # relaciones entre tablas
    coche_ids = fields.One2many('garaje.coche', 'aparcamiento_id', string='coches')


class coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas de un coche'
    _order = 'name'

    name = fields.Char(string='Matricula', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de construccion', required=True)
    consumo = fields.Float('Consumo', (4, 1), default=0.0)
    averiado = fields.Boolean(string='Averiado',default=False)
    # store=True no es conventiente en este caso
    annos = fields.Integer('Años', compute='_get_años', store=True)
    descripcion = fields.Text('Descripción')

    # relaciones entre tablas
    aparcamiento_id = fields.Many2one(
        'garaje.aparcamiento', string='Aparcamiento')
    mantenimiento_ids = fields.Many2many(
        'garaje.mantenimiento', string='Mantenimientos')

    @api.depends('construido')
    def _get_annos(self):
        # TODO: lo dejamos para mas adelante
        for coche in self:
            coche.annos = 0


class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir mantenimientos rutinarios sobre los coches'
    _order = 'fecha'

    # name = fields.Char()
    fecha = fields.Date('fecha', required=True, defaul=fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[
        ('l', 'Lavar'), ('r', 'Revision'), ('m', 'Mecanica'), ('p', 'Pintura')], default='l')
    coste = fields.Float('Coste', (8, 2), help='Coste total del mantenimiento')

    # relaciones entre tablas
    coche_ids = fields.Many2many('garaje.coche', string='Coches')
