from odoo import models, fields, api
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import date

class com_arrangement(models.Model):
    ##---------------------------------Fields---------------------------------
    _name = 'cockpit_integration.com_arrangement'
    _description = 'Communication arrangement'
    ##DEV-01-DB-03-01 		 ID 
    ##id = fields.Integer(string='ID')
    ##DEV-01-DB-03-02 		 Opération 
    operation = fields.Char()
    ##DEV-01-DB-03-03 		 Status 
    status = fields.Selection([('A', 'Active'), ('I', 'Inactive')], string='Status')
    ## Direction
    direction = fields.Selection([('IN', 'Inbound'), ('OU', 'Outbound')], string='Direction')
    ## DEV-01-DB-03-04 		 Endpoint (URL) 
    endpoint = fields.Char(string='Endpoint (URL)')
    ## DEV-01-DB-03-05 		 Format 
    formats = fields.Selection([('JS', 'JSON'), ('XM', 'XML'), ('SO', 'SOAP')], string='Format')
    ## DEV-01-DB-03-06 		 Modèle d'identification 
    identification = fields.Selection([('USR', 'User/password')], string='Identification')
    ## DEV-01-DB-03-07 		 User 
    user = fields.Char(string='User')
    ## DEV-01-DB-03-08 		 Password 
    password = fields.Char(string='Password')
    ## DEV-01-DB-03-09 		 Contact d'échec (Nom Prénom) 
    failContact = fields.Char(string='Fail contact Name')
    ## DEV-01-DB-03-10 		 Contact d'échec (Email) 
    failEmail = fields.Char(string='Fail contact Email')
    ## originDocType
    originDocType = fields.Char(string='Origin document type')
    ## Need for token
    needToken = fields.Boolean(string='Need to get token first')
    ## DEV-01-DB-05 		 Com Headers 
    headers = fields.One2many('cockpit_integration.com_header', 'arrangement', string = 'Header')
    
    ##---------------------------------Methods---------------------------------
    ## DEV-01-AC-03-01 		L'opération doit être unique
    _sql_constraints = [
        ('uniq_operation', 'unique(operation)', "A communication arrangement already exists with this operation. Operation must be unique!"),
    ]
    
    ## Appel d'API
    def _api_launch_post(self, body, originDocId):
        for record in self:
            ##DEV-01-AC-04-01 		URL correspond au endpoint du communication arrangement
            url = self.endpoint
            ##DEV-01-AC-04-02 		Le user correspond au user du communication arrangement
            user = self.user
            ##DEV-01-AC-04-03 		Le password correspond au password du communication arrangement
            pwd = self.password
            ## DEV-01-AC-04-04 		Les headers sont ceux du communication arrangement
            requHeaders = {}
            for header in self.headers:
                requHeaders[header.key] = header.value
            ## body
            json_data = body 
            ## API POST call
            response = requests.post(url, data=json.dumps(json_data), auth=HTTPBasicAuth(user, pwd), headers=requHeaders)

                        ##DEV-01-AC-01 	3	 Création du tracking 
            if (response.ok):
                status = 'Success'
            else:
                status = 'Error'
            self.env['cockpit_integration.track'].create(
            {
                'status' : status,
                'originDocId' : originDocId, ##!!!!!!!!!!!!!!!!!!!
                'originDocType' : self.originDocType,##!!!!!!!!!!!!!!!!!!!
                'direction' : self.direction,
                'operation' : self.operation,
                'targetUrl' : url,
                'date' : fields.datetime.now(),
                'returnCode' : response.status_code,
                'requestHeader' : requHeaders,
                'requestBody' : json_data
            }
            )
            
            ## give back api call response
            return response

        
        

    
class com_header(models.Model):
    ##---------------------------------Fields---------------------------------
    _name = 'cockpit_integration.com_header'
    _description = 'Header'
    arrangement = fields.Many2one('cockpit_integration.com_arrangement', string = 'Arrangement') 
    ## DEV-01-DB-05-01 		 Key 
    key = fields.Char(string = 'Key')
    ##  DEV-01-DB-05-02 		 Value 
    value = fields.Char(string = 'Value')