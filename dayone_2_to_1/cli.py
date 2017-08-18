import click
import json
import plistlib
import sys


class DayoneConverter():
    """A class for converting DayOne 2 entries to DayOne Classic entries"""

    @staticmethod
    def load_journal(filename):
        with file(filename) as f:
            try:
                entries = json.load(f)
            except ValueError:
                sys.stderr.write("ERROR: {0} could not be parsed\n".format(f))
                raise
        print(entries)


@click.command()
@click.argument('journal', default='Journal.json', required=False)
def main(journal):
    """Converts DayOne2 journal.json to DayOne Classic xml"""
    click.echo("working with {}".format(journal))
    j = DayoneConverter()
    j.load_journal(journal)

