# -*- coding: utf-8 -*-
# from odoo import http


# class Ex(http.Controller):
#     @http.route('/ex/ex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ex/ex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ex.listing', {
#             'root': '/ex/ex',
#             'objects': http.request.env['ex.ex'].search([]),
#         })

#     @http.route('/ex/ex/objects/<model("ex.ex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ex.object', {
#             'object': obj
#         })
