# -*- coding: utf-8 -*-
# from odoo import http


# class SparkTutorialMs(http.Controller):
#     @http.route('/spark_tutorial_ms/spark_tutorial_ms', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spark_tutorial_ms/spark_tutorial_ms/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('spark_tutorial_ms.listing', {
#             'root': '/spark_tutorial_ms/spark_tutorial_ms',
#             'objects': http.request.env['spark_tutorial_ms.spark_tutorial_ms'].search([]),
#         })

#     @http.route('/spark_tutorial_ms/spark_tutorial_ms/objects/<model("spark_tutorial_ms.spark_tutorial_ms"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spark_tutorial_ms.object', {
#             'object': obj
#         })
