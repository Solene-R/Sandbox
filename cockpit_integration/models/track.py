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
    ## Response headers
    returnHeaders = fields.Char(string='Response Headers')
    ## DEV-01-DB-01-13 		 Request Headers 
    requestHeader = fields.Text(string='Request Headers')
    ## DEV-01-DB-01-14 		 Request body 
    requestBody = fields.Text(string='Request Body')
    ## DEV-01-DB-01-12 		 Tracking Log ID
    ##log = fields.One2many('cockpit_integration.log', 'track', string = 'Log')
    ## date de rensend
    resendDate = fields.Datetime(string='Last resend on')
    ## token from get call
    token = fields.Text(string='Token from get call')
    
    ##---------------------------------Methods---------------------------------

    def resend(self):
        for record in self:
            ## Retreieve communication arrangement
            arrangement = self.env['cockpit_integration.com_arrangement'].search([('operation', '=', self.operation)])            
            body = self.requestBody
            ## API call
            answer = arrangement._api_launch_post(body, record.originDocId + '_Resent')
            ## update resend date
            record.resendDate = fields.datetime.now()
