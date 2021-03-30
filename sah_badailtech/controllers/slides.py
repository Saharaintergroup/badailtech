from odoo import http
from odoo.http import request


class SlidesCourses(http.Controller):
    @http.route('/slides/courses', type='http', auth="public", website=True)
    def slides_courses(self, **post):

        courses = request.env['slide.channel'].search([('slide_type','=','training')])


        return request.render('module_name.template_name', {
            'courses': courses,
            })

    @http.route('/slides/training', type='http', auth="public", website=True)
    def slides_training(self, **post):
        training = request.env['slide.channel'].search([('channel_type', '=', 'documentation')])

        return request.render('module_name.template_name', {
            'training': training,
        })
