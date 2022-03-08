# -*- coding: utf-8 -*-
# from odoo import http


# class InfameAvanzado(http.Controller):
#     @http.route('/infame_avanzado/infame_avanzado/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infame_avanzado/infame_avanzado/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infame_avanzado.listing', {
#             'root': '/infame_avanzado/infame_avanzado',
#             'objects': http.request.env['infame_avanzado.infame_avanzado'].search([]),
#         })

#     @http.route('/infame_avanzado/infame_avanzado/objects/<model("infame_avanzado.infame_avanzado"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infame_avanzado.object', {
#             'object': obj
#         })
