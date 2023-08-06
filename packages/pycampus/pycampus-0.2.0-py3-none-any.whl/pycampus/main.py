import click
from pycampus.__about__ import VERSION

@click.group()
@click.version_option(VERSION)
def pycampus():
    pass
