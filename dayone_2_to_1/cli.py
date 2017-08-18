import click
import json
import plistlib
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)


class DayoneConverter():
    """A class for converting DayOne 2 entries to DayOne Classic entries"""

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
            entry['tags'].append('#dayone-2-to-1')
            entry['Entry Text'] = entry.pop('text')
            entry['Location'] = entry.pop('location')
            entry['Weather'] = entry.pop('weather')
            entry['Creator'] = {'Software Agent': 'dayone-2-to-1'}
            entry['Creation Date'] = entry.pop('creationDate')
            entry['Starred'] = entry.pop('starred')
            entry['Time Zone'] = entry.pop('timeZone')
            entry['UUID'] = entry.pop('uuid')
            # TODO: Finish these conversions
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


