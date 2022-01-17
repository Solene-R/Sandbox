from odoo import models, fields, api


class com_arrangement(models.Model):
     _name = 'cockpit_integration.com_arrangement'
     _description = 'Communication arrangement'
    
    ##DEV-01-DB-03-01 		 ID 
    id = fields.Integer()
    ##DEV-01-DB-03-02 		 Opération 
    operation = fields.Char()
    ##DEV-01-DB-03-03 		 Status 
    status = fields.Selection([('A', 'Active'), ('I', 'Inactiv')], string='Statuses')
    ## DEV-01-DB-03-04 		 Endpoint (URL) 
    endpoint = fields.Char()
    ## DEV-01-DB-03-05 		 Format 
    formats = fields.Selection([('JS', 'JSON'), ('XM', 'XML')], ('SO', 'SOAP')], string='Formats')
    ## DEV-01-DB-03-06 		 Modèle d'identification 
    formats = fields.Selection([('USR', 'User/password'), ('OTH', 'Others')], string='Identifications')
    ## DEV-01-DB-03-07 		 User 
    user = fields.Char()
    ## DEV-01-DB-03-08 		 Password 
    password = fields.Char()
    ## DEV-01-DB-03-09 		 Contact d'échec (Nom Prénom) 
    failContact = fields.Char()
    ## DEV-01-DB-03-10 		 Contact d'échec (Email) 
    failEmail = fields.Char()
    