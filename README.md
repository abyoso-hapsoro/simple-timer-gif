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
- result_path (-p / --result_path): Specify filepath
- color (-c / --color): Specify background color

Create a timer with duration of 5 seconds with custom background and save to custom filename.
```shell
$ python main.py 5 --result_path "timergreen.gif" --color "#2cb037"
```
![](timergreen.gif)