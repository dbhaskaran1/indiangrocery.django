# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Create your views here.
class TrackOrderView(TemplateView):
	template_name = 'track_order/track_order.html'
