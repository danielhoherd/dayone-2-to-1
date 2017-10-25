# -*- coding: utf-8 -*-
from dateutil import parser
import json
import plistlib
import sys


class DayOneConverter:
    """A class for converting DayOne 2 entries to DayOne Classic entries"""

    # TODO: Finish these conversions
    # or... make a function to convert each field, then call each function individually
    converted_fields = {
        'Creation Date': 'creationDate',
        'UUID': 'uuid',
        'Entry Text': 'text',
        'Location': 'location',
        'Starred': 'starred',
        'Time Zone': 'timeZone',
        'Weather': 'weather',
    }

    new_fields = {
        'Creator': {'Software Agent': 'dayone-2-to-1'},
        'Tags': 'dayone-2-to-1'
    }

    def __init__(self):
        self.entries = dict()
        self.metadata = dict()

    def load_journal(self, filename):
        with file(filename) as f:
            try:
                entries = json.load(f)
            except ValueError:
                sys.stderr.write("ERROR: {} could not be parsed\n".format(f))
                raise
        self.entries = entries['entries']
        self.metadata = entries['metadata']

    def dump_journal(self):
        print(self.entries)

    def dump_plists(self):
        for entry in self.entries:
            entry.setdefault('tags', list())
            for k, v in self.new_fields.items():
                entry.setdefault(k, list())
                entry[k].append(v)
            for k, v in self.converted_fields.items():
                entry[k] = entry.pop(v)
            entry['Creation Date'] = parser.parse(entry['Creation Date'])

            plistlib.writePlist(entry, '{}.doentry'.format(entry['UUID']))

    def __iter__(self):
        for entry in self.entries:
            yield entry
