# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sah_badailtech(models.Model):
#     _name = 'sah_badailtech.sah_badailtech'
#     _description = 'sah_badailtech.sah_badailtech'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
