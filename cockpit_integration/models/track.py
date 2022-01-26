from odoo import models, fields, api
import json
import requests
from requests.auth import HTTPBasicAuth

class track(models.Model):
    ##---------------------------------Fields---------------------------------
    _name = 'cockpit_integration.track'
    _description = 'Tracking'
    ##DEV-01-DB-01-01 		 Statut 
    status = fields.Char(string='Status')
    ## DEV-01-DB-01-02 		 Origin Document ID 
    originDocId = fields.Char(string='Origin Document ID')
    ## DEV-01-DB-01-03 		 Origin Document type 
    originDocType = fields.Char(string='Origin Document Type')
    ## DEV-01-DB-01-04 		 Direction 
    direction = fields.Selection([('IN', 'Inbound'), ('OU', 'Outbound')], string='Direction')
    ## DEV-01-DB-01-05 		 Operation 
    operation = fields.Char(string='Operation')
    ## DEV-01-DB-01-06 		 Target URL
    targetUrl = fields.Char(string='Target URL')
    ## DEV-01-DB-01-07 		 Date
    date = fields.Datetime(string='Sent on')
    ## DEV-01-DB-01-08 		 Code de retour 
    returnCode = fields.Char(string='Return Code')
    ## DEV-01-DB-01-09 		 Message de retour 
    returnReason = fields.Text(string='Return Reason')
    ## DEV-01-DB-01-10 		 Response text
    returnText = fields.Char(string='Response')
    ## DEV-01-DB-01-13 		 Request Headers 
    requestHeader = fields.Text(string='Request Headers')
    ## DEV-01-DB-01-14 		 Request body 
    requestBody = fields.Text(string='Request Body')
    ## DEV-01-DB-01-12 		 Tracking Log ID
    log = fields.One2many('cockpit_integration.log', 'track', string = 'Log')
    resendDate = fields.Datetime(string='Last resend on')
    
    ##---------------------------------Methods---------------------------------

    def resend(self):
        for record in self:
            ## Retreieve communication arrangement
            arrangement = self.env['cockpit_integration.com_arrangement'].search([('operation', '=', self.operation)])            
            ##DEV-01-AC-01-03		Les infos du resend se basent au maximum sur l'accord de communication
            url = arrangement.endpoint
            user = arrangement.user
            pwd = arrangement.password
            requHeaders = {}
            for header in arrangement.headers:
                requHeaders[header.key] = header.value
            json_data = self.requestBody
            ## API call
            response = requests.post(url, data=json.dumps(json_data), auth=HTTPBasicAuth(user, pwd), headers=requHeaders)
            record.resendDate = fields.datetime.now()
            ##DEV-01-AC-01 	3	 Création du tracking 
            if (response.ok):
                status = 'Success'
            else:
                status = 'Error'            
            self.env['cockpit_integration.track'].create(
            {
                'status' : status,
                'originDocId' : self.originDocId + '_RESEND',
                'originDocType' : self.originDocType,
                'direction' : self.direction,
                'operation' : self.operation,
                'targetUrl' : url,
                'date' : fields.datetime.now(),
                'returnCode' : response.status_code,
                'returnReason' : response.reason,
                'returnText' : response.text,
                'requestHeader' : requHeaders,
                'requestBody' : json_data
            }
            )
  

    
class log(models.Model):
    ##---------------------------------Fields---------------------------------
    _name = 'cockpit_integration.log'
    _description = 'Log'
    ## DEV-01-DB-02-01 		 Tracking ID 
    track = fields.Many2one('cockpit_integration.track', string = 'Track') ##,default=lambda self:self.env['cockpit_integration.track'].search([], limit=1))
    ## DEV-01-DB-02-02 		 Log message 
    logMsg = fields.Text(string='Log Message')
    
