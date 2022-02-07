from odoo import models, fields, api

class customerinvoice(models.Model):
    _inherit = 'account.move'
    
    ##---------------------------------Methods--------------------------------- 
    def apicall(self):
        for record in self:
            ## Retreieve communication arrangement
            arrangement = self.env['cockpit_integration.com_arrangement'].search([('operation', '=', 'New_Material_ByD')]) 
            ## Define body
            body = {
                "InternalID":"TEST08",
                "ProductCategoryInternalID":"192"
            }
            ## call _api_launch_post method from communication arrangement
            answer = arrangement._api_launch_post(body, record.id)

