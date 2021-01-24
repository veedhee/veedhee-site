DIPOR_PREFIX = '/home/vidhi/dipordocs/src'
DIPOR_SOURCE_ROOT = 'main-blog/src'
DIPOR_CONTENT_ROOT = 'main-blog/content'
DIPOR_INITIAL_APP = 'main-blog'
DIPOR_EXTENSIONS = ['meta']
DIPOR_FILE_FORMATS_ALLOWED = ['md', 'json']
DIPOR_PORT = 5050
DIPOR_PRETTIFY = True

DIPOR_LIST_ITEMS = [
    # <path-relative-to-content>
    # must have a _branches
    # should have a list.json for data you want available in listing items
    ('blog', '-chrono')
]


instance = globals()