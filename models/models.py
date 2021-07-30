#!/usr/bin/python3
# @Time    : 2021-07-30
# @Author  : Kevin Kong (kfx2007@163.com)

from werkzeug import urls
from odoo import api, fields, models, _


class website(models.Model):

    _inherit="website"
    
    def _get_http_domain(self):
        """Get the domain of the current website, prefixed by http if no
        scheme is specified.

        Empty string if no domain is specified on the website.
        """
        self.ensure_one()
        if not self.domain:
            return ''
        res = urls.url_parse(self.domain)
        base_url = self.env['ir.config_paramter'].get_param("web.base.ur")
        protocal = base_url.split("://")[0]
        return protocal + self.domain if not res.scheme else self.domain
