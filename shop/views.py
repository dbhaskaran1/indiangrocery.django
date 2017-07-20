# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ShopView(TemplateView):
	template_name = 'shop/shop.html'

