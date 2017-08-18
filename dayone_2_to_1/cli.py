import click
import json
import sys


class DayoneConverter():
    """A class for converting DayOne 2 entries to DayOne Classic entries"""

    @staticmethod
    def load_journal(filename):
        entries = json.load(filename)
        print(entries)


@click.command()
@click.argument('journal', default='Journal.json', required=False)
def main(journal):
    """Converts DayOne2 journal.json to DayOne Classic xml"""
    click.echo("working with {}".format(journal))
    j = DayoneConverter()
    with file(journal) as f:
        try:
            j.load_journal(f)
        except ValueError:
            sys.stderr.write("ERROR: {0} could not be parsed\n".format(journal))
            raise

