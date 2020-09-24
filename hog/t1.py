from hog import *
trials_count=1000
dice = make_test_dice(1,2,2,2,2,2)
roll=make_averaged(roll_dice,trials_count)
for i in range(10,0,-1):
      max_value=roll(i,dice)
      print(max_value)

