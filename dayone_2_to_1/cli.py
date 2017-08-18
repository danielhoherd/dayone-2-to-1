import click
from DayoneConverter import DayoneConverter

@click.command()
@click.argument('journal', default='Journal.json', required=False)
def main(journal):
    """Converts DayOne2 journal.json to DayOne Classic xml files"""

    j = DayoneConverter()
    j.load_journal(journal)
    j.dump_plists()


