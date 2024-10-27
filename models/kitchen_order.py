from odoo import models, fields, api

class KitchenOrder(models.Model):
    _name = 'kitchen.order'
    _description = 'Kitchen Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default='New')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    state = fields.Selection([
        ('to_cook', 'To Cook'),
        ('ready', 'Ready'),
        ('completed', 'Completed')
    ], string='Status', default='to_cook')
    order_line_ids = fields.One2many('kitchen.order.line', 'kitchen_order_id', string='Order Lines')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('kitchen.order') or 'New'
        return super(KitchenOrder, self).create(vals)

class KitchenOrderLine(models.Model):
    _name = 'kitchen.order.line'
    _description = 'Kitchen Order Line'

    kitchen_order_id = fields.Many2one('kitchen.order', string='Kitchen Order', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
