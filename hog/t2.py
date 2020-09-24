from hog import *
dice = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
a=max_scoring_num_rolls(dice, trials_count=1000)

