#!/usr/bin/python3
import click


# For program of any complexity, use config file
times = 0

@click.group()
@click.option('--count', default=1, help='Number of greetings.')
def greet(count: int) -> None:
    global times
    times = count


@click.command()
@click.option('--name', help='The person to greet.')
def by_name(name: str) -> None:
    """
    Simple command that greets person by their NAME
    """
    global times
    for i in range(0, times):
        click.echo('Hello %s!' % name)


@click.command()
@click.option('--location', help='Where the person to greet is.')
def by_location(location: str) -> None:
    """
    Simple command that greets person by their LOCATION
    """
    global times
    for i in range(0, times):
        click.echo('Hello you over there by the %s' % location)


if __name__ == '__main__':
    greet.add_command(by_name)
    greet.add_command(by_location)
    greet()
