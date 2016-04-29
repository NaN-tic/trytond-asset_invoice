# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta, Pool
from trytond.pyson import Eval

__all__ = ['InvoiceLine']


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

    __metaclass__ = PoolMeta
    __metaclass__ = PoolMeta
    def get_invoice_line(self):
        lines = super(SaleLine, self).get_invoice_line()