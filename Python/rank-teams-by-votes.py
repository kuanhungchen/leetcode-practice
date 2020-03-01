class Solution:
    def rankTeams(self, votes):
        """
        ranks = [..., 'A'],
                [..., 'B'],
                ...,
                [..., 'Z']
                ranks[i][j] stands for the number of position j that team i gets.
        """

        ranks = [[0 for _ in range(len(votes[0]))] + [team] for team in votes[0]]
        teams = {team: i for i, team in enumerate(votes[0])}

        for vote in votes:
            for i, c in enumerate(vote):
                ranks[teams[c]][i] -= 1
        ranks = sorted(ranks)
        return ''.join(rank[-1] for rank in ranks)
