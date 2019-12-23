class Solution:
    def maxCandies(self, status, candies, keys, conBs, iniBs):
        def grab(box, hkeys):
            candyGain = 0
            if status[box] == 1 or (status[box] == 0 and box in hkeys.keys()):
                # if box is open or we have its key, then start grabbing
                status[box] = 2  # set to grabbed-already, then we won't grab it again
                for key in keys[box]:
                    # collect keys in this box
                    if key not in hkeys: hkeys[key] = 1
                candyGain = candies[box]  # grab candies in this box

                lastKeys = {}
                while True:
                    for conB in conBs[box]:
                        tmp, hkeys = grab(conB, hkeys)
                        candyGain += tmp
                    if lastKeys == hkeys: break  # we may have new keys each time we grab, so only stop at the
                    lastKeys = hkeys  # moment when we have exactly same keys after grabbing

            return candyGain, hkeys

        totalCandy = 0
        keysOwned = {}
        for iniB in iniBs:
            if status[iniB] == 0: continue
            for key in keys[iniB]:  # prepare our keys at the beginning
                if key not in keysOwned: keysOwned[key] = 1

        for iniB in iniBs:
            tmp, keysOwned = grab(iniB, keysOwned)  # grab each box we have at the beginning
            totalCandy += tmp
        return totalCandy
