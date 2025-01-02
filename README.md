# Simple Timer GIF
A simple project for a simple timer GIF that counts down assisted by visual indicator.

## Getting Started
1. Ensure installed Python is version 3.9 or higher
   ```shell
   python --version
   ```
2. Clone the repo
   ```shell
   git clone https://github.com/abyoso-hapsoro/simple-timer-gif.git
   ```
3. Install requirements (optional)
   ```shell
   pip install -U -r requirements.txt
   ```

## Example Usage
### Basic
Create a timer with duration of 10 seconds.
```shell
$ python main.py 10
```
![](timer10.gif)

### Customization
Customization options:
- warning (-w / --warning): Specify low timer warning
- result_path (-p / --result_path): Specify filepath
- size (-s / --size): Specify image size
- font_size (-f / --font_size): Specify font size
- dot_radius (-r / --dot_radius): Specify dot radius
- color (-c / --color): Specify background color

Create a timer with the following specifications:
1. Duration of 5 seconds
2. Warning from 2 seconds
3. GIF size of 600 x 450
4. Font size of 100
5. Dot radius of 10
6. Custom background color
7. Save to custom filename
```shell
$ python main.py 5 -w 2 -s (600,450) -f 100 -r 10 -c "#2cb037" -p "timergreen.gif"
```
![](timergreen.gif)