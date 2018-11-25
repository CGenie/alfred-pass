#!/usr/bin/env python

import fnmatch
import os
import sys
import string

from fuzzywuzzy import process

QUERY = sys.argv[1]
HOME = os.environ['HOME']
PASS_DIR = os.environ.get('PASSWORD_STORE_DIR', os.path.join(HOME, '.password-store/'))


# TODO: list_passwords creates cache of passwords for first time
def list_passwords():
    ret = []

    for root, dirnames, filenames in os.walk(PASS_DIR, True, None, True):
        for filename in fnmatch.filter(filenames, '*.gpg'):
            ret.append(os.path.join(root, filename.replace('.gpg','')).replace(PASS_DIR, ''))
    return sorted(ret, key=lambda s: s.lower())


def search_passwords(query):
    ret = []

    passwords = list_passwords()
    return [entry[0] for entry in process.extract(query, passwords)]


def xmlize_items(items, query):
    items_a = []

    for item in items:
        list = string.rsplit(item, "/", 1)
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
print xmlize_items(items, QUERY)

