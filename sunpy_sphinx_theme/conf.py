import os
import socket
from urllib.parse import urljoin

from sunpy_sphinx_theme import get_html_theme_path

html_theme_path = get_html_theme_path()
html_theme = "sunpy"
html_css_files = [
    "sunpy_style.css",
]
html_static_path = [os.path.join(html_theme_path[0], html_theme, "static")]
html_extra_path = [os.path.join(
    html_theme_path[0], html_theme, "static", "img")]
html_favicon = os.path.join(html_static_path[0], "img", "favicon-32.ico")
png_icon = os.path.join(html_static_path[0], "img", "sunpy_icon_128x128.png")
html_logo = png_icon
svg_icon = os.path.join(html_static_path[0], "img", "sunpy_icon.svg")
templates_path = [os.path.join(html_theme_path[0], html_theme, "templates")]

sunpy_website_url_base = socket.gethostname()
on_rtd = os.environ.get("READTHEDOCS") == "True"


def page_url(page):
    return urljoin(sunpy_website_url_base, page)


html_sidebars = {"**": ["search-field.html",
                        "sidebar-nav-bs.html", "sidebar-ethical-ads.html"]}

html_theme_options = {
    "page_toctree_depths": {"generated/gallery": 2},
    "on_rtd": on_rtd,
    "external_links": [
        (
            "About",
            [
                ("Our Mission", page_url("about.html"), 1),
                (
                    "Acknowledge SunPy",
                    page_url("about.html") + "#acknowledging-or-citing-sunpy",
                    1,
                ),
                (
                    "Code of Conduct",
                    page_url("coc.html"),
                    1,
                ),
            ],
            1,
        ),
        (
            "Documentation",
            [
                ("sunpy", "https://docs.sunpy.org/en/stable/", 1),
                ("ndcube", "https://docs.sunpy.org/projects/ndcube/", 1),
                ("drms", "https://docs.sunpy.org/projects/drms/", 1),
                ("aiapy", "https://aiapy.readthedocs.io/en/stable/", 1),
                ("pfsspy", "https://pfsspy.readthedocs.io/en/stable/", 1),
                ("sunraster", "https://docs.sunpy.org/projects/sunraster/en/stable/", 1),
                ("sunkit-instruments",
                 "https://docs.sunpy.org/projects/sunkit-instruments/en/stable/", 1),
                ("sunkit-image",
                 "https://docs.sunpy.org/projects/sunkit-image/en/stable/", 1),
                ("radiospectra",
                 "https://docs.sunpy.org/projects/radiospectra/en/stable/", 1),
                ("pyflct", "https://pyflct.readthedocs.io/en/stable/", 1),
                ("ablog", "https://ablog.readthedocs.io/", 1),
            ],
            1,
        ),
        ("Blog", page_url("blog.html"), 1),
        ("Support Us", page_url("contribute.html"), 1),
        ("Get Help", page_url("help.html"), 1),
        (
            "SunPy Project",
            [
                ("SunPy Project", page_url("project/"), 1),
                ("Community Roles", page_url("project/roles.html"), 1),
                ("Affiliated Packages", page_url("project/affiliated.html"), 1),
                ("Emeritus role holders", page_url("project/former.html"), 1),
            ],
            1,
        ),
    ],
    # Only really setup to look nice with 3 values.
    "footer_links": [
        ("Github", "https://github.com/sunpy/sunpy", 1),
        ("Twitter", "https://twitter.com/SunPyProject", 1),
        ("Matrix", "https://app.element.io/#/room/#sunpy:openastronomy.org", 1),
    ],
}
