#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PowerDNS Recursor documentation build configuration file, created by
# sphinx-quickstart on Wed Jun 28 14:56:44 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import glob
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import guzzle_sphinx_theme

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = []
#extensions = ['redjack.sphinx.lua', 'sphinxcontrib.httpdomain', 'sphinxjsondomain']
extensions = ['sphinxcontrib.httpdomain', 'sphinxjsondomain',
              'sphinxcontrib.fulltoc', 'changelog']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'indexTOC'

# General information about the project.
project = 'PowerDNS Authoritative Server'
copyright = '2017, PowerDNS.COM BV'
author = 'PowerDNS.COM BV'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '4.1'
# The full version, including alpha/beta/rc tags.
#release = '4.1.0-alpha0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    '.venv',
                    'security-advisories/security-policy.rst',
                    'common/secpoll.rst',
                    'common/api/zone.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Changelog Options ----------------------------------------------------

changelog_render_ticket = "https://github.com/PowerDNS/pdns/issues/%s"
changelog_render_pullreq = "https://github.com/PowerDNS/pdns/pull/%s"
changelog_render_changeset = "https://github.com/PowerDNS/pdns/commit/%s"

changelog_sections = ['New Features', 'Removed Features', 'Improvements', 'Bug Fixes']
changelog_inner_tag_sort = ['Internals', 'API', 'Tools', 'ALIAS', 'DNSUpdate', 'BIND', 'MySQL', 'Postgresql', 'Oracle', 'LDAP', 'GeoIP', 'Remote']

changelog_render_tags = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

extensions.append("guzzle_sphinx_theme")

html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "PowerDNS Authoritative Server",
}
html_favicon = 'common/favicon.ico'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = 'pdns.css'


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PowerDNSAuthoritativedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PowerDNS-Authoritative.tex', 'PowerDNS Authoritative Server Documentation',
     'PowerDNS.COM BV', 'manual'),
]

latex_logo = 'common/powerdns-logo-500px.png'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
descriptions = {
    'calidns': 'A DNS recursor testing tool',
    'dnsbulktest': 'A debugging tool for intermittent resolver failures',
    'dnsgram': 'A debugging tool for intermittent resolver failures',
    'dnspcap2protobuf': 'A tool to convert PCAPs of DNS traffic to PowerDNS Protobuf',
    'dnsreplay': 'A PowerDNS nameserver debugging tool',
    'dnsscan': 'List the amount of queries per qtype in a pcap',
    'dnsscope': 'A PowerDNS nameserver debugging tool',
    'dnstcpbench': 'tool to perform TCP benchmarking of nameservers',
    'dnswasher': 'A PowerDNS nameserver debugging tool',
    'dumresp': 'A dumb DNS responder',
    'ixplore': 'A tool that provides insights into IXFRs',
    'nsec3dig': 'Show and validate NSEC3 proofs',
    'pdns_control': 'Control the PowerDNS nameserver',
    'pdns_notify': 'A simple DNS NOTIFY sender',
    'pdns_server': 'The PowerDNS Authoritative Namserver',
    'pdnsutil': 'PowerDNS record and DNSSEC command and control',
    'saxfr': 'Perform AXFRs and show information about it',
    'sdig': 'Perform a DNS query and show the results',
    'zone2json': 'convert BIND zones to JSON',
    'zone2ldap': 'convert zonefiles to ldif',
    'zone2sql': 'convert BIND zones to SQL',
}
man_pages = []
for f in glob.glob('manpages/*.1.rst'):
    srcname = '.'.join(f.split('.')[:-1])
    destname = srcname.split('/')[-1][:-2]
    man_pages.append((srcname, destname, descriptions.get(destname, ''),
                      [author], 1))

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
#texinfo_documents = [
#    (master_doc, 'PowerDNSRecursor', 'PowerDNS Recursor Documentation',
#     author, 'PowerDNSRecursor', 'One line description of project.',
#     'Miscellaneous'),
#]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
