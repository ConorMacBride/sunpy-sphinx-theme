"""
SunPy Sphinx Theme.
"""
import os

import pydata_sphinx_theme


def get_html_theme_path():
    """
    Return list of HTML theme paths.
    """
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir] + pydata_sphinx_theme.get_html_theme_path()
