# -*- coding: utf-8 -*-
# MIT License
# Copyright (c) 2023 ByQuant.com

from byquant.data.get import Bar

def get_bar(symbol, ktype,freq, tawtime,renew,cache):
    result = Bar(symbol, ktype,freq, tawtime,renew,cache)
    return result

