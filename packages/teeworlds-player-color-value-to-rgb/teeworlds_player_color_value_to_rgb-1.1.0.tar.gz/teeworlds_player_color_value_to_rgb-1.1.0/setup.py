# !/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='teeworlds_player_color_value_to_rgb',
    version='1.1.0',
    author='XCWQW233',
    author_email='3539757707@qq.com',
    url='https://github.com/XCWQW1/teeworlds_player_color_value_to_rgb',
    description=u'吧teeworlds/ddnet中有关颜色的值转换到RGB(Convert the value of the color in teeworlds/ddnet to RGB)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['teeworlds_player_color_value_to_rgb'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'value_to_rgb=teeworlds_player_color_value_to_rgb.__init__:value_to_rgb'
        ]
    }
)
