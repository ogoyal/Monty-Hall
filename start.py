
from controllers import monty
from controllers.monty import change_choice, same_choice, display_prob
from helpers.settings import set_trial_number, set_sections

set_trial_number(10000)
set_sections(150)

monty.__init__()

change_prob = change_choice()
same_prob = same_choice()

display_prob(change_prob, same_prob)


