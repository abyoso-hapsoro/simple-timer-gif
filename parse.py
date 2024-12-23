import argparse
from typing import Union, Tuple


def _parse_color(color: str) -> Union[str, Tuple[int, ...]]:
    """
    Helper function to parse color into string or tuple format.

    Args:
        color (str):
            Background color of the timer. Defaults to (255, 255, 255, 0) — i.e. transparent.

    Returns:
        Union[str, Tuple[int, ...]]:
            The color formatted as string or tuple with 4 integer elements.
    """

    try:
        # Attempt to convert color to tuple
        color = eval(color)

        # Validate the color tuple
        if isinstance(color, tuple) and len(color) == 4 and all(isinstance(c, int) for c in color):
            # Return color as tuple format
            return color
    except:
        # Return color as string format
        return color


def parse_input() -> dict:
    """
    Parse input arguments from command line.

    Returns:
        dict:
            Dictionary containing keyword arguments for main program.
    """

    # Instantiate argument parser
    parser = argparse.ArgumentParser()

    # Add positional argument
    parser.add_argument('duration', type=int, nargs='?')

    # Add flag arguments
    parser.add_argument('-d', '--duration', type=int, dest='flag_duration', required=False)
    parser.add_argument('-w', '--warning', type=int, dest='warning', required=False)
    parser.add_argument('-p', '--result_path', type=str, dest='result_path', required=False)
    parser.add_argument('-c', '--color', type=str, dest='color', required=False)

    # Parse the arguments
    args = parser.parse_args()

    # Resolve duration value
    kwargs = {'duration': args.flag_duration if args.flag_duration is not None else args.duration}

    # Resolve warning
    if args.warning is not None:
        kwargs.update({'warning': args.warning})

    # Resolve result path
    if args.result_path is not None:
        kwargs.update({'result_path': args.result_path})
    
    # Resolve color value
    if args.color is not None:
        kwargs.update({'color': _parse_color(args.color)})

    return kwargs
