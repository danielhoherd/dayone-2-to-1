# -*- coding: utf-8 -*-
import click
import os
from dayone_2_to_1 import DayoneConverter


def validate_filename(ctx, opts, args):
    try:
        assert os.path.isfile(args)
        return args
    except AssertionError:
        raise click.BadParameter('File "{}" does not exist! '
                                 'Must be a valid Journal.json from DayOne 2 export.'.format(args))


@click.command()
@click.argument('journal', default='Journal.json', required=False,
                callback=validate_filename, nargs=1)
def main(journal):
    """Converts DayOne2 Journal.json to DayOne Classic xml files"""

    j = DayoneConverter()
    j.load_journal(journal)
    j.dump_plists()
