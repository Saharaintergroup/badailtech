# -*- coding: utf-8 -*-
# from odoo import http


# class SahBadailtech(http.Controller):
#     @http.route('/sah_badailtech/sah_badailtech/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sah_badailtech/sah_badailtech/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sah_badailtech.listing', {
#             'root': '/sah_badailtech/sah_badailtech',
#             'objects': http.request.env['sah_badailtech.sah_badailtech'].search([]),
#         })

#     @http.route('/sah_badailtech/sah_badailtech/objects/<model("sah_badailtech.sah_badailtech"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sah_badailtech.object', {
#             'object': obj
#         })
