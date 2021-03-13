# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BlogPost(models.Model):
    _inherit = "blog.post"

    image = fields.Binary(
        "Image", attachment=True,)

class EventPost(models.Model):
    _inherit = "event.event"

    image = fields.Binary(
        "Image", attachment=True,)
