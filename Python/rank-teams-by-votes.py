class Solution:
    def rankTeams(self, votes):
        ranks = {team: [0] * len(votes[0]) for team in votes[0]}
        for vote in votes:
            for i, team in enumerate(vote):
                ranks[team][i] -= 1
        return ''.join(sorted(votes[0], key=lambda x: ranks[x] + [x]))
