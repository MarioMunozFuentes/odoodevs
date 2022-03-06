# -*- coding: utf-8 -*-

from odoo import models, fields, api # llena los constructores de todos los campos


class milkay(models.Model):
     _name = 'milkay.milkay' #nombre de la base de datos
     _description = 'milkay.milkay'
     

     name = fields.Text()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True) #este campo depende del anterior
     description = fields.Text()
     planet_status = fields.Text()
     mass = fields.Text()
     radius = fields.Text()
     orbital_period = fields.Text()
     angular_distance = fields.Text()
     discovered = fields.Text()
     molecules = fields.Text()
     star_name = fields.Text()
     star_distance = fields.Text()
     star_age = fields.Float()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100
