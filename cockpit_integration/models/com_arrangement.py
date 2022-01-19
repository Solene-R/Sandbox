from odoo import models, fields, api


class com_arrangement(models.Model):
    _name = 'cockpit_integration.com_arrangement'
    _description = 'Communication arrangement'
    ##DEV-01-DB-03-01 		 ID 
    ##id = fields.Integer(string='ID')
    ##DEV-01-DB-03-02 		 Opération 
    operation = fields.Char()
    ##DEV-01-DB-03-03 		 Status 
    status = fields.Selection([('A', 'Active'), ('I', 'Inactive')], string='Status')
    ## DEV-01-DB-03-04 		 Endpoint (URL) 
    endpoint = fields.Char(string='Endpoint (URL)')
    ## DEV-01-DB-03-05 		 Format 
    formats = fields.Selection([('JS', 'JSON'), ('XM', 'XML'), ('SO', 'SOAP')], string='Format')
    ## DEV-01-DB-03-06 		 Modèle d'identification 
    formats = fields.Selection([('USR', 'User/password')], string='Identification')
    ## DEV-01-DB-03-07 		 User 
    user = fields.Char(string='User')
    ## DEV-01-DB-03-08 		 Password 
    password = fields.Char(string='Password')
    ## DEV-01-DB-03-09 		 Contact d'échec (Nom Prénom) 
    failContact = fields.Char(string='Fail contact Name')
    ## DEV-01-DB-03-10 		 Contact d'échec (Email) 
    failEmail = fields.Char(string='Fail contact Email')
    
    ## DEV-01-AC-03-01 		L'opération doit être unique
    _sql_constraints = [
        ('uniq_operation', 'unique(operation)', "A communication arrangement already exists with this operation. Operation must be unique!"),
    ]