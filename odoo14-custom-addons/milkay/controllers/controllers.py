# -*- coding: utf-8 -*-
# from odoo import http


# class Milkay(http.Controller):
#     @http.route('/milkay/milkay/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/milkay/milkay/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('milkay.listing', {
#             'root': '/milkay/milkay',
#             'objects': http.request.env['milkay.milkay'].search([]),
#         })

#     @http.route('/milkay/milkay/objects/<model("milkay.milkay"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('milkay.object', {
#             'object': obj
#         })
