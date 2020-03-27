# Easy to use offline chat archive.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: March 27, 2020
# URL: https://github.com/xolox/python-chat-archive

"""Sphinx documentation configuration for the `chat-archive` project."""

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'humanfriendly.sphinx',
    'property_manager.sphinx',
]

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'chat-archive'
copyright = '2020, Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from chat_archive import __version__  # noqa

# The short X.Y version.
version = '.'.join(__version__.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# http://sphinx-doc.org/ext/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'bysource'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
intersphinx_mapping = dict(
    hangups=('https://hangups.readthedocs.io/en/latest/', None),
    humanfriendly=('https://humanfriendly.readthedocs.io/en/latest/', None),
    property_manager=('https://property-manager.readthedocs.io/en/latest/', None),
    python2=('https://docs.python.org/2/', None),
    python3=('https://docs.python.org/3/', None),
    qpass=('https://qpass.readthedocs.io/en/latest/', None),
    telethon=('https://telethon.readthedocs.io/en/latest/', None),
    update_dotdee=('https://update-dotdee.readthedocs.io/en/latest/', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'
