SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS = True

try:
    from .local import *
except ImportError:
    pass
