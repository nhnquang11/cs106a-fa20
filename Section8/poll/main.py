"""
File: main.py
-------------

Uses the Poll class to run some sample polls.
"""
from solution import Poll


def main():
    """
    >>> main()
    Professor McGonagall wins!
    """
    # Which Hogwarts professor would win in a battle?
    poll = Poll()

    poll.add_option('Professor McGonagall')
    poll.add_option('Professor Snape')
    poll.add_option('Professor Umbridge')
    poll.add_option('Professor Lupin')

    # 4 votes for McGonagall
    poll.vote_for('Professor McGonagall')
    poll.vote_for('Professor McGonagall')
    poll.vote_for('Professor McGonagall')
    poll.vote_for('Professor McGonagall')

    # 3 votes for Snape
    poll.vote_for('Professor Snape')
    poll.vote_for('Professor Snape')
    poll.vote_for('Professor Snape')

    # No votes for Umbridge (*boo*)

    # One faithful vote for our favorite werewolf
    poll.vote_for('Professor Lupin')

    print(poll.get_winner() + " wins!")



if __name__ == '__main__':
    main()