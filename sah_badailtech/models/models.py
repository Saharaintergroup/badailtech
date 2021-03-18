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

class EventPost(models.Model):
    _inherit = "hr.job"

    job_category = fields.Selection([('full_time', 'Full Time'), ('part_time', 'Part Time')], 'Job Category', default='full_time')
    benefits = fields.Text(string='Benefits')
    responsibilities = fields.Html(string='Responsibilities')
    min_requirements = fields.Html(string='Min Requirements')
    must_have = fields.Html(string='Must Have')
