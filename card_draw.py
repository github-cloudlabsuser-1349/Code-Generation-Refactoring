# Fixed Python program to draw a specified number of random cards

import itertools
import random

def get_num_cards():
    while True:
        try:
            num = int(input("How many cards would you like to draw? (1-52): "))
            if 1 <= num <= 52:
                return num
            else:
                print("Please enter a number between 1 and 52.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    # Create a deck of cards with ranks and suits
    ranks = [str(n) for n in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    deck = list(itertools.product(ranks, suits))

    # Shuffle the deck
    random.shuffle(deck)

    num_cards = get_num_cards()

    # Draw cards
    print("You got:")
    for rank, suit in deck[:num_cards]:
        print(f"{rank} of {suit}")

    # Handle scenario: drawing all cards
    if num_cards == 52:
        print("You have drawn the entire deck!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
