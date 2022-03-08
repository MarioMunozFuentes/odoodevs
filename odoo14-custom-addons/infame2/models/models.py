# -*- coding: utf-8 -*-

from odoo import models, fields, api

# from datetime import date
# from turtle import title


class infame2(models.Model):
    _name = 'infame2.infame2'
    _description = 'infame2.infame2'

    title = fields.Char()
    date = fields.Date()
    score = fields.Float()
    distributor = fields.Char()
    publisher = fields.Char()
    favs = fields.Boolean(compute="_value_favs", store=True)

    # ESTE COMPUTO DEPENDE DE LA VARIABLE SCORE
    @api.depends('score')
    # FUNCION PARA CALCULAR EL VALOR DE FAVS
    def _value_favs(self):
        for record in self:
            # SI LA PRIORIDAD ES MAYOR QUE 75, SE CONSIDERA FAVS, EN OTRO CASO NO LO ES
            if record.score>75:
                record.favs = True
            else:
                record.favs = False
