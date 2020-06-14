### Multifunctional Rofi launcher

#### Usecases

|Identifier|Function|Example|
|-|-|-|
|w|Websearch with firefox|`function: w !archwiki xrandr`|
|s|Search files in your home folder and open them|`function: s config`|
|x|Launch shell command|`function: x neofetch`|
|e|Login session management|`function: e`|

Flags can be used to launch a specific function: `python spotlight.py -w`

#### Dependencies

https://pypi.org/project/python-rofi/

`xdg-utils`