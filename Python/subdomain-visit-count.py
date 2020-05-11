import collections


class Solution:
    def subdomainVisits(self, cpdomains):
        mp = collections.defaultdict(int)
        for cpdomain in cpdomains:
            visit = int(cpdomain.split(' ')[0])
            domain = cpdomain.split(' ')[1]
            subs = list(reversed(domain.split('.')))
            cur = subs[0]
            mp[cur] += visit
            for sub in subs[1:]:
                cur = sub + "." + cur
                mp[cur] += visit

        return ["%d %s" % (v, k) for k, v in mp.items()]
