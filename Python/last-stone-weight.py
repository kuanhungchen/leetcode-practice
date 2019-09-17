class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            _first, _second = -1, -1
            _first_idx, _second_idx = -1, -1
            for idx in range(len(stones)):
                if stones[idx] > _first:
                    _first, _second = stones[idx], _first
                    _first_idx, _second_idx = idx, _first_idx
                elif stones[idx] > _second:
                    _second = stones[idx]
                    _second_idx = idx
            stones.pop(max(_first_idx, _second_idx))
            stones.pop(min(_first_idx, _second_idx))
            _new = _first - _second
            if _new != 0:
                stones.append(_new)
        return 0 if len(stones) == 0 else stones[0]
