from odoo import models, fields, api
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import date
class customerinvoice(models.Model):
    _inherit = 'account.move'
    
    def apicall(self):
        for record in self:
            ## Retreieve communication arrangement
            arrangement = self.env['cockpit_integration.com_arrangement'].search([('operation', '=', 'INV_SAGE_01')])            
            ##DEV-01-AC-04-01 		URL correspond au endpoint du communication arrangement
            url = arrangement.endpoint
            ##DEV-01-AC-04-02 		Le user correspond au user du communication arrangement
            user = arrangement.user
            ##DEV-01-AC-04-03 		Le password correspond au password du communication arrangement
            pwd = arrangement.password
            ##Headers
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Catch-Control": "no-cache"}
            ## body
            json_data = {
                "id": record.name,
            }         
            ## API call
            response = requests.post(url, data=json.dumps(json_data), auth=HTTPBasicAuth(user, pwd),headers=headers)
            
            ##DEV-01-AC-01 	3	 Création du tracking 
            self.env['cockpit_integration.track'].create(
            {
                'status' : '',
                'originDocId' : record.id,
                'originDocType' : 'Invoice',
                'direction' : 'OU',
                'operation' : 'INV_SAGE_01',
                'targetUrl' : url,
                'date' : fields.datetime.now(),
                'returnCode' : response.status_code,
                'requestHeader' : headers,
                'requestBody' : json_data
            }
            )