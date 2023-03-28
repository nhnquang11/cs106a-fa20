"""
File: poll.py
-------------

Contains the Poll class, which powers a poll where people vote for options and
the poll computes a winner.
"""

class Poll:
    def __init__(self):
        pass


    def add_option(self, option):
        """
        Adds option as a valid poll choice.

        Arguments
        ---------
        option (str) -- The option value to add to the poll.
        """
        pass


    def vote_for(self, option):
        """
        Processes a vote for option.

        Argument
        --------
        option (str) -- The option to vote for.
        """
        pass


    def get_winner(self):
        """
        Returns the winner in the poll.

        Returns
        -------
        str -- The poll option that received the most votes.
        """
        pass