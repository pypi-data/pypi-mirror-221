import typer

from .core import Quickbar

app = typer.Typer(
    name="quickbar",
    help="This CLI is a way for you to loop over things from the terminal. But pretty ✨",
    no_args_is_help=True
)

@app.command("for", help="Just a plain for loop, echoes the index each loop", no_args_is_help=True)
def loop(
        begin: int = typer.Argument(None, help="Positional version of `start`, optional. Equal to `start`."),
        end: int = typer.Argument(None, help="Positional version of `stop`, optional. Equal to `stop`."),
        start: int = typer.Option(0, '-s', '--start', help='Start index of the loop'),
        stop: int = typer.Option(10, '-e', '--end', help='The final step index, without any `step` arg this is just `stop - start + 1` steps.'),
        jump: int = typer.Option(1, '-j', '--jump', help='Step size, each loop the looping var is incremented by `jump`'),
        step: int = typer.Option(1, '-S', '--step', help='Step size, each loop the looping var is incremented by `step`. Equal to `jump`'),
    ):
    step = max(step, jump)
    begin = begin or start
    end = end or stop
    
    for i in Quickbar.track(range(start, stop, jump)):
        typer.echo(i)

@app.command("eval", help="Loops through the input, assuming space separated or comma separated. Comma is assumed first, and if not then spaces")
def eval(
        listing: str = typer.Option(None, '-s', '--source', help='Object over which to loop. Should be of the form `<item>,<item>,..` or `"<item> <item> .."`'),
        separator: str = typer.Option(',', '-b', '--break', help='A separator to consider before the comma, if needed')
    ):
    if listing is None:
        listing = input()
    if separator in listing:
        listing = listing.split(separator)
    elif ',' in listing:
        listing = listing.split(',')
    else:
        listing = listing.split(' ')
    
    for l in listing:
        typer.echo(l)    
        
if __name__ == '__name__':
    app()