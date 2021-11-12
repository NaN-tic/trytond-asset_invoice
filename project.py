# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Work']


class Work(metaclass=PoolMeta):
    __name__ = 'project.work'
    asset = fields.Many2One('asset', 'Asset')
