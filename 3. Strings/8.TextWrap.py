# HackerRank Home
# HackerRank
# |
# Prepare
# Certify
# Compete
# Search
# |
# Switch to..
# A_M_Sanjeev
# PreparePythonStringsText WrapTutorial
# Text Wrap
# 15 more points to get your next star!
# Rank: 459611|Points: 205/220
# Python
# Problem
# Submissions
# Leaderboard
# Discussions
# Editorial
# Tutorial
# Textwrap
# The textwrap module provides two convenient functions: wrap() and fill().

# textwrap.wrap()
# The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
# It returns a list of output lines.

# >>> import textwrap
# >>> string = "This is a very very very very very long string."
# >>> print textwrap.wrap(string,8)
# ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
# textwrap.fill()
# The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

# >>> import textwrap
# >>> string = "This is a very very very very very long string."
# >>> print textwrap.fill(string,8)
# This is
# a very
# very
# very
# very
# very
# long
# string.
# Solve Problem

# TUTORIAL DETAILS
# NEED HELP?
# View discussions
# View editorial
# View top submissions
# BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy


import textwrap

def wrap(string, max_width):
    wrapped=textwrap.fill(string,width=max_width)  
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)