"""
Examples of creating objects with custom attributes and methods
"""


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
