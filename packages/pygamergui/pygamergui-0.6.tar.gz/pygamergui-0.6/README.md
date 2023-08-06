
# pygamergui-0.6

A simple gui library made using python and pygame module as core.


## Authors

- [@Bishnu-coder](https://github.com/Bishnu-coder)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://bishnu-coder.github.io/)
[![Facebook](https://img.shields.io/badge/facebook-0A66C2?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/bishnukohar01/)
[![twitter](https://img.shields.io/badge/youtube-1DA1F2?style=for-the-badge&logo=youtube&logoColor=red)](https://www.youtube.com/channel/UCNj9jZBVxRWm7TA5g2K7XtA)


## How to install ?

Install module

```bash
  pip install pygame,pygamergui
```


## Demo Video
![video](https://github.com/Bishnu-coder/pygamergui-0.6/blob/main/tests/Untitled%20video%20-%20Made%20with%20Clipchamp.gif)

## Demo image
![image](https://github.com/Bishnu-coder/pygamergui-0.6/blob/main/tests/Screenshot_2023-06-28_16_13_11.png)

## Demo code 
```python
from pygamergui import buttons,slider,text,window


def b1test(args):
    t1.text = "use->"
    print(args)


def b2test(args):
    t1.text = "Pygamergui"
    print(args)

anemi = text.Word_Animation("pygamergui",color='red')

b1 = buttons.simple_button(target=b1test,
                         text='use',
                         fg='white',
                         w=75,
                         h=50,
                         color=(0, 175, 250),
                         args=[1]
                         )

b2 = buttons.simple_button(target=b2test,
                         fg='white',
                         text="PGG",
                         w=100,
                         h=50,
                         color=(0, 175, 250)
                         )

t1 = text.text("what to use??")

r1 = buttons.button_radio(radius=30, color='cyan')

s1 = slider.slider(300,
                  550,
                  h=10,
                  corner_round=10,
                  color='purple',
                  t1_align='side',
                  text_size=20,
                  text_color='black',
                  color_circle=(0, 175, 250)
                  )


def update():
    b1.show_no_anemi(200, 400, window=windowm, corner_round_level=10)
    b2.show_color_change(300, 400, window=windowm, corner_round_level=10)

    t1.show(windowm, 175, 175)

    a=r1.show(windowm, 300, 300)
    if a:
        anemi.show(windowm,180,100,4)
    a = s1.show(windowm)
    

windowm = window.app(title='test',
                    bgcolor=(40, 40, 40), 
                    target=update, update_rate=10, 
                    background="python1.png"
                    )
windowm.run()

```

## Project structure
![structure](https://raw.githubusercontent.com/Bishnu-coder/pygamergui-0.6/a575318116fe23d22ecee5f0982ab9e590e777ba/tests/diagram-export-7_25_2023%2C%2010_56_49%20AM.svg)
## Appendix

Important points:

1. all widgets (i.e button,text,slider,Button_radio)can be used importing text,buttons,slider from pygamergui.

2. background image path should be provided to window class as in example

3. window class makes the main window appear

4. All the show methods should be put in an function which is passed as target to window class

## Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
