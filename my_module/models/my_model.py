from odoo import models, fields


class MyModel(models.Model):
    _name = 'my.module.model'
    _description = 'My Model'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
