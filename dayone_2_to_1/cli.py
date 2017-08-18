import click
from dateutil import parser
import json
import plistlib
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)


class DayoneConverter():
    """A class for converting DayOne 2 entries to DayOne Classic entries"""

    # TODO: Finish these conversions
    converted_fields = {
        'Creation Date': 'creationDate',
        'Entry Text': 'text',
        'Location': 'location',
        'Starred': 'starred',
        'Time Zone': 'timeZone',
        'UUID': 'uuid',
        'Weather': 'weather',

    }

    new_fields = {
        'Creator': {'Software Agent': 'dayone-2-to-1'},
        'Tags': '#dayone-2-to-1'
    }

    def __init__(self):
        self.entries = dict()
        self.metadata = dict()

    def load_journal(self, filename):
        with file(filename) as f:
            try:
                entries = json.load(f)
            except ValueError:
                sys.stderr.write("ERROR: {0} could not be parsed\n".format(f))
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


@click.command()
@click.argument('journal', default='Journal.json', required=False)
def main(journal):
    """Converts DayOne2 journal.json to DayOne Classic xml"""
    click.echo("working with {}".format(journal))
    j = DayoneConverter()
    j.load_journal(journal)
    # for entry in j:
    #     print(entry)
    # j.dump_journal()
    j.dump_plists()


