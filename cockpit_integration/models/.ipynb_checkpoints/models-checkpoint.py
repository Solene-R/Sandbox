# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cockpit_integration(models.Model):
#     _name = 'cockpit_integration.cockpit_integration'
#     _description = 'cockpit_integration.cockpit_integration'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
