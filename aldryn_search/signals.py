# -*- coding: utf-8 -*-
"""
Created on Nov 30, 2015

@author: jakob
"""
from django.dispatch.dispatcher import Signal


add_to_index = Signal(['instance', 'object_action'])
remove_from_index = Signal(['instance', 'object_action'])
