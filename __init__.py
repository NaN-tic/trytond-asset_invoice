# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .invoice import *
from .sale import *


def register():
    Pool.register(
        InvoiceLine,
        Sale,
        SaleLine,
        module='asset_invoice', type_='model')
