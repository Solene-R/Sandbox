from odoo import models, fields, api


class track(models.Model):
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
    ##returnMsg = fields.Text(string='Return Message')
    ## DEV-01-DB-01-10 		 Document ID 
    ##returnDocId = fields.Char(string='Returned Document ID')
    ## DEV-01-DB-01-11 		 Request ID 
    ##requestId = fields.Char(string='Request ID')
    ## DEV-01-DB-01-13 		 Request Headers 
    requestHeader = fields.Text(string='Request Headers')
    ## DEV-01-DB-01-14 		 Request body 
    requestBody = fields.Text(string='Request Body')
    ## DEV-01-DB-01-12 		 Tracking Log ID
    log = fields.One2many('cockpit_integration.log', 'track', string = 'Log')

    
class log(models.Model):
    _name = 'cockpit_integration.log'
    _description = 'Log'
    ## DEV-01-DB-02-01 		 Tracking ID 
    track = fields.Many2one('cockpit_integration.track', string = 'Track') ##,default=lambda self:self.env['cockpit_integration.track'].search([], limit=1))
    ## DEV-01-DB-02-02 		 Log message 
    logMsg = fields.Text(string='Log Message')
    
