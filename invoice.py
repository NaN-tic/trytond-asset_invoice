# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['InvoiceLine', 'Sale', 'SaleLine']


class InvoiceLine:
    __name__ = 'account.invoice.line'
    __metaclass__ = PoolMeta
    invoice_asset = fields.Many2One('asset', 'Asset',
        states={
            'invisible': Eval('type') != 'line',
            },
        depends=['type', 'party'])

    def _credit(self):
        result = super(InvoiceLine, self)._credit()
        if self.invoice_asset:
            result['invoice_asset'] = self.invoice_asset.id
        return result


class Sale:
    __name__ = 'sale.sale'
    __metaclass__ = PoolMeta
    asset = fields.Many2One('asset', 'Asset',
        domain=[
            ('owner', '=', Eval('party')),
            ],
        states={
            'readonly': Eval('state') != 'draft',
            },
        depends=['state', 'party'])


class SaleLine:
    __name__ = 'sale.line'
    __metaclass__ = PoolMeta
    asset_used = fields.Function(fields.Many2One('asset', 'Asset'),
        'on_change_with_asset_used')

    @fields.depends('sale')
    def on_change_with_asset_used(self, name=None):
        if self.sale and self.sale.asset:
            return self.sale.asset.id
        return None

    def get_invoice_line(self, invoice_type):
        lines = super(SaleLine, self).get_invoice_line(invoice_type)
        if self.asset_used:
            for line in lines:
                line.invoice_asset = self.asset_used
        return lines
