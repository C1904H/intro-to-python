class Height(object):
  def __init__(self, feet, inches):
    self.feet = feet
    self.inches = inches

  # Define method for greater than operator
  def __gt__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A > height_inches_B

  # Define method for greater than or equal to operator
  def __ge__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A >= height_inches_B

# Define method for not equal to operator
  def __ne__(self, other):
    height_inches_A = self.feet * 12 + self.inches
    height_inches_B = other.feet * 12 + other.inches
    return height_inches_A != height_inches_B