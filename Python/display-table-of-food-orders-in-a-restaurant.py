class Solution:
    def displayTable(self, orders):
        mp = {}
        types = set()
        tables = set()
        for _, table, typ in orders:
            if table not in mp:
                mp[table] = {typ: 1}
            elif typ not in mp[table]:
                mp[table][typ] = 1
            else:
                mp[table][typ] += 1
            types.add(typ)
            tables.add(table)
        types = sorted(list(types))
        tables = sorted(list(tables), key=lambda x: int(x))
        ans = [["Table"]]
        for typ in types:
            ans[-1].append(typ)
        for table in tables:
            eat = mp[table]
            ans.append([str(table)])
            for i, typ in enumerate(types):
                if typ in eat:
                    ans[-1].append(str(eat[typ]))
                else:
                    ans[-1].append("0")
        return ans
