from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    lot_info = fields.Char("Lot/Serial Number info")
    lot_info_usage = fields.Selection(
        [("no", "No"), ("optional", "Optional"), ("required", "Required")],
        related="product_id.product_tmpl_id.lot_info_usage",
    )
