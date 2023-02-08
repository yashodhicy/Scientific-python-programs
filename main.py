import arithmetic_problem
import prob_calculator

print(arithmetic_problem.arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)