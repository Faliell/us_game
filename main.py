import turtle
import pandas
from texto import Texto

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv('50_states.csv')
so_states = states['state'].tolist()
certos = []
game_on = True
while len(certos) < 50:
    answer_state = (screen.textinput(title=f'Placar{len(certos)}/50', prompt='Whats another state?')).title()

    if answer_state == 'Exit':
        break

    if answer_state in so_states:
        certo = (states[states.state == answer_state])
        certo_x = int(certo.x)
        certo_y = int(certo.y)
        texto = Texto(answer_state, certo_x, certo_y)
        if answer_state not in certos:
            certos.append(answer_state)

#a = []
#for i in so_states:
#    if i not in certos:
#        a.append(i)


a = [i for i in so_states if i not in certos]
dt = pandas.DataFrame(a)
dt.to_csv('a.csv')


screen.exitonclick()