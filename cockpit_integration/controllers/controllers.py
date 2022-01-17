# -*- coding: utf-8 -*-
# from odoo import http


# class CockpitIntegration(http.Controller):
#     @http.route('/cockpit_integration/cockpit_integration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cockpit_integration/cockpit_integration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cockpit_integration.listing', {
#             'root': '/cockpit_integration/cockpit_integration',
#             'objects': http.request.env['cockpit_integration.cockpit_integration'].search([]),
#         })

#     @http.route('/cockpit_integration/cockpit_integration/objects/<model("cockpit_integration.cockpit_integration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cockpit_integration.object', {
#             'object': obj
#         })
