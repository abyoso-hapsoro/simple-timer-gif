import argparse
from typing import Union


def _parse_size(size: str) -> tuple[int, int]:
    """
    Helper function to parse size.

    Args:
        size (str):
            Array of image size in pixels.
    
    Returns:
        tuple[int, int]:
            Image size in width x height in pixels.
    """

    # Attempt to convert size to tuple
    size = eval(size)
    # Validate the size tuple
    assert isinstance(size, tuple) and len(size) == 2 and all(isinstance(c, int) for c in size)
    # Return size as tuple format
    return size


def _parse_color(color: str) -> Union[str, tuple[int, ...]]:
    """
    Helper function to parse color into string or tuple format.

    Args:
        color (str):
            Background color of the timer.

    Returns:
        Union[str, Tuple[int, ...]]:
            The background color formatted as string or tuple with 4 integer elements.
    """

    try:
        # Attempt to convert color to tuple
        bg_color = eval(color)
        # Validate the color tuple
        assert isinstance(bg_color, tuple) and len(bg_color) == 4 and all(isinstance(c, int) for c in bg_color)
        # Return color as tuple format
        return bg_color
    except (SyntaxError, ValueError, AssertionError):
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
    parser.add_argument('-s', '--size', type=str, dest='size', required=False)
    parser.add_argument('-f', '--font_size', type=int, dest='font_size', required=False)
    parser.add_argument('-r', '--dot_radius', type=int, dest='dot_radius', required=False)
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

    # Resolve size
    if args.size is not None:
        kwargs.update({'size': _parse_size(args.size)})

    # Resolve font size
    if args.font_size is not None:
        kwargs.update({'font_size': args.font_size})
    
    # Resolve dot radius
    if args.dot_radius is not None:
        kwargs.update({'dot_radius': args.dot_radius})

    # Resolve color value
    if args.color is not None:
        kwargs.update({'color': _parse_color(args.color)})

    return kwargs
