class Solution:
    def connect(self, root):
        nodes = [[root], []]
        x = 0
        while (nodes[0] and nodes[0][0]) or (nodes[1] and nodes[1][0]):
            for i in range(len(nodes[x])):
                nodes[x][i].next = None if i == len(nodes[x]) - 1 else nodes[x][i+1]
                nodes[(1 + x) % 2].append(nodes[x][i].left)
                nodes[(1 + x) % 2].append(nodes[x][i].right)
            nodes[x] = []
            x = (1 + x) % 2
        return root
