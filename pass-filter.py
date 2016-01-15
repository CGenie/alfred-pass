#!/usr/bin/env python

import fnmatch
import os
import sys


QUERY = sys.argv[1]
HOME = os.environ['HOME']
PASS_DIR = os.environ.get('PASSWORD_STORE_DIR', os.path.join(HOME, '.password-store/'))


# TODO: list_passwords creates cache of passwords for first time
def list_passwords():
    ret = []

    for root, dirnames, filenames in os.walk(PASS_DIR):
        for filename in fnmatch.filter(filenames, '*.gpg'):
            ret.append(os.path.join(root, filename).rstrip('.gpg').replace(PASS_DIR, ''))

    return ret


def search_passwords(query):
    ret = []

    terms = filter(lambda x: x, query.lower().split())
    passwords = list_passwords()

    for password in passwords:
        for t in terms:
            if t not in password.lower():
                break
        else:
            ret.append(password)

    return ret


def xmlize_items(items):
    items_a = []

    for item in items:
        items_a.append("""
    <item arg="%(item)s">
        <title>%(item)s</title>
    </item>
        """ % {'item': item})

    return """
<?xml version="1.0"?>
<items>
    %s
</items>
    """ % '\n'.join(items_a)


items = search_passwords(QUERY)
print xmlize_items(items)

