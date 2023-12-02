"""
Examples of creating objects with custom attributes and methods
"""


from numpy.random import permutation
from enum import Enum


class Suit(Enum):
    """
    This is an "Enum" or "Enumerate" class.

    Say that you have a fixed set of options for a particular property, such
    as the suit of a card (spades, hearts, diamonds, or clubs).

    Rather than storing that property as a string, such as
    >>> Card().suit = 'diamonds'
    it is more memory efficient to store the property using an Enum class:
    >>> Card().suit = Suit.DIAMONDS

    This way, you store the property as an integer (either 0, 1, 2, or 3),
    however while writing the code, you do not have to keep going back and
    forth checking what integer corresponds to which label
    """
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3


class Card:
    """
    This will be a standard card from a 52 card deck, which has both a suit a
    number associated with it
    """

    def __init__(self, suit: Suit, number: int):
        """
        The __init__ method "initializes" an instance of the class with
        whatever properties you want it to have.  This method is necessary
        to add to most classes.
        """

        # Make sure the number is valid
        if not 0 < number < 14:
            raise SyntaxError("Invalid card number")

        # Set the attributes for the card
        self.suit: Suit = suit
        self.number: int = number

    def __str__(self):
        """
        This method is used whenever you want to convert an instance of this
        object to a string.  It is not necessary to write, but if you ever
        want to print out the instance
        >>> print(Card())
        This method will dictate what string is printed.
        """

        # Identify the string associated with the number of the card
        if self.number == 1:
            num_string = "Ace"
        elif self.number == 11:
            num_string = "Jack"
        elif self.number == 12:
            num_string = "Queen"
        elif self.number == 13:
            num_string = "King"
        else:
            num_string = f'{self.number}'

        # Identify the string associated with the suit of the card
        if self.suit == Suit.SPADES:
            suit_string = "spades"
        elif self.suit == Suit.HEARTS:
            suit_string = "hearts"
        elif self.suit == Suit.DIAMONDS:
            suit_string = "diamonds"
        elif self.suit == Suit.CLUBS:
            suit_string = "clubs"
        else:
            raise SyntaxError("Invalid suit")

        # return the string
        return f'{num_string} of {suit_string}'


class Deck:
    """
    This will be a collection of all the cards in a 52 card deck, which
    can be shuffled and have cards removed/added
    """

    def __init__(self):
        """
        Initialize a deck with all 52 cards
        """

        # Initialize an empty list of cards
        self.cards = []

        # Add the cards one by one
        for suit in [Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS]:
            for num in range(1, 14):
                self.cards.append(Card(suit, num))

    def count(self):
        """
        Gets a count of the number of cards currently in the deck
        """

        return len(self.cards)

    def shuffle(self):
        """
        Rearranges the list of cards
        """

        # Use the NumPy permutation command
        self.cards = permutation(self.cards)

    def deal_cards(self, n=1):
        """
        Deals out n cards, and removes these from the deck
        """

        if n > self.count():
            raise SyntaxError('Cannot deal more cards than '
                              'there are currently in the deck')
        yield self.cards[:n]
        self.cards = self.cards[n:]

