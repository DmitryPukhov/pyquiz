import itertools
from collections import defaultdict
from itertools import groupby
from typing import List


class MostVisitedPattern:
    """
    We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].
    A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
    (The websites in a 3-sequence are not necessarily distinct.)
    Find the 3-sequence visited by the largest number of users.
    If there is more than one solution, return the lexicographically smallest such 3-sequence.

    Example 1:

    Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
    Output: ["home","about","career"]
    Explanation:
    The tuples in this example are:
    ["joe", 1, "home"]
    ["joe", 2, "about"]
    ["joe", 3, "career"]
    ["james", 4, "home"]
    ["james", 5, "cart"]
    ["james", 6, "maps"]
    ["james", 7, "home"]
    ["mary", 8, "home"]
    ["mary", 9, "about"]
    ["mary", 10, "career"]
    The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
    The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
    The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
    The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
    The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.


    Note:
    3 <= N = username.length = timestamp.length = website.length <= 50
    1 <= username[i].length <= 10
    0 <= timestamp[i] <= 10^9
    1 <= website[i].length <= 10
    Both username[i] and website[i] contain only lowercase characters.
    It is guaranteed that there is at least one user who visited at least 3 websites.
    No user visits two websites at the same time.
    """

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        uservisits = defaultdict(list)
        visits = sorted(zip(username, timestamp, website), key=lambda x: x[1])

        for user, time, website in visits:
            uservisits[user].append(website)
        # For each combination of 3 websites store users, visited them
        # (website1, website2, website3) -> set of users
        ws3users = defaultdict(set)
        for user in uservisits:
            # Get all combinations of 3 websites for user
            userwebsites = uservisits[user]
            combs3 = set(itertools.combinations(userwebsites, 3))
            for comb in combs3:
                ws3users[comb].add(user)
        maxseq = max(sorted(ws3users.keys()), key=lambda seq: len(list(ws3users[seq]))) if ws3users else []
        return list(maxseq)
