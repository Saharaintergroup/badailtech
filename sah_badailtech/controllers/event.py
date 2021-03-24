from odoo.addons.portal.controllers.web import Home
from odoo import http
from odoo.http import request


class WebsiteSort(Home):
    @http.route('/')
    def index(self, **kw):
        super(WebsiteSort, self).index()

        event = request.env['event.event']
        latest_events = event.search([], order="create_date desc", limit=4)



        return request.render('sah_badailtech.badailtech_home_page', {
            'latest_events': latest_events,
            })