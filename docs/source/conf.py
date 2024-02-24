#  pyroblack - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#  Copyright (C) 2024-present eyMarv <https://github.com/eyMarv>
#
#  This file is part of pyroblack.
#
#  pyroblack is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  pyroblack is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with pyroblack.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

from pyrogram import __version__
from pyrogram.raw.all import layer

from pygments.styles.friendly import FriendlyStyle

FriendlyStyle.background_color = "#f3f2f1"

project = "pyroblack"
copyright = f"2023-present, eyMarv"
author = "eyMarv"

version = ".".join(__version__.split(".")[:-1]) + " [" + str(layer) + "]"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_immaterial",
]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

master_doc = "index"
source_suffix = ".rst"
autodoc_member_order = "bysource"

templates_path = ["../resources/templates"]
html_copy_source = False

napoleon_use_rtype = False
napoleon_use_param = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Decides the language used for syntax highlighting of code blocks.
highlight_language = "python3"

copybutton_prompt_text = "$ "

suppress_warnings = ["image.not_readable"]

html_title = f"pyroblack Documentation v{__version__}"
html_theme = "sphinx_immaterial"
html_static_path = [os.path.abspath("static")]
print("ABSOLUTE PATH", os.path.abspath("static"))

html_show_sourcelink = True
html_show_copyright = False
# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the documentation.
html_theme_options = {
    "navigation_with_keys": True,
    "dark_css_variables": {
        "admonition-title-font-size": "0.95rem",
        "admonition-font-size": "0.92rem",
    },
    "light_css_variables": {
        "admonition-title-font-size": "0.95rem",
        "admonition-font-size": "0.92rem",
    },
    "light_logo": "hydrogram-light.png",
    "dark_logo": "hydrogram-dark.png",
}

html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://eyMarv.github.io/pyroblack-docs/",
    "repo_url": "https://github.com/eyMarv/pyroblack/",
    "repo_name": "pyroblack",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        "navigation.tabs",
        "navigation.sections",
        "navigation.top",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [{"media": "(prefers-color-scheme: dark)", "scheme": "slate"}],
    "toc_title_is_page_title": True,
    "version_dropdown": True,
    "version_info": [
        {"version": "main", "title": "main", "aliases": ["latest"]},
        {"version": "staging", "title": "staging", "aliases": []},
    ],
}

html_logo = html_static_path[0] + "/img/pyroblack.png"
html_favicon = html_static_path[0] + "/img/favicon.ico"

latex_engine = "xelatex"
latex_logo = os.path.abspath(html_static_path[0] + "/img/pyroblack.png")

latex_elements = {
    "pointsize": "12pt",
    "fontpkg": r"""
        \setmainfont{Open Sans}
        \setsansfont{Bitter}
        \setmonofont{Ubuntu Mono}
        """,
}

html_css_files = [
    "css/custom.css",
    "css/all.min.css",
]
