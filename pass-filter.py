#!/usr/bin/env python3

import fnmatch
import os
import sys
import re
# import string


QUERY = sys.argv[1]
HOME = os.environ['HOME']
PASS_DIR = os.environ.get('PASSWORD_STORE_DIR', os.path.join(HOME, '.password-store/'))


# TODO: list_passwords creates cache of passwords for first time
def list_passwords():
    ret = []

    for root, _, filenames in os.walk(PASS_DIR):
        for filename in fnmatch.filter(filenames, '*.gpg'):
            ret.append(os.path.join(root, filename.replace('.gpg','')).replace(PASS_DIR, ''))
    return sorted(ret, key=lambda s: s.lower())


def search_passwords(query):
    ret = []

    passwords = list_passwords()
    regex = ".*{}.*".format(query)

    for password in passwords:
        if re.match(regex, password):
            ret.append(password)
    return ret


def xmlize_items(items, query):
    items_a = []

    for item in items:
        list = item.split("/", 1)
        name = list[-1]
        path = item if len(list) == 2 else ""

        complete = item
        if item.lower().startswith(query.lower()):
            i = item.find("/", len(query))
            if i != -1:
                complete = item[:(i+1)]

        items_a.append("""
    <item uid="%(item)s" arg="%(item)s" autocomplete="%(complete)s">
        <title>%(name)s</title>
        <subtitle>%(path)s</subtitle>
    </item>
        """ % {'item': item, 'name': name, 'path': path, 'complete': complete})

    return """
<?xml version="1.0"?>
<items>
    %s
</items>
    """ % '\n'.join(items_a)


items = search_passwords(QUERY)
print (xmlize_items(items, QUERY))
