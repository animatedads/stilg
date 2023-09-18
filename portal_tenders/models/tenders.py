from odoo import models, fields

class Tender(models.Model):
    _name = 'tender.manager'
    _description = 'Tender Manager'

    name = fields.Char(string='Tender Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('closed', 'Closed'),
    ], string='State', default='draft')
