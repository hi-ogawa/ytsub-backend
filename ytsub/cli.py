import click

from .db import connection_generator
from .models import Base
from .utils import wrap_in_sync


@click.group()
def cli():
    pass


@cli.command()
@wrap_in_sync
async def create_tables():
    async for conn in connection_generator():
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    cli()
