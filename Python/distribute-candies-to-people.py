class Solution:
    def distributeCandies(self, candies, num_people):
        left, right = 0, candies+1
        while True:
            time = (left + right) // 2
            if 0 <= candies - (1+time) * time // 2 <= time:
                break
            elif candies - (1+time) * time // 2 < 0:
                right = time
            else:
                left = time
        ans = [0] * num_people
        common_terms = time // num_people
        remain_terms = time % num_people
        for i in range(num_people):
            ans[i] = common_terms * (i+1 + i+1+(common_terms-1)*num_people) // 2
        for i in range(remain_terms):
            ans[i] += (i+1+common_terms*num_people)
        remain_candy = candies - (1+time) * time // 2
        ans[remain_terms] += remain_candy
        return ans

