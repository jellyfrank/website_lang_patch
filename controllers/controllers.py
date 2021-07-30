# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteLangPatch(http.Controller):
#     @http.route('/website_lang_patch/website_lang_patch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_lang_patch/website_lang_patch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_lang_patch.listing', {
#             'root': '/website_lang_patch/website_lang_patch',
#             'objects': http.request.env['website_lang_patch.website_lang_patch'].search([]),
#         })

#     @http.route('/website_lang_patch/website_lang_patch/objects/<model("website_lang_patch.website_lang_patch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_lang_patch.object', {
#             'object': obj
#         })
