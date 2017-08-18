import click
from DayoneConverter import DayoneConverter

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


