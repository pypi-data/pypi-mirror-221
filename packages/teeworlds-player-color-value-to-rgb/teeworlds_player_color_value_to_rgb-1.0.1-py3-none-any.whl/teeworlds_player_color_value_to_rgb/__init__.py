# !/usr/bin/env python
# coding: utf-8
import math
import colorsys
from typing import Tuple


def value_to_rgb(value: int) -> tuple[int, int, int]:
    def hsl_to_rgb(h, s, l):
        # 将h, s, l的值范围映射到0到1之间
        h /= 360.0
        s /= 100.0
        l /= 100.0

        # 调用colorsys模块函数进行转换
        r, g, b = colorsys.hls_to_rgb(h, l, s)

        # 将0到1之间的浮点数转换为0到255之间的整数
        r = int(round(r * 255))
        g = int(round(g * 255))
        b = int(round(b * 255))

        return r, g, b

    H = round(math.floor(value / 65536) * (360 / 256))
    L = round(math.floor(value % 256) * (50 / 256) + 50)
    if L == 0:
        L = 50
    S = round(math.floor((value / 256) % 256) * (100 / 256))

    rgb = hsl_to_rgb(H, S, L)

    return rgb
