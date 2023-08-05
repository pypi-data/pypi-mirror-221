# pylint: disable-msg=W0622
"""cubicweb-person packaging information"""

modname = 'person'
distname = "cubicweb-%s" % modname

numversion = (1, 13, 0)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
description = "person component for the CubicWeb framework"
author = "Logilab"
author_email = "contact@logilab.fr"
web = 'https://www.cubicweb.org/project/%s' % distname
classifiers = [
    'Environment :: Web Environment',
    'Framework :: CubicWeb',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    ]

__depends__ = {'cubicweb': '>= 3.38.0,<3.39'}
__recommends__ = {'cubicweb-addressbook': None}
