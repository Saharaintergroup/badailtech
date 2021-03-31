from ast import literal_eval

from odoo import http
from odoo.http import request

class SlidesCourses(http.Controller):
    def _extract_channel_tag_search(self, **post):
        tags = request.env['slide.channel.tag']
        if post.get('tags'):
            try:
                tag_ids = literal_eval(post['tags'])
            except:
                pass
            else:
                # perform a search to filter on existing / valid tags implicitely
                tags = request.env['slide.channel.tag'].search([('id', 'in', tag_ids)])
        return tags
    @http.route('/slides/courses', type='http', auth="public", website=True)
    def slides_courses(self, **post):

        courses = request.env['slide.channel'].search([('channel_type','=','training')])

        tag_groups = request.env['slide.channel.tag.group'].search(
            ['&', ('tag_ids', '!=', False), ('website_published', '=', True)])
        search_tags = self._extract_channel_tag_search(**post)

        return request.render('sah_badailtech.badailtech_courses_template', {
            'courses': courses,
            'tag_groups': tag_groups,
            'search_tags': search_tags,
            })

    @http.route('/slides/training', type='http', auth="public", website=True)
    def slides_training(self, **post):
        training = request.env['slide.channel'].search([('channel_type', '=', 'documentation')])

        tag_groups = request.env['slide.channel.tag.group'].search(
            ['&', ('tag_ids', '!=', False), ('website_published', '=', True)])
        search_tags = self._extract_channel_tag_search(**post)

        return request.render('sah_badailtech.badailtech_training_template', {
            'training': training,
            'tag_groups': tag_groups,
            'search_tags': search_tags,
        })
