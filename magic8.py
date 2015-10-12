# TODO: convert tabs to spaces - google
# TODO: find out how to trim trailing space
# TODO: always make sure there is a line and EOF

import random


def get_outcomes():
	outcomes = []

	# HW: Thoroughly understand every single line of code below
	# HW(BONUS): assign all outcomes in one line (outcomes = ...)
	with open("outcomes.txt", "r") as outcomes_file:
		for outcome in outcomes_file:
			outcomes.append(outcome)

	return outcomes


# CONSTANTS
OUTCOMES = get_outcomes()
NO_QUESTION = ""

o
# loop indefinitely (capital 'T' always on true)
while True:

	# defining variable 'question' as raw input prompted by
	# string "Ask the magic 8 ball..."
	# and instructions for submit/exit
	question = raw_input(
		"Ask the magic 8 ball a question: " +
		"(type question and press enter or just enter to quit) ")

	if question == NO_QUESTION:
		break

	rand_int = random.randint(0, len(OUTCOMES)-1)
	print OUTCOMES[rand_int]



