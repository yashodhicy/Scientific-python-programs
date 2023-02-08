import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **args):

    self.contents = [
      color for color, value in args.items() for i in range(value)
    ]

  def __str__(self):
    return str(self.contents)

  def draw(self, number):
    items =[]
    if (number >= len(self.contents)):
      return self.contents
    else:
      for i in range(0,number):
        item = random.choice(self.contents)
        self.contents.remove(item)
        items.append(item)
      return items


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matched_draws = 0
  for i in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    # print(new_hat)
    balls = new_hat.draw(num_balls_drawn)
    # print(balls)
    # print(expected_balls)
    numOfBalls = {color: balls.count(color) for color in expected_balls.keys()}
    # print(numOfBalls)
    if all(numOfBalls[color] >= expected_balls[color] for color in expected_balls.keys()):
      matched_draws += 1

  probability = matched_draws / num_experiments
  return probability
