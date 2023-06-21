# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProfessionPartner(models.Model):
    _name = 'res.partner.profession'

    name = fields.Char()


class PartnerProfessionExtended(models.Model):
    _inherit = 'res.partner'

    profession_id = fields.Many2one('res.partner.profession', string='Profesión')
    