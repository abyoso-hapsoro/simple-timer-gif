import math
from PIL import Image, ImageDraw, ImageFont
from typing import Union, Tuple
from validate import validate_input
from parse import parse_input


def create_timer_gif(
    duration: int,
    warning: int = -1,
    result_path: str = None,
    color: Union[str, Tuple[int, ...]] = (255, 255, 255, 0)
) -> None:
    """
    Create a timer GIF that counts down to zero with elapsing dot indicators.

    Args:
        duration (int):
            Duration of timer in seconds.
        warning (int, optional):
            Low timer warning in seconds. Defaults to -1 — i.e. no warning.
        result_path (str, optional):
            Path to save the timer. Defaults to None.
        color (Union[str, Tuple[int, ...]], optional):
            Background color of the timer. Defaults to (255, 255, 255, 0) — i.e. transparent.
    
    Raises:
        AssertionError: If arguments do not match requirement.
    
    Examples:
        Create a timer with duration of 5 seconds.
            $ python main.py 5
            $ python main.py --duration 5
            $ python main.py -d 5
        Create a timer with duration of 60 seconds with white background.
            $ python main.py 60 --color "white"
            $ python main.py --duration 60 --color "white"
            $ python main.py 60 -c "white"
            $ python main.py -d 60 -c "white"
        Create a timer with duration of 15 seconds and save to custom filename.
            $ python main.py 15 --result_path "timer.gif"
            $ python main.py --duration 15 --result_path "timer.gif"
            $ python main.py 15 -p "timer.gif"
            $ python main.py -d 15 -p "timer.gif"
        Create a timer with duration of 10 seconds with custom background and save to custom filename.
            $ python main.py 10 --result_path "timergreen.gif" --color "#2cb037"
            $ python main.py --duration 10 --result_path "timergreen.gif" --color "#2cb037"
            $ python main.py 10 -p "timergreen.gif" -c "#2cb037"
            $ python main.py -d 10 -p "timergreen.gif" -c "#2cb037"
        Create a timer with duration of 30 seconds with warning starting from 10 seconds.
            $ python main.py 30 --warning 10
            $ python main.py --duration 30 --warning 10
            $ python main.py 30 -w 10
            $ python main.py -d 30 -w 10
    """

    # Validate inputs
    args = [eval(arg) for arg in create_timer_gif.__code__.co_varnames[:create_timer_gif.__code__.co_argcount]]
    validate_input(*args)

    # Consolidate result path
    if result_path is None:
        result_path = f'timer{duration}.gif'

    # Set option values
    size = (500, 500)
    font_size = 120
    dot_radius = 8

    # Determine center and radius
    x0, y0 = [coord // 2 for coord in size]
    radius = min(size) // 2.5

    # Initialize list to store image frames
    frames = []

    # Iterate from duration to 0
    for t in range(duration, -1, -1):
        # Create new blank image
        image = Image.new('RGBA', size, color)
        draw = ImageDraw.Draw(image)

        # Draw circular dots around the center
        for idx in range(t):
            # Set angle in radians
            angle = (math.pi / 2) + (2 * math.pi * idx) / duration

            # Get current x and y positions
            x = x0 + int(radius * math.cos(angle))
            y = y0 - int(radius * math.sin(angle))

            # Draw the dots
            draw.ellipse(
                (x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius),
                fill='black' if idx >= warning else 'red'
            )
        
        # Load font
        font = ImageFont.load_default(size=font_size)

        # Calculate center position
        text = str(t)
        # position = (250 - len(text)*35, 174)
        left, top, right, bottom = font.getbbox(text)
        width = right - left
        height = bottom - top
        position = (
            (size[0] - width) // 2 - left,
            (size[1] - height) // 2 - top
        )
        
        # Draw the central number
        draw.text(
            position,
            text,
            fill='black' if t > warning else 'red',
            font=font
        )

        # Save the frame
        frames.append(image)
    
    # Save frames as GIF
    frames[0].save(
        result_path,
        save_all=True,
        append_images=frames[1:],
        duration=1000,  # 1 second per frame
        disposal=2,
        loop=0
    )


if __name__ == '__main__':
    # Create the timer GIF
    create_timer_gif(**parse_input())
