class DivisorGame:

    def __init__(self):
        self.memo = dict()

    """
    Alice and Bob take turns playing a game, with Alice starting first.

    Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

        Choosing any x with 0 < x < N and N % x == 0.
        Replacing the number N on the chalkboard with N - x.

    Also, if a player cannot make a move, they lose the game.

    Return True if and only if Alice wins the game, assuming both players play optimally.



    Example 1:

    Input: 2
    Output: true
    Explanation: Alice chooses 1, and Bob has no more moves.

    Example 2:

    Input: 3
    Output: false
    Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

    """

    def divisorGame(self, N: int) -> bool:
        """
        Solution: dynamic programming, memoization
        win(n) = not win(n-x) where n%x == 0


        :param N:
        :return:
        """
        if N == 1:
            self.memo.clear()
            return False

        if N in self.memo:
            return self.memo[N]

        for x in range(1, N):
            # Found divisor with lose
            if N % x == 0 and not self.divisorGame(N - x):
                self.memo[N] = True
                return True

        self.memo[N] = False
        return False
