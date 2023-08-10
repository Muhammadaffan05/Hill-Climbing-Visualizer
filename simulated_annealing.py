import turtle
import numpy as np

def objective_function(x):
    return -x**2 + 5

def simulated_annealing(initial_position, step_size, max_iter, temperature, cooling_rate):
    current_position = initial_position
    objective_value = objective_function(current_position)
    objective_values = [objective_value]
    
    for i in range(max_iter):
        new_position = current_position + np.random.uniform(-step_size, step_size)
        new_objective_value = objective_function(new_position)
        
       
        delta = new_objective_value - objective_value
        if delta > 0 or np.exp(delta/temperature) > np.random.uniform():
            current_position = new_position
            objective_value = new_objective_value
            objective_values.append(objective_value)
        
        
        temperature *= cooling_rate
    
    return current_position, objective_values


x_min = -10
x_max = 10

initial_position = np.random.uniform(x_min, x_max)
step_size = 0.1
max_iter = 100
temperature = 1
cooling_rate = 0.95

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300, 0)
t.pendown()


t.pencolor('lightgray')
for y in np.linspace(-25, 25, 11):
    t.penup()
    t.goto(-300, y*12)
    t.pendown()
    t.goto(300, y*12)
for x in np.linspace(-300, 300, 11):
    t.penup()
    t.goto(x, -150)
    t.pendown()
    t.goto(x, 150)


t.pencolor('black')
for x in np.linspace(x_min, x_max, 1000):
    y = objective_function(x)
    t.goto(x*30, y*6)


best_position, objective_values = simulated_annealing(initial_position, step_size, max_iter, temperature, cooling_rate)


t.penup()
t.goto(best_position*30, objective_function(best_position)*6)
t.dot(20, 'red')
t.pendown()
for i, objective_value in enumerate(objective_values):
    t.goto((i+1)*3-300, objective_value*6)
    t.dot(6, 'blue')
    
t.penup()
t.goto(best_position*30, objective_function(best_position)*6+50)
t.write(f'Best Solution: ({best_position:.2f}, {objective_function(best_position):.2f})', align='center', font=('Arial', 18, 'normal'))

t.penup()
t.goto(0, 200)
t.write('Simulated Annealing', align='center', font=('Arial', 20, 'bold'))
t.goto(0, -200)
t.write('x', align='center', font=('Arial', 16, 'normal'))
t.goto(350, 0)
t.write('f(x)', align='center', font=('Arial', 16, 'normal'))
t.goto(0, -220)
t.write(f'Starting position: {initial_position:.2f}', align='center', font=('Arial', 14, 'normal'))
t.goto(0, -240)
t.write(f'Step size: {step_size:.2f}, Max iterations: {max_iter}, Temperature: {temperature:.2f}, Cooling rate: {cooling_rate:.2f}', align='center', font=('Arial', 14, 'normal'))

turtle.done()