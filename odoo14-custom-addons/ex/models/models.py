# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ex(models.Model):
    _name = 'ex.ex'
    _description = 'ex.ex'

    title = fields.Char()
    date = fields.Date()
    score = fields.Float()
    distributor = fields.Char()
    publisher = fields.Char()
    favs = fields.Boolean(compute="_value_favs", store=True)

    @api.depends('score')
    def _value_favs(self):
        for record in self:
            if record.score>75:
                record.favs = True
            else:
                record.favs = False