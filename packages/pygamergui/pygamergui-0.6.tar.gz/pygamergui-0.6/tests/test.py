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
                    )
windowm.run()
