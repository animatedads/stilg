# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class Product(models.Model):
    _name = 'product.product'
    _description = 'Product'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    image = fields.Binary(string='Image')

class ProductPortal(models.Model):
    _inherit = 'product.product'

    portal_user_id = fields.Many2one('res.users', string='Portal User')
