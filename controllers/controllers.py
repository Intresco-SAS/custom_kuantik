# -*- coding: utf-8 -*-
# from odoo import http


# class CustomKuantik(http.Controller):
#     @http.route('/custom_kuantik/custom_kuantik/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_kuantik/custom_kuantik/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_kuantik.listing', {
#             'root': '/custom_kuantik/custom_kuantik',
#             'objects': http.request.env['custom_kuantik.custom_kuantik'].search([]),
#         })

#     @http.route('/custom_kuantik/custom_kuantik/objects/<model("custom_kuantik.custom_kuantik"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_kuantik.object', {
#             'object': obj
#         })
