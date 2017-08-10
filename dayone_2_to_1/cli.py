import click


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False)
def main(name, as_cowboy):
    """Converts DayOne2 journal.json to DayOne Classic xml"""
    greet = 'Howdy' if as_cowboy else 'Hi there'
    click.echo('{0}, {1}.'.format(greet, name))
