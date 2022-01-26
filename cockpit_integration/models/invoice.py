from odoo import models, fields, api

class customerinvoice(models.Model):
    _inherit = 'account.move'
    
    ##---------------------------------Methods--------------------------------- 
    def apicall(self):
        for record in self:
            ## Retreieve communication arrangement
            arrangement = self.env['cockpit_integration.com_arrangement'].search([('operation', '=', 'INV_SAGE_01')]) 
            ## Define body
            body = {
                "id": record.name,
            }
            ## call _api_launch_post method from communication arrangement
            answer = arrangement._api_launch_post(body, record.id)

