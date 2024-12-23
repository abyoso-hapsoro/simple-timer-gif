# Simple Timer GIF
A simple project for a simple timer GIF that counts down assisted by visual indicator.

## Getting Started
1. Clone the repo
   ```shell
   git clone https://github.com/abyoso-hapsoro/simple-timer-gif.git
   ```
2. Install requirements (optional)
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
- color (-c / --color): Specify background color

Create a timer with duration of 5 seconds with warning from 2 seconds, custom background color and save to custom filename.
```shell
$ python main.py 5 -w 2 -p "timergreen.gif" -c "#2cb037"
```
![](timergreen.gif)