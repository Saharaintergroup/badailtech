from odoo import models


class ThemeBadailtech(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_badailtech_post_copy(self, mod):
        # self.disable_view('website_theme_install.customize_modal')
        self.disable_view('website.header_visibility_standard')

