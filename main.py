import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# get hold of our data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
rem_states = []
score = 0

while len(guessed_states) < 50:

  answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

  if answer_state == "Exit":
    rem_states = [x for x in all_states if x not in guessed_states]
    new_data = pandas.DataFrame(rem_states)
    new_data.to_csv("learn.csv",index="False")
    break

  for i in range(len(data)):
    if data.loc[i,"state"] == answer_state:
      t=turtle.Turtle()
      t.hideturtle()
      t.penup()
      # state = data.loc[i,'state']
      x = data.loc[i,"x"]
      y = data.loc[i,'y']
      print(x,y)
      t.goto(x,y)
      t.write(answer_state)
      score += 1
      guessed_states.append(answer_state)
    
    
  
  


