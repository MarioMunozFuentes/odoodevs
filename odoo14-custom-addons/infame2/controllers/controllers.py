# -*- coding: utf-8 -*-
# from odoo import http


# class Infame2(http.Controller):
#     @http.route('/infame2/infame2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infame2/infame2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infame2.listing', {
#             'root': '/infame2/infame2',
#             'objects': http.request.env['infame2.infame2'].search([]),
#         })

#     @http.route('/infame2/infame2/objects/<model("infame2.infame2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infame2.object', {
#             'object': obj
#         })
