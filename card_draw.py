# Fixed Python program to draw five random cards

import itertools
import random

# Create a deck of cards with ranks and suits
ranks = [str(n) for n in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
deck = list(itertools.product(ranks, suits))

# Shuffle the deck
random.shuffle(deck)

# Draw five cards
print("You got:")
for rank, suit in deck[:5]:
    print(f"{rank} of {suit}")
