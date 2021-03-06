# Pycss - Make your python output standout
Pycss is a module that will help you to color your output!

## How does it work?
Pycss uses ansi color codes. [Read the ansi codes](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html).

**Note**: In PyCharm, you will get weird outputs as it doesn't quite yet support ansi color codes!

## Installation
```commandline
pip install pycss
```
And import it as
```python
# Not pycss
import css
```

## Documentation
### Inbuilt colors
Before the documentation starts, you should be familiar with css' colors  
#### Color
You can access them by referring the module and saying the variable. The color name is always in capital letters: 
`css.COLORNAME`

| Variable  | Color          |
|-----------|----------------|
| BLACK     | Black          |
| RED       | Red            |
| GREEN     | Green          |
| YELLOW    | Yellow         |
| BLUE      | Blue           |
| MAGENTA   | Magenta        |
| CYAN      | Cyan           |
| WHITE     | White          |
| NOCOLOR   | Transparent    |
| C_BLACK   | Bright Black   |
| C_RED     | Bright Red     |
| C_YELLOW  | Bright Yellow  |
| C_GREEN   | Bright Green   |
| C_BLUE    | Bright Blue    |
| C_MAGENTA | Bright Magenta |
| C_CYAN    | Bright Cyan    |
| C_WHITE   | Bright White   |

#### Background colors
You can access them by referring the module and saying the variable. The background color name is always in capital letters: 
`css.BACKROUND_COLOR`

| Variable    | Color          |
|-------------|----------------|
| BGBLACK     | Black          |
| BGRED       | Red            |
| BGGREEN     | Green          |
| BGYELLOW    | Yellow         |
| BGBLUE      | Blue           |
| BGMAGENTA   | Magenta        |
| BGCYAN      | Cyan           |
| BGWHITE     | White          |
| C_BGBLACK   | Bright Black   |
| C_BGRED     | Bright Red     |
| C_BGYELLOW  | Bright Yellow  |
| C_BGGREEN   | Bright Green   |
| C_BGBLUE    | Bright Blue    |
| C_BGMAGENTA | Bright Magenta |
| C_BGCYAN    | Bright Cyan    |
| C_BGWHITE   | Bright White   |

### Coloring the text
To color text, you use the `color()` function.  
> Parameters
> 1. text - The text you want to be colored
> 2. color - Pass in the color you want  
**Note:** You don't use normal strings as color eg: "red". USE pycss's colors!

It returns the colored text

```python
print(css.color("Hello World", css.RED))
```

### Applying background
To apply the background, you use the `bgcolor()` function

> Parameters
> 1. text - The text you want to be colored
> 2. background_color - Pass in the background color you want   
**Note:** You don't use normal strings for background colors eg: "red".USE pycss's background color!

It returns the background colored text

```python
print(css.bgcolor("Hello World", css.BGRED))
```

### Making text bold
To apply the bold, you use the `bold()` function

> Parameters
> 1. text - The text you want to be bold

It returns the bolded text

```python
print(css.bold("Hello World"))
```

### Underlining text
To underline text, you use the `underline()` function

> Parameters
> 1. text - The text you want to be underlined
It returns the underlined text

```python
print(css.underline("Hello World"))
```