# leetcode-practice
* Try to solve [leetcode](https://leetcode.com/) problems as many as possible!
* This repository may contain not only my own solutions but some amazing ones from others.
* All stuff that I look up during coding may be collected in here also.
 
## Tags

|  👻 |  👅 |  🏁 |  🌈 |  💎 | 
|:---:|:---:|:---:|:---:|:---:|
|[Array](#array)|[Dynamic Programming](#dynamic-programming)|[Math](#math)|[String](#string)|[Tree](#tree)|
|[Hash Table](#hash-table)|[Depth-first Search](#depth-first-search)|[Binary Search](#binary-search)|[Greedy](#greedy)|[Two Pointers](#two-pointers)|
|[Breadth First Search](#breadth-first-search)|[Stack](#stack)|[Backtracking](#backtracking)|[Design](#design)|[Linked List](#linked-list)|
|[Graph](#graph)|[Sort](#sort)|[Bit Manipulation](#bit-manipulation)|[Heap](#heap)|[Divide and Conquer](#divide-and-conquer)|
|[Recursion](#recursion)|[Ordered Map](#ordered-map)|[Brainteaser](#brainteaser)|[Geometry](#geometry)|[Line Sweep](#line-sweep)|
|[Binary Search Tree](#binary-search-tree)|[No category](#no-category)||||

## Contest notes
- Global Ranking: 6811/93877 (updated: 04/29/2020)
- Taiwan Ranking: 146/1143 (updated: 04/30/2020)

|  👻 |  👅 |  🏁 |  🌈 |  💎 | 
|:---:|:---:|:---:|:---:|:---:|
|[Weekly 184](https://kuanhungchen.github.io/2020/04/25/LeetCode-Weekly-Contest-184/)|[Biweekly 23](https://kuanhungchen.github.io/2020/04/05/LeetCode-Biweekly-Contest-23/)|[Weekly 182](https://kuanhungchen.github.io/2020/04/01/LeetCode-Weekly-Contest-182/)|[Weekly 181](https://kuanhungchen.github.io/2020/04/03/LeetCode-Weekly-Contest-181/)|[Weekly 178](https://kuanhungchen.github.io/2020/03/02/LeetCode-Weekly-Contest-178/)|

## Notes

* [lru-cache.md](./notes/lru-cache.md)
* [collections](./notes/collections.md)
* [str-vs-repr](./notes/str-vs-repr.md)
* [zip](./notes/zip.md)

## Array

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0001|[Two Sum](https://leetcode.com/problems/two-sum/)|[two-sum.py](./Python/two-sum.py)| Easy | |
| 0026|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|[remove-duplicates-from-sorted-array.py](./Python/remove-duplicates-from-sorted-array.py)| Easy | |
| 0027|[Remove Element](https://leetcode.com/problems/remove-element/)|[remove-element.py](./Python/remove-element.py)| Easy | |
| 0033|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|[search-in-rotated-sorted-array.py](./Python/search-in-rotated-sorted-array.py)| Medium | |
| 0034|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)|[find-first-and-last-position-of-element-in-sorted-array.py](./Python/find-first-and-last-position-of-element-in-sorted-array.py)| Medium | |
| 0035|[Search Insert Position](https://leetcode.com/problems/search-insert-position/)|[search-insert-position.py](./Python/search-insert-position.py)| Easy | |
| 0053|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[maximum-subarray.py](./Python/maximum-subarray.py)| Easy | |
| 0055|[Jump Game](https://leetcode.com/problems/jump-game/)|[jump-game.py](./Python/jump-game.py)| Medium | | 
| 0056|[Merge Intervals](https://leetcode.com/problems/merge-intervals/)|[merge-intervals.py](./Python/merge-intervals.py)| Medium | |
| 0062|[Unique Paths](https://leetcode.com/problems/unique-paths/)|[unique-paths.py](./Python/unique-paths.py)| Medium | |
| 0063|[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)|[unique-paths-ii.py](./Python/unique-paths-ii.py)| Medium | |
| 0066|[Plus One](https://leetcode.com/problems/plus-one/)|[plus-one.py](./Python/plus-one.py)| Easy | |
| 0075|[Sort Colors](https://leetcode.com/problems/sort-colors/)|[sort-colors.py](./Python/sort-colors.py)| Medium | |
| 0080|[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)|[remove-duplicates-from-sorted-array-ii.py](./Python/remove-duplicates-from-sorted-array-ii.py)| Medium | |
| 0088|[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|[merge-sorted-array.py](./Python/merge-sorted-array.py)| Easy | |
| 0118|[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)|[pascal's-triangle.py](./Python/pascal's-triangle.py)| Easy | |
| 0119|[Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)|[pascal's-triangle-ii.py](./Python/pascal's-triangle-ii.py)| Easy | |
| 0121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|[best-time-to-buy-and-sell-stock.py](./Python/best-time-to-buy-and-sell-stock.py)| Easy | |
| 0122|[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|[best-time-to-buy-and-sell-stock-ii.py](./Python/best-time-to-buy-and-sell-stock-ii.py)| Easy | |
| 0162|[Find Peak Element](https://leetcode.com/problems/find-peak-element/)|[find-peak-element](./Python/find-peak-element.py)| Medium | |
| 0167|[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|[two-sum-ii-input-array-is-sorted.py](./Python/two-sum-ii-input-array-is-sorted.py)| Easy | |
| 0169|[Majority Element](https://leetcode.com/problems/majority-element/)|[majority-element.py](./Python/majority-element.py)| Easy | |
| 0189|[Rotate Array](https://leetcode.com/problems/rotate-array/)|[rotate-array.py](./Python/rotate-array.py)| Easy | |
| 0217|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|[contains-duplicate.py](./Python/contains-duplicate.py)| Easy | |
| 0219|[Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)|[contains-duplicate-ii.py](./Python/contains-duplicate-ii.py)| Easy | |
| 0228|[Summary Ranges](https://leetcode.com/problems/summary-ranges/)|[summary-ranges.py](./Python/summary-ranges.py)| Medium | |
| 0238|[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)|[product-of-array-except-self.py](./Python/product-of-array-except-self.py)| Medium | |
| 0268|[Missing Number](https://leetcode.com/problems/missing-number)|[missing-number.py](./Python/missing-number.py)| Easy | |
| 0283|[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|[move-zeroes.py](./Python/move-zeroes.py)| Easy | |
| 0287|[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)|[find-the-duplicate-number.py](./Python/find-the-duplicate-number.py)| Medium | |
| 0414|[Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)|[third-maximum-number.py](./Python/third-maximum-number.py)| Easy | | 
| 0448|[Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)|[find-all-numbers-disappeared-in-an-array.py](./Python/find-all-numbers-disappeared-in-an-array.py)| Easy | |
| 0457|[Circular Array Loop](https://leetcode.com/problems/circular-array-loop/)|[circular-array-loop.py](./Python/circular-array-loop.py)| Medium | |
| 0485|[Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)|[max-consecutive-ones.py](./Python/max-consecutive-ones.py)| Easy | |
| 0509|[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)|[fibonacci-number.py](./Python/fibonacci-number.py)| Easy | |
| 0532|[K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)|[k-diff-pairs-in-an-array.py](./Python/k-diff-pairs-in-an-array.py)| Easy | |
| 0560|[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)|[subarray-sum-equals-k.py](./Python/subarray-sum-equals-k.py)| Medium | hash table |
| 0561|[Array Partition I](https://leetcode.com/problems/array-partition-i/)|[array-partition-i.py](./Python/array-partition-i.py)| Easy | |
| 0566|[Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/)|[reshape-the-matrix.py](./Python/reshape-the-matrix.py)| Easy | |
| 0605|[Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)|[can-place-flowers.py](./Python/can-place-flowers.py)| Easy | |
| 0628|[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/)|[maximum-product-of-three-numbers.py](./Python/maximum-product-of-three-numbers.py)| Easy | |
| 0643|[Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)|[maximum-average-subarray-i.py](./Python/maximum-average-subarray-i.py)| Easy | |
| 0674|[Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)|[longest-continuous-increasing-subsequence.py](./Python/longest-continuous-increasing-subsequence.py)| Easy | |
| 0695|[Max Area of Island](https://leetcode.com/problems/max-area-of-island/)|[max-area-of-island.py](./Python/max-area-of-island.py)| Medium | |
| 0697|[Degree of an Array](https://leetcode.com/problems/degree-of-an-array/)|[degree-of-an-array.py](./Python/degree-of-an-array.py)| Easy | |
| 0717|[1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters)|[1-bit-and-2-bit-characters.py](./Python/1-bit-and-2-bit-characters.py)| Easy | |
| 0724|[Find Pivot Index](https://leetcode.com/problems/find-pivot-index/submissions/)|[find-pivot-index.py](./Python/find-pivot-index.py)| Easy | |
| 0746|[Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)|[min-cost-climbing-stairs.py](./Python/min-cost-climbing-stairs.py)| Easy | |
| 0747|[Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/)|[largest-number-at-least-twice-of-others.py](./Python/largest-number-at-least-twice-of-others.py)| Easy | |
| 0766|[Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)|[toeplitz-matrix.py](./Python/toeplitz-matrix.py)| Easy | |
| 0830|[Positions of Large Groups](https://leetcode.com/problems/positions-of-large-groups/)|[positions-of-large-groups.py](./Python/positions-of-large-groups.py)| Easy | |
| 0832|[Flipping an Image](https://leetcode.com/problems/flipping-an-image)|[flipping-an-image.py](./Python/flipping-an-image.py)| Easy | |
| 0849|[Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/)|[maximize-distance-to-closest-person.py](./Python/maximize-distance-to-closest-person.py)| Easy | |
| 0867|[Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)|[transpose-matrix.py](./Python/transpose-matrix.py)| Easy | |
| 0888|[Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/)|[fair-candy-swap.py](./Python/fair-candy-swap.py)| Easy | |
| 0896|[Monotonic Array](https://leetcode.com/problems/monotonic-array/)|[monotonic-array](./Python/monotonic-array.py)| Easy | |
| 0905|[Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)|[sort-array-by-parity.py](./Python/sort-array-by-parity.py)| Easy | |
| 0914|[X of A Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)|[x-of-a-kind-in-a-deck-of-cards.py](./Python/x-of-a-kind-in-a-deck-of-cards.py)| Easy | |
| 0915|[Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)|[partition-array-into-disjoint-intervals.py](./Python/partition-array-into-disjoint-intervals.py)| Medium | |
| 0922|[Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)|[sort-array-by-parity-ii.py](./Python/sort-array-by-parity-ii.py)| Easy | |
| 0926|[Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/)|[flip-string-to-monotone-increasing.py](./Python/flip-string-to-monotone-increasing.py)| Medium | |
| 0941|[Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)|[valid-mountain-array.py](./Python/valid-mountain-array.py)| Easy | |
| 0950|[Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/)|[reveal-cards-in-increasing-order.py](./Python/reveal-cards-in-increasing-order.py)| Medium | |
| 0969|[Pancake Sorting](https://leetcode.com/problems/pancake-sorting/)|[pancake-sorting.py](./Python/pancake-sorting.py)| Medium | |
| 0977|[Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)|[squares-of-a-sorted-array.py](./Python/squares-of-a-sorted-array.py)| Easy | |
| 0985|[Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)|[sum-of-even-numbers-after-queries.py](./Python/sum-of-even-numbers-after-queries.py)| Easy | |
| 0989|[Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/)|[add-to-array-form-of-integer.py](./Python/add-to-array-form-of-integer.py)| Easy | |
| 0999|[Available Captures for Rook](https://leetcode.com/problems/available-captures-for-rook/)|[available-captures-for-rook](./Python/available-captures-for-rook.py)| Easy | |
| 1002|[Find Common Characters](https://leetcode.com/problems/find-common-characters/)|[find-common-characters.py](./Python/find-common-characters.py)| Easy | [collections](./notes/collections.md) |
| 1010|[Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)|[pairs-of-songs-with-total-durations-divisible-by-60.py](./Python/pairs-of-songs-with-total-durations-divisible-by-60.py)| Easy | |
| 1013|[Partition Array Into Three Parts With Equal Sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/)|[partition-array-into-three-parts-with-equal-sum](./Python/partition-array-into-three-parts-with-equal-sum.py)| Easy | |
| 1018|[Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/)|[binary-prefix-divisible-by-5.py](./Python/binary-prefix-divisible-by-5.py)| Easy | |
| 1051|[Height Checker](https://leetcode.com/problems/height-checker/)|[height-checker.py](./Python/height-checker.py)| Easy | |
| 1074|[Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)|[number-of-submatrices-that-sum-to-target.py](./Python/number-of-submatrices-that-sum-to-target.py)| Hard | |
| 1089|[Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)|[duplicate-zeros.py](./Python/duplicate-zeros.py)| Easy | |
| 1122|[Relative Sort Array](https://leetcode.com/problems/relative-sort-array/)|[relative-sort-array.py](./Python/relative-sort-array.py)| Easy | |
| 1128|[Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)|[number-of-equivalent-domino-pairs.py](./Python/number-of-equivalent-domino-pairs.py)| Easy | [str-vs-repr](./notes/str-vs-repr.md) |
| 1160|[Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)|[find-words-that-can-be-formed-by-characters.py](./Python/find-words-that-can-be-formed-by-characters.py)| Easy | |
| 1170|[Compare Strings by Frequency of the Smallest Character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)|[compare-strings-by-frequency-of-the-smallest-character.py](./Python/compare-strings-by-frequency-of-the-smallest-character.py)| Easy | |
| 1184|[Distance Between Bus Stops](https://leetcode.com/problems/distance-between-bus-stops/)|[distance-between-bus-stops.py](./Python/distance-between-bus-stops.py)| Easy | |
| 1185|[Day of the Week](https://leetcode.com/problems/day-of-the-week/)|[day-of-the-week.py](./Python/day-of-the-week.py)| Easy | |
| 1200|[Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)|[minimum-absolute-difference.py](./Python/minimum-absolute-difference.py)| Easy | |
| 1208|[Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/)|[get-equal-substrings-within-budget.py](./Python/get-equal-substrings-within-budget.py)| Medium | |
| 1213|[Intersection of Three Sorted Arrays](https://leetcode.com/contest/biweekly-contest-10/problems/intersection-of-three-sorted-arrays/)|[intersection-of-three-sorted-arrays.py](./Python/intersection-of-three-sorted-arrays.py)| Easy | Premium only |
| 1217|[Play with Chips](https://leetcode.com/problems/play-with-chips/)|[play-with-chips.py](./Python/play-with-chips.py)| Easy | |
| 1222|[Queens That Can Attack the King](https://leetcode.com/problems/queens-that-can-attack-the-king/)|[queens-that-can-attack-the-king.py](./Python/queens-that-can-attack-the-king.py)| Medium | |
| 1232|[Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)|[check-if-it-is-a-straight-line.py](./Python/check-if-it-is-a-straight-line.py)| Easy | |
| 1233|[Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)|[remove-sub-folders-from-the-filesystem.py](./Python/remove-sub-folders-from-the-filesystem.py)| Medium | |
| 1266|[Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)|[minimum-time-visiting-all-points.py](./Python/minimum-time-visiting-all-points.py)| Easy | |
| 1267|[Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/)|[count-servers-that-communicate.py](./Python/count-servers-that-communicate.py)| Medium | |
| 1275|[Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)|[find-winner-on-a-tic-tac-toe-game.py](./Python/find-winner-on-a-tic-tac-toe-game.py)| Easy | |
| 1287|[Element Appearing More Than 25% In Sorted Array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/)|[element-appearing-more-than-25-in-sorted-array.py](./Python/element-appearing-more-than-25-in-sorted-array.py)| Easy | |
| 1292|[Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)|[maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold](./Python/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold.py)| Medium | |
| 1295|[Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)|[find-numbers-with-even-number-of-digits.py](./Python/find-numbers-with-even-number-of-digits.py)| Easy | |
| 1296|[Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)|[divide-array-in-sets-of-k-consecutive-numbers.py](./Python/divide-array-in-sets-of-k-consecutive-numbers.py)| Medium | |
| 1313|[Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/)|[decompress-run-length-encoded-list.py](./Python/decompress-run-length-encoded-list.py)| Easy | |
| 1351|[Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)|[count-negative-numbers-in-a-sorted-matrix.py](./Python/count-negative-numbers-in-a-sorted-matrix.py)| Easy | |
| 1352|[Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/)|[product-of-the-last-k-numbers.py](./Python/product-of-the-last-k-numbers.py)| Medium | |
| 1365|[How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)|[how-many-numbers-are-smaller-than-the-current-number.py](./Python/how-many-numbers-are-smaller-than-the-current-number.py)| Easy | |
| 1366|[Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)|[rank-teams-by-votes.py](./Python/rank-teams-by-votes.py)| Medium | |
| 1380|[Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/)|[lucky-numbers-in-a-matrix.py](./Python/lucky-numbers-in-a-matrix.py)| Easy | |
| 1375|[Bulb Switcher III](https://leetcode.com/problems/bulb-switcher-iii/)|[bulb-switcher-iii.py](./Python/bulb-switcher-iii.py)| Medium | |
| 1385|[Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)|[find-the-distance-value-between-two-arrays.py](./Python/find-the-distance-value-between-two-arrays.py)| Easy | |
| 1389|[Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/)|[create-target-array-in-the-given-order.py](./Python/create-target-array-in-the-given-order.py)| Easy | |
| 1394|[Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array/)|[find-lucky-integer-in-an-array.py](./Python/find-lucky-integer-in-an-array.py)| Easy | |
| 1395|[Count Number of Teams](https://leetcode.com/problems/count-number-of-teams/)|[count-number-of-teams](./Python/count-number-of-teams.py)| Medium | |
| 1399|[Count Largest Group](https://leetcode.com/problems/count-largest-group/)|[count-largest-group.py](./Python/count-largest-group.py)| Easy | |
| 1409|[Queries on a Permutation With Key](https://leetcode.com/problems/queries-on-a-permutation-with-key/)|[queries-on-a-permutation-with-key.py](./Python/queries-on-a-permutation-with-key.py)| Medium | |
| 1413|[Minimum Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/)|[minimum-value-to-get-positive-step-by-step-sum.py](./Python/minimum-value-to-get-positive-step-by-step-sum.py)| Easy | |
| 1414|[Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)|[find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k.py](./Python/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k.py)| Medium | |
| 1423|[Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)|[maximum-points-you-can-obtain-from-cards.py](./Python/maximum-points-you-can-obtain-from-cards.py)| Medium | |
| 1424|[Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/)|[diagonal-traverse-ii.py](./Python/diagonal-traverese-ii.py)| Medium | |

## Dynamic Programming

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0053|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[maximum-subarray.py](./Python/maximum-subarray.py)| Easy | |
| 0062|[Unique Paths](https://leetcode.com/problems/unique-paths/)|[unique-paths.py](./Python/unique-paths.py)| Medium | |
| 0063|[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)|[unique-paths-ii.py](./Python/unique-paths-ii.py)| Medium | |
| 0121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|[best-time-to-buy-and-sell-stock.py](./Python/best-time-to-buy-and-sell-stock.py)| Easy | |
| 0198|[House Robber](https://leetcode.com/problems/house-robber/)|[house-robber.py](./Python/house-robber.py)| Easy | |
| 0221|[Maximal Square](https://leetcode.com/problems/maximal-square/)|[maximal-square.py](./Python/maximal-square.py)| Medium | | 
| 0303|[Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)|[range-sum-query-immutable.py](./Python/range-sum-query-immutable.py)| Easy | |
| 0338|[Counting Bits](https://leetcode.com/problems/counting-bits/)|[counting-bits.py](./Python/counting-bits.py)| Medium | |
| 0392|[Is Subsequence](https://leetcode.com/problems/is-subsequence/)|[is-subsequence.py](./Python/is-subsequence.py)| Easy | |
| 0523|[Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)|[continuous-subarray-sum.py](./Python/continuous-subarray-sum.py)| Medium | |
| 0638|[Shopping Offers](https://leetcode.com/problems/shopping-offers/)|[shopping-offers.py](./Python/shopping-offers.py)| Medium | |
| 0746|[Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)|[min-cost-climbing-stairs.py](./Python/min-cost-climbing-stairs.py)| Easy | |
| 1025|[Divisor Game](https://leetcode.com/problems/divisor-game/)|[divisor-game.py](./Python/divisor-game.py)| Easy | |
| 1027|[Longest Arithmetic Sequence](https://leetcode.com/problems/longest-arithmetic-sequence/)|[longest-arithmetic-sequence.py](./Python/longest-arithmetic-sequence.py)| Medium | |
| 1074|[Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)|[number-of-submatrices-that-sum-to-target.py](./Python/number-of-submatrices-that-sum-to-target.py)| Hard | |
| 1143|[Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|[longest-common-subsequence.py](./Python/longest-common-subsequence.py)| Medium | |
| 1186|[Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)|[maximum-subarray-sum-with-one-deletion.py](./Python/maximum-subarray-sum-with-one-deletion.py)| Medium | |
| 1218|[Longest Arithmetic Subsequence of Given Difference](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)|[longest-arithmetic-subsequence-of-given-difference.py](./Python/longest-arithmetic-subsequence-of-given-difference.py)| Medium | |
| 1262|[Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)|[greatest-sum-divisible-by-three.py](./Python/greatest-sum-divisible-by-three.py)| Medium | |
| 1367|[Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/)|[linked-list-in-binary-tree.py](./Python/linked-list-in-binary-tree.py)| Medium | |
| 1359|[Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)|[count-all-valid-pickup-and-delivery-options.py](./Python/count-all-valid-pickup-and-delivery-options.py)| Hard | |
| 1402|[Reducing Dishes](https://leetcode.com/problems/reducing-dishes/)|[reducing-dishes.py](./Python/reducing-dishes.py)| Hard | |
| 1405|[Longest Happy String](https://leetcode.com/problems/longest-happy-string/)|[longest-happy-string.py](./Python/longest-happy-string.py)| Medium | |
| 1406|[Stone Game III](https://leetcode.com/problems/stone-game-iii/)|[stone-game-iii.py](./Python/stone-game-iii.py)| Hard | |
| 1411|[Number of Ways to Paint N x 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)|[number-of-ways-to-paint-n-3-grid.py](./Python/number-of-ways-to-paint-n-3-grid.py)| Hard | |
| 1423|[Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)|[maximum-points-you-can-obtain-from-cards.py](./Python/maximum-points-you-can-obtain-from-cards.py)| Medium | |
| 1424|[Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/)|[diagonal-traverse-ii.py](./Python/diagonal-traverese-ii.py)| Medium | |

## Math

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0069|[Sqrt(x)](https://leetcode.com/problems/sqrtx/)|[sqrtx.py](./Python/sqrtx.py)| Easy | |
| 0166|[Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)|[fraction-to-recurring-decimal](./Python/fraction-to-recurring-decimal.py)| Medium | |
| 0202|[Happy Number](https://leetcode.com/problems/happy-number/)|[happy-number.py](./Python/happy-number.py)| Easy | |
| 0223|[Rectangle Area](https://leetcode.com/problems/rectangle-area/)|[rectangle-area.py](./Python/rectangle-area.py)| Medium | |
| 0268|[Missing Number](https://leetcode.com/problems/missing-number)|[missing-number.py](./Python/missing-number.py)| Easy | |
| 0367|[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)|[valid-perfect-square.py](./Python/valid-perfect-square.py)| Easy | |
| 0441|[Arranging Coins](https://leetcode.com/problems/arranging-coins/)|[arranging-coins.py](./Python/arranging-coins.py)| Easy | |
| 0523|[Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)|[continuous-subarray-sum.py](./Python/continuous-subarray-sum.py)| Medium | |
| 0628|[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/)|[maximum-product-of-three-numbers.py](./Python/maximum-product-of-three-numbers.py)| Easy | |
| 0640|[Solve the Equation](https://leetcode.com/problems/solve-the-equation/)|[solve-the-equation.py](./Python/solve-the-equation.py)| Medium | |
| 0892|[Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/)|[surface-area-of-3d-shapes.py](./Python/surface-area-of-3d-shapes.py)| Easy | |
| 0908|[Smallest Range I](https://leetcode.com/problems/smallest-range-i/)|[smallest-range-i.py](./Python/smallest-range-i.py)| Easy | |
| 0910|[Smallest Range II](https://leetcode.com/problems/smallest-range-ii/)|[smallest-range-ii.py](./Python/smallest-range-ii.py)| Medium | |
| 0914|[X of A Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)|[x-of-a-kind-in-a-deck-of-cards.py](./Python/x-of-a-kind-in-a-deck-of-cards.py)| Easy | |
| 0942|[DI String Match](https://leetcode.com/problems/di-string-match/)|[di-string-match.py](./Python/di-string-match.py)| Easy | |
| 0949|[Largest Time for Given Digits](https://leetcode.com/problems/largest-time-for-given-digits/)|[largest-time-for-given-digits.py](./Python/largest-time-for-given-digits.py)| Easy | |
| 0970|[Powerful Integers](https://leetcode.com/problems/powerful-integers/)|[powerful-integers.py](./Python/powerful-integers.py)| Easy | |
| 1025|[Divisor Game](https://leetcode.com/problems/divisor-game/)|[divisor-game.py](./Python/divisor-game.py)| Easy | |
| 1103|[Distribute Candies to People](https://leetcode.com/problems/distribute-candies-to-people/)|[distribute-candies-to-people.py](./Python/distribute-candies-to-people.py)| Easy | |
| 1154|[Day of the Year](https://leetcode.com/problems/day-of-the-year/)|[day-of-the-year.py](./Python/day-of-the-year.py)| Easy | |
| 1201|[Ugly Number III](https://leetcode.com/problems/ugly-number-iii/)|[ugly-number-iii.py](./Python/ugly-number-iii.py)| Medium | |
| 1217|[Play with Chips](https://leetcode.com/problems/play-with-chips/)|[play-with-chips.py](./Python/play-with-chips.py)| Easy | |
| 1218|[Longest Arithmetic Subsequence of Given Difference](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)|[longest-arithmetic-subsequence-of-given-difference.py](./Python/longest-arithmetic-subsequence-of-given-difference.py)| Medium | |
| 1232|[Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)|[check-if-it-is-a-straight-line.py](./Python/check-if-it-is-a-straight-line.py)| Easy | |
| 1271|[Hexspeak](https://leetcode.com/problems/hexspeak/)|[hexspeak.py](./Python/hexspeak.py)| Easy | |
| 1272|[Remove Interval](https://leetcode.com/problems/remove-interval/)|[remove-interval.py](./Python/remove-interval.py)| Medium | |
| 1281|[Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)|[subtract-the-product-and-sum-of-digits-of-an-integers.py](./Python/subtract-the-product-and-sum-of-digits-of-an-integer.py)| Easy | |
| 1359|[Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)|[count-all-valid-pickup-and-delivery-options.py](./Python/count-all-valid-pickup-and-delivery-options.py)| Hard | |
| 1390|[Four Divisors](https://leetcode.com/problems/four-divisors/)|[four-divisors.py](./Python/four-divisors.py)| Medium | |

## String

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0028|[Implement strStr()](https://leetcode.com/problems/implement-strstr/)|[implement-strstr.py](./Python/implement-strstr.py)| Easy | |
| 0049|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|[group-anagrams.py](./Python/group-anagrams.py)| Medium | |
| 0093|[Restore IP Address](https://leetcode.com/problems/restore-ip-addresses/)|[restore-ip-address.py](./Python/restore-ip-address.py)| Medium | |
| 0125|[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|[valid-palindrome.py](./Python/valid-palindrome.py)| Easy | |
| 0344|[Reverse String](https://leetcode.com/problems/reverse-string/)|[reverse-string.py](./Python/reverse-string.py)| Easy | |
| 0345|[Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)|[reverse-vowels-of-a-string.py](./Python/reverse-vowels-of-a-string.py)| Easy | |
| 0383|[Ransom Note](https://leetcode.com/problems/ransom-note/)|[ransom-note.py](./Python/ransom-note.py)| Easy | |
| 0387|[First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)|[first-unique-character-in-a-string.py](./Python/first-unique-character-in-a-string.py)| Easy | |
| 0459|[Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)|[repeated-substring-pattern.py](./Python/repeated-substring-pattern.py)| Easy | |
| 0606|[Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)|[construct-string-from-binary-tree.py](./Python/construct-string-from-binary-tree.py)| Easy | |
| 0680|[Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)|[valid-palindrome-ii.py](./Python/valid-palindrome-ii.py)| Easy | |
| 0709|[To Lower Case](https://leetcode.com/problems/to-lower-case/)|[to-lower-case.py](./Python/to-lower-case.py)| Easy | |
| 0791|[Custom Sort String](https://leetcode.com/problems/custom-sort-string/)|[custom-sort-string.py](./Python/custom-sort-string.py)| Medium | |
| 0809|[Expressive Words](https://leetcode.com/problems/expressive-words/)|[expressive-words.py](./Python/expressive-words.py)| Medium | |
| 0824|[Goat Latin](https://leetcode.com/problems/goat-latin/)|[goat-latin.py](./Python/goat-latin.py)| Easy | |
| 0848|[Shifting Letters](https://leetcode.com/problems/shifting-letters/)|[shifting-letters.py](./Python/shifting-letters.py)| Medium | |
| 0859|[Buddy Strings](https://leetcode.com/problems/buddy-strings/)|[buddy-strings.py](./Python/buddy-strings.py)| Easy | |
| 0890|[Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)|[find-and-replace-pattern.py](./Python/find-and-replace-pattern.py)| Medium | |
| 0916|[Word Subsets](https://leetcode.com/problems/word-subsets/)|[word-subsets.py](./Python/word-subsets.py)| Medium | |
| 0925|[Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)|[long-pressed-name.py](./Python/long-pressed-name.py)| Easy | |
| 0929|[Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/)|[unique-email-addresses.py](./Python/unique-email-addresses.py)| Easy | |
| 1071|[Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)|[greatest-common-divisor-of-strings.py](./Python/greatest-common-divisor-of-strings.py)| Easy | |
| 1108|[Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/)|[defanging-an-ip-address.py](./Python/defanging-an-ip-address.py)| Easy | |
| 1170|[Compare Strings by Frequency of the Smallest Character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)|[compare-strings-by-frequency-of-the-smallest-character.py](./Python/compare-strings-by-frequency-of-the-smallest-character.py)| Easy | |
| 1189|[Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)|[maximum-number-of-balloons.py](./Python/maximum-number-of-balloons.py)| Easy | |
| 1233|[Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)|[remove-sub-folders-from-the-filesystem.py](./Python/remove-sub-folders-from-the-filesystem.py)| Medium | |
| 1234|[Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)|[replace-the-substring-for-balanced-string.py](./Python/replace-the-substring-for-balanced-string.py)| Medium | |
| 1247|[Minimum Swaps to Make Strings Equal](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/)|[minimum-swaps-to-make-strings-equal.py](./Python/minimum-swaps-to-make-strings-equal.py)| Medium | |
| 1268|[Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)|[search-suggestions-system.py](./Python/search-suggestions-system.py)| Medium | |
| 1271|[Hexspeak](https://leetcode.com/problems/hexspeak/)|[hexspeak.py](./Python/hexspeak.py)| Easy | |
| 1297|[Maximum Number of Occurrences of a Substring](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/)|[maximum-number-of-occurrences-of-a-substring.py](./Python/maximum-number-of-occurrences-of-a-substring.py)| Medium | |
| 1358|[Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)|[number-of-substrings-containing-all-three-characters.py](./Python/number-of-substrings-containing-all-three-characters.py)| Medium | |
| 1370|[Increasing Decreasing String](https://leetcode.com/problems/increasing-decreasing-string/)|[increasing-decreasing-string.py](./Python/increasing-decreasing-string.py)| Easy | |
| 1374|[Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/)|[generate-a-string-with-characters-that-have-odd-counts.py](./Python/generate-a-string-with-characters-that-have-odd-counts.py)| Easy | |
| 1392|[Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)|[longest-happy-prefix.py](./Python/longest-happy-prefix.py)| Hard | |
| 1404|[Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)|[number-of-steps-to-reduce-a-number-in-binary-representation-to-one.py](./Python/number-of-steps-to-reduce-a-number-in-binary-representation-to-one.py)| Medium | |
| 1408|[String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/)|[string-matching-in-an-array.py](./Python/string-matching-in-an-array.py) | Easy | |
| 1410|[HTML Entity Parser](https://leetcode.com/problems/html-entity-parser/)|[html-entity-parser.py](./Python/html-entity-parser.py)| Medium | |
| 1417|[Reformat The String](https://leetcode.com/problems/reformat-the-string/)|[reformat-the-string.py](./Python/reformat-the-string.py)| Easy | |
| 1422|[Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/)|[maximum-score-after-splitting-a-string.py](./Python/maximum-score-after-splitting-a-string.py)| Easy | |

## Tree

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0094|[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|[binary-tree-inorder-traversal.py](./Python/binary-tree-inorder-traversal.py) | Medium | |
| 0104|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[maximum-depth-of-binary-tree.py](./Python/maximum-depth-of-binary-tree.py)| Easy | |
| 0111|[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[minimum-depth-of-binary-tree.py](./Python/minimum-depth-of-binary-tree.py)| Easy | |
| 0112|[Path Sum](https://leetcode.com/problems/path-sum/)|[path-sum.py](./Python/path-sum.py)| Easy | | 
| 0116|[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|[populating-next-right-pointers-in-each-node.py](./Python/populating-next-right-pointers-in-each-node.py)| Medium | |
| 0144|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|[binary-tree-preorder-traversal.py](./Python/binary-tree-preorder-traversal.py)| Medium | |
| 0145|[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|[binary-tree-postorder-traversal.py](./Python/binary-tree-postorder-traversal.py)| Hard | |
| 0222|[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)|[count-complete-tree-nodes.py](./Python/count-complete-tree-nodes.py)| Medium | |
| 0226|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)|[invert-binary-tree.py](./Python/invert-binary-tree.py)| Easy | |
| 0235|[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)|[lowest-common-ancestor-of-a-binary-search-tree.py](./Python/lowest-common-ancestor-of-a-binary-search-tree.py)| Easy | |
| 0257|[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|[binary-tree-paths.py](./Python/binary-tree-paths.py)| Easy | |
| 0530|[Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/submissions/)|[minimum-absolute-difference-in-bst.py](./Python/minimum-absolute-difference-in-bst.py)| Easy | |
| 0543|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|[diameter-of-binary-tree.py](./Python/diameter-of-binary-tree.py)| Easy | |
| 0559|[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[maximum-depth-of-n-ary-tree.py](./Python/maximum-depth-of-n-ary-tree.py)| Easy | |
| 0606|[Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)|[construct-string-from-binary-tree.py](./Python/construct-string-from-binary-tree.py)| Easy | |
| 0637|[Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)|[average-of-levels-in-binary-tree.py](./Python/average-of-levels-in-binary-tree.py)| Easy | |
| 0653|[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)|[two-sum-iv-input-is-a-bst.py](./Python/two-sum-iv-input-is-a-bst.py)| Easy | |
| 0872|[Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)|[leaf-similar-trees.py](./Python/leaf-similar-trees.py)| Easy | |
| 0897|[Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)|[increasing-order-search-tree.py](./Python/increasing-order-search-tree.py)| Easy | |
| 0958|[Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)|[check-completeness-of-a-binary-tree.py](./Python/check-completeness-of-a-binary-tree.py)| Medium | |
| 0965|[Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)|[univalued-binary-tree.py](./Python/univalued-binary-tree.py)| Easy | |
| 1008|[Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)|[construct-binary-search-tree-from-preorder-traversal.py](./Python/construct-binary-search-tree-from-preorder-traversal.py)| Medium | |
| 1214|[Two Sum BSTs](https://leetcode.com/contest/biweekly-contest-10/problems/two-sum-bsts/)|[two-sum-bsts.py](./Python/two-sum-bsts.py)| Medium | not released yet |
| 1367|[Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/)|[linked-list-in-binary-tree.py](./Python/linked-list-in-binary-tree.py)| Medium | |

## Hash Table

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0001|[Two Sum](https://leetcode.com/problems/two-sum/)|[two-sum.py](./Python/two-sum.py)| Easy | |
| 0049|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|[group-anagrams.py](./Python/group-anagrams.py)| Medium | |
| 0094|[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|[binary-tree-inorder-traversal.py](./Python/binary-tree-inorder-traversal.py) | Medium | |
| 0136|[Single Number](https://leetcode.com/problems/single-number/)|[single-number.py](./Python/single-number.py) | Easy | |
| 0166|[Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)|[fraction-to-recurring-decimal](./Python/fraction-to-recurring-decimal.py)| Medium | |
| 0202|[Happy Number](https://leetcode.com/problems/happy-number/)|[happy-number.py](./Python/happy-number.py)| Easy | |
| 0217|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|[contains-duplicate.py](./Python/contains-duplicate.py)| Easy | |
| 0219|[Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)|[contains-duplicate-ii.py](./Python/contains-duplicate-ii.py)| Easy | |
| 0242|[Valid Anagram](https://leetcode.com/problems/valid-anagram/)|[valid-anagram.py](./Python/valid-anagram.py)| Easy | |
| 0299|[Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/)|[bulls-and-cows.py](./Python/bulls-and-cows.py)| Easy | |
| 0349|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)|[intersection-of-two-arrays.py](./Python/intersection-of-two-arrays.py)| Easy | |
| 0350|[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)|[intersection-of-two-arrays-ii.py](./Python/intersection-of-two-arrays-ii.py)| Easy | |
| 0387|[First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)|[first-unique-character-in-a-string.py](./Python/first-unique-character-in-a-string.py)| Easy | |
| 0447|[Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/)|[number-of-boomerangs.py](./Python/number-of-boomerangs.py)| Easy | |
| 0451|[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)|[sort-characters-by-frequency.py](./Python/sort-characters-by-frequency.py)| Medium | |
| 0463|[Island Perimeter](https://leetcode.com/problems/island-perimeter/)|[island-perimeter.py](./Python/island-perimeter.py)| Easy | |
| 0525|[Continuous Array](https://leetcode.com/problems/contiguous-array/)|[continuous-array.py](./Python/continuous-array.py)| Medium | |
| 0560|[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)|[subarray-sum-equals-k.py](./Python/subarray-sum-equals-k.py)| Medium | hash table |
| 0599|[Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/)|[minimum-index-sum-of-two-lists.py](./Python/minimum-index-sum-of-two-lists.py)| Easy | |
| 0706|[Design HashMap](https://leetcode.com/problems/design-hashmap/)|[design-hashmap.py](./Python/design-hashmap.py)| Easy | |
| 0748|[Shortest Completing Word](https://leetcode.com/problems/shortest-completing-word/)|[shortest-completing-word.py](./Python/shortest-completing-word.py)| Easy | |
| 0895|[Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)|[maximum-frequency-stack.py](./Python/maximum-frequency-stack.py)| Hard | |
| 0953|[Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)|[verifying-an-alien-dictionary.py](./Python/verifying-an-alien-dictionary.py)| Easy | |
| 0970|[Powerful Integers](https://leetcode.com/problems/powerful-integers/)|[powerful-integers.py](./Python/powerful-integers.py)| Easy | |
| 1002|[Find Common Characters](https://leetcode.com/problems/find-common-characters/)|[find-common-characters.py](./Python/find-common-characters)| Easy | |
| 1072|[Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/)|[flip-columns-for-maximum-number-of-equal-rows.py](./Python/flip-columns-for-maximum-number-of-equal-rows.py)| Medium | |
| 1078|[Occurrences After Bigram](https://leetcode.com/problems/occurrences-after-bigram/)|[occurrences-after-bigram.py](./Python/occurrences-after-bigram.py)| Easy | |
| 1090|[Largest Values From Labels](https://leetcode.com/problems/largest-values-from-labels/)|[largest-values-from-labels.py](./Python/largest-values-from-labels.py)| Medium | |
| 1160|[Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)|[find-words-that-can-be-formed-by-characters.py](./Python/find-words-that-can-be-formed-by-characters.py)| Easy | |
| 1189|[Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)|[maximum-number-of-balloons.py](./Python/maximum-number-of-balloons.py)| Easy | |
| 1207|[Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)|[unique-number-of-occurrences.py](./Python/unique-number-of-occurrences.py)| Easy | |
| 1365|[How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)|[how-many-numbers-are-smaller-than-the-current-number.py](./Python/how-many-numbers-are-smaller-than-the-current-number.py)| Easy | |
| 1418|[Display Table of Food Orders in a Restaurant](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/)|[display-table-of-food-orders-in-a-restaurant.py](./Python/display-table-of-food-orders-in-a-restaurant.py)| Medium | |

## Depth-first Search

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0104|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[maximum-depth-of-binary-tree.py](./Python/maximum-depth-of-binary-tree.py)| Easy | |
| 0111|[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[minimum-depth-of-binary-tree.py](./Python/minimum-depth-of-binary-tree.py)| Easy | |
| 0112|[Path Sum](https://leetcode.com/problems/path-sum/)|[path-sum.py](./Python/path-sum.py)| Easy | |
| 0116|[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|[populating-next-right-pointers-in-each-node.py](./Python/populating-next-right-pointers-in-each-node.py)| Medium | |
| 0257|[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|[binary-tree-paths.py](./Python/binary-tree-paths.py)| Easy | |
| 0559|[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[maximum-depth-of-n-ary-tree.py](./Python/maximum-depth-of-n-ary-tree.py)| Easy | |
| 0638|[Shopping Offers](https://leetcode.com/problems/shopping-offers/)|[shopping-offers.py](./Python/shopping-offers.py)| Medium | |
| 0695|[Max Area of Island](https://leetcode.com/problems/max-area-of-island/)|[max-area-of-island.py](./Python/max-area-of-island.py)| Medium | |
| 0841|[Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)|[keys-and-rooms.py](./Python/keys-and-rooms.py)| Medium | |
| 0872|[Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)|[leaf-similar-trees.py](./Python/leaf-similar-trees.py)| Easy | |
| 0897|[Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)|[increasing-order-search-tree.py](./Python/increasing-order-search-tree.py)| Easy | |
| 0980|[Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)|[unique-paths-iii.py](./Python/unique-paths-iii.py)| Hard | |
| 1020|[Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)|[number-of-enclaves.py](./Python/number-of-enclaves.py)| Medium | |
| 1391|[Check if There is a Valid Path in a Grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/)|[check-of-there-is-a-valid-path-in-a-grid.py](./Python/check-if-there-is-a-valid-path-in-a-grid.py)| Medium | |

## Binary Search

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0033|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|[search-in-rotated-sorted-array.py](./Python/search-in-rotated-sorted-array.py)| Medium | |
| 0034|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)|[find-first-and-last-position-of-element-in-sorted-array.py]| Medium | |
| 0069|[Sqrt(x)](https://leetcode.com/problems/sqrtx/)|[sqrtx.py](./Python/sqrtx.py)| Easy | |
| 0035|[Search Insert Position](https://leetcode.com/problems/search-insert-position/)|[search-insert-position.py](./Python/search-insert-position.py)| Easy | |
| 0162|[Find Peak Element](https://leetcode.com/problems/find-peak-element/)|[find-peak-element](./Python/find-peak-element.py)| Medium | |
| 0167|[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|[two-sum-ii-input-array-is-sorted.py](./Python/two-sum-ii-input-array-is-sorted.py)| Easy | |
| 0222|[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)|[count-complete-tree-nodes.py](./Python/count-complete-tree-nodes.py)| Medium | |
| 0278|[First Bad Version](https://leetcode.com/problems/first-bad-version/)|[first-bad-version.py](./Python/first-bad-version.py)| Easy | |
| 0287|[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)|[find-the-duplicate-number.py](./Python/find-the-duplicate-number.py)| Medium | |
| 0349|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)|[intersection-of-two-arrays.py](./Python/intersection-of-two-arrays.py)| Easy | |
| 0350|[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)|[intersection-of-two-arrays-ii.py](./Python/intersection-of-two-arrays-ii.py)| Easy | |
| 0367|[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)|[valid-perfect-square.py](./Python/valid-perfect-square.py)| Easy | |
| 0374|[Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)|[guess-number-higher-or-lower.py](./Python/guess-number-higher-or-lower.py)| Easy | |
| 0392|[Is Subsequence](https://leetcode.com/problems/is-subsequence/)|[is-subsequence.py](./Python/is-subsequence.py)| Easy | |
| 0441|[Arranging Coins](https://leetcode.com/problems/arranging-coins/)|[arranging-coins.py](./Python/arranging-coins.py)| Easy | |
| 0704|[Binary Search](https://leetcode.com/problems/binary-search/)|[binary-search.py](./Python/binary-search.py)| Easy | |
| 0744|[Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)|[find-smallest-letter-greater-than-target.py](./Python/find-smallest-letter-greater-than-target.py)| Easy | |
| 1201|[Ugly Number III](https://leetcode.com/problems/ugly-number-iii/)|[ugly-number-iii.py](./Python/ugly-number-iii.py)| Medium | |
| 1283|[Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)|[find-the-smallest-divisor-given-a-threshold.py](./Python/find-the-smallest-divisor-given-a-threshold.py)| Medium | |
| 1292|[Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)|[maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold](./Python/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold.py)| Medium | |
| 1351|[Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)|[count-negative-numbers-in-a-sorted-matrix.py](./Python/count-negative-numbers-in-a-sorted-matrix.py)| Easy | |

## Greedy

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0055|[Jump Game](https://leetcode.com/problems/jump-game/)|[jump-game.py](./Python/jump-game.py)| Medium | |
| 0122|[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)|[best-time-to-buy-and-sell-stock-ii.py](./Python/best-time-to-buy-and-sell-stock-ii.py)| Easy | |
| 0392|[Is Subsequence](https://leetcode.com/problems/is-subsequence/)|[is-subsequence.py](./Python/is-subsequence.py)| Easy | |
| 0402|[Remove K Digits](https://leetcode.com/problems/remove-k-digits/)|[remove-k-digits.py](./Python/remove-k-digits.py)| Medium | |
| 0860|[Lemonade Change](https://leetcode.com/problems/lemonade-change/)|[lemonade-change.py](./Python/lemonade-change.py)| Easy | |
| 0861|[Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/)|[score-after-flipping-matrix.py](./Python/score-after-flipping-matrix.py)| Medium | |
| 0881|[Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)|[boats-to-save-people.py](./Python/boats-to-save-people.py)| Medium | |
| 0910|[Smallest Range II](https://leetcode.com/problems/smallest-range-ii/)|[smallest-range-ii.py](./Python/smallest-range-ii.py)| Medium | |
| 0921|[Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)|[minimum-add-to-make-parenthess-valid.py](./Python/minimum-add-to-make-parentheses-valid.py)| Medium | |
| 0944|[Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)|[delete-columns-to-make-sorted.py](./Python/delete-columns-to-make-sorted.py)| Easy | [zip](./notes/zip.md) |
| 1005|[Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)|[maximize-sum-of-array-after-k-negations.py](./Python/maximize-sum-of-array-after-k-negations.py)| Easy | |
| 1029|[Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)|[two-city-scheduling.py](./Python/two-city-scheduling.py)| Easy | |
| 1046|[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)|[last-stone-weight.py](./Python/last-stone-weight.py)| Easy | |
| 1090|[Largest Values From Labels](https://leetcode.com/problems/largest-values-from-labels/)|[largest-values-from-labels.py](./Python/largest-values-from-labels.py)| Medium | |
| 1217|[Play with Chips](https://leetcode.com/problems/play-with-chips/)|[play-with-chips.py](./Python/play-with-chips.py)| Easy | |
| 1247|[Minimum Swaps to Make Strings Equal](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/)|[minimum-swaps-to-make-strings-equal.py](./Python/minimum-swaps-to-make-strings-equal.py)| Medium | |
| 1282|[Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/)|[group-the-people-given-the-group-size-they-belong-to.py](./Python/group-the-people-given-the-group-size-they-belong-to.py)| Medium | |
| 1296|[Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)|[divide-array-in-sets-of-k-consecutive-numbers.py](./Python/divide-array-in-sets-of-k-consecutive-numbers.py)| Medium | |
| 1383|[Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/)|[maximum-performance-of-a-team.py](./Python/maximum-performance-of-a-team.py)| Hard | |
| 1400|[Construct K Palindrome Strings](https://leetcode.com/problems/construct-k-palindrome-strings/)|[construct-k-palindrome-strings.py](./Python/construct-k-palindrome-strings.py)| Medium | |
| 1403|[Minimum Subsequence in Non-Increasing Order](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/)|[minimum-subsequence-in-non-increasing-order.py](./Python/minimum-subsequence-in-non-increasing-order.py)| Easy | |
| 1405|[Longest Happy String](https://leetcode.com/problems/longest-happy-string/)|[longest-happy-string.py](./Python/longest-happy-string.py)| Medium | |
| 1414|[Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)|[find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k.py](./Python/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k.py)| Medium | |

## Two Pointers

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0019|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[remove-nth-node-from-end-of-list.py](./Python/remove-nth-node-from-end-of-list.py)| Medium | |
| 0026|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|[remove-duplicates-from-sorted-array.py](./Python/remove-duplicates-from-sorted-array.py)| Easy | |
| 0027|[Remove Element](https://leetcode.com/problems/remove-element/)|[remove-element.py](./Python/remove-element.py)| Easy | |
| 0028|[Implement strStr()](https://leetcode.com/problems/implement-strstr/)|[implement-strstr.py](./Python/implement-strstr.py)| Easy | |
| 0075|[Sort Colors](https://leetcode.com/problems/sort-colors/)|[sort-colors.py](./Python/sort-colors.py)| Medium | |
| 0080|[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)|[remove-duplicates-from-sorted-array-ii.py](./Python/remove-duplicates-from-sorted-array-ii.py)| Medium | |
| 0088|[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)|[merge-sorted-array.py](./Python/merge-sorted-array.py)| Easy | |
| 0125|[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|[valid-palindrome.py](./Python/valid-palindrome.py)| Easy | |
| 0141|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|[linked-list-cycle.py](./Python/linked-list-cycle.py)| Easy | |
| 0167|[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)|[two-sum-ii-input-array-is-sorted.py](./Python/two-sum-ii-input-array-is-sorted.py)| Easy | |
| 0234|[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)|[palindrome-linked-list.py](./Python/palindrome-linked-list.py)| Easy | |
| 0283|[Move Zeroes](https://leetcode.com/problems/move-zeroes/)|[move-zeroes.py](./Python/move-zeroes.py)| Easy | |
| 0287|[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)|[find-the-duplicate-number.py](./Python/find-the-duplicate-number.py)| Medium | |
| 0344|[Reverse String](https://leetcode.com/problems/reverse-string/)|[reverse-string.py](./Python/reverse-string.py)| Easy | |
| 0345|[Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)|[reverse-vowels-of-a-string.py](./Python/reverse-vowels-of-a-string.py)| Easy | |
| 0349|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)|[intersection-of-two-arrays.py](./Python/intersection-of-two-arrays.py)| Easy | |
| 0350|[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)|[intersection-of-two-arrays-ii.py](./Python/intersection-of-two-arrays-ii.py)| Easy | |
| 0457|[Circular Array Loop](https://leetcode.com/problems/circular-array-loop/)|[circular-array-loop.py](./Python/circular-array-loop.py)| Medium | |
| 0532|[K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)|[k-diff-pairs-in-an-array.py](./Python/k-diff-pairs-in-an-array.py)| Easy | |
| 0844|[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)|[backspace-string-compare.py](./Python/backspace-string-compare.py)| Easy | |
| 0845|[Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/)|[longest-mountain-in-array.py](./Python/longest-mountain-in-array.py)| Medium | |
| 0881|[Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)|[boats-to-save-people.py](./Python/boats-to-save-people.py)| Medium | |
| 0925|[Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)|[long-pressed-name.py](./Python/long-pressed-name.py)| Easy | |
| 0977|[Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)|[squares-of-a-sorted-array.py](./Python/squares-of-a-sorted-array.py)| Easy | |
| 1234|[Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)|[replace-the-substring-for-balanced-string.py](./Python/replace-the-substring-for-balanced-string.py)| Medium | |

## Breadth-first Search

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0111|[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[minimum-depth-of-binary-tree.py](./Python/minimum-depth-of-binary-tree.py)| Easy | |
| 0559|[Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[maximum-depth-of-n-ary-tree.py](./Python/maximum-depth-of-n-ary-tree.py)| Easy | |
| 1298|[Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/)|[maximum-candies-you-can-get-from-boxes.py](./Python/maximum-candies-you-can-get-from-boxes.py)| Hard | |
| 1368|[Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)|[minimum-cost-to-make-at-least-one-valid-path-in-a-grid.py](./Python/minimum-cost-to-make-at-least-one-valid-path-in-a-grid.py)| Hard | |
| 1391|[Check if There is a Valid Path in a Grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/)|[check-of-there-is-a-valid-path-in-a-grid.py](./Python/check-if-there-is-a-valid-path-in-a-grid.py)| Medium | |

## Stack

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0094|[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|[binary-tree-inorder-traversal.py](./Python/binary-tree-inorder-traversal.py) | Medium | |
| 0144|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|[binary-tree-preorder-traversal.py](./Python/binary-tree-preorder-traversal.py)| Medium | |
| 0145|[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)|[binary-tree-postorder-traversal.py](./Python/binary-tree-postorder-traversal.py)| Hard | |
| 0155|[Min Stack](https://leetcode.com/problems/min-stack/)|[min-stack.py](./Python/min-stack.py)| Easy | |
| 0402|[Remove K Digits](https://leetcode.com/problems/remove-k-digits/)|[remove-k-digits.py](./Python/remove-k-digits.py)| Medium | |
| 0844|[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)|[backspace-string-compare.py](./Python/backspace-string-compare.py)| Easy | |
| 0895|[Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)|[maximum-frequency-stack.py](./Python/maximum-frequency-stack.py)| Hard | |
| 0921|[Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)|[minimum-add-to-make-parenthess-valid.py](./Python/minimum-add-to-make-parentheses-valid.py)| Medium | |
| 1047|[Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)|[remove-all-adjacent-duplicates-in-string.py](./Python/remove-all-adjacent-duplicates-in-string.py)| Easy | |
| 1190|[Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)|[reverse-substrings-between-each-pair-of-parentheses.py](./Python/reverse-substrings-between-each-pair-of-parentheses.py)| Medium | |
| 1209|[Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)|[remove-all-adjacent-duplicates-in-string-ii.py](./Python/remove-all-adjacent-duplicates-in-string-ii.py)| Medium | |
| 1381|[Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/)|[design-a-stack-with-increment-operation.py](./Python/design-a-stack-with-increment-operation.py)| Medium | |
| 1410|[HTML Entity Parser](https://leetcode.com/problems/html-entity-parser/)|[html-entity-parser.py](./Python/html-entity-parser.py)| Medium | |

## Backtracking

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0093|[Restore IP Address](https://leetcode.com/problems/restore-ip-addresses/)|[restore-ip-address.py](./Python/restore-ip-address.py)| Medium | |
| 0784|[Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)|[letter-case-permutation.py](./Python/letter-case-permutation.py)| Easy | |
| 0980|[Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)|[unique-paths-iii.py](./Python/unique-paths-iii.py)| Hard | |
| 1286|[Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/)|[iterator-for-combination.py](./Python/iterator-for-combination.py)| Medium | |
| 1291|[Sequential Digits](https://leetcode.com/problems/sequential-digits/)|[sequential-digits.py](./Python/sequential-digits.py)| Medium | |
| 1415|[The k-th Lexicographical String of All Happy Strings of Length n](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)|[the-k-th-lexicographical-string-of-all-happy-strings-of-length-n.py](./Python/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n.py)| Medium | |

## Design

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0146|[LRU Cache](https://leetcode.com/problems/lru-cache/)|[lru-cache.py](./Python/lru-cache.py)| Medium | linked list |
| 0155|[Min Stack](https://leetcode.com/problems/min-stack/)|[min-stack.py](./Python/min-stack.py)| Easy | |
| 0706|[Design HashMap](https://leetcode.com/problems/design-hashmap/)|[design-hashmap.py](./Python/design-hashmap.py)| Easy | |
| 0707|[Design Linked List](https://leetcode.com/problems/design-linked-list/)|[design-linked-list.py](./Python/design-linked-list.py)| Easy | |
| 1286|[Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/)|[iterator-for-combination.py](./Python/iterator-for-combination.py)| Medium | |
| 1352|[Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/)|[product-of-the-last-k-numbers.py](./Python/product-of-the-last-k-numbers.py)| Medium | |
| 1357|[Apply Discount Every n Orders](https://leetcode.com/problems/apply-discount-every-n-orders/)|[apply-discount-every-n-orders.py](./Python/apply-discount-every-n-orders.py)| Medium | |
| 1381|[Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/)|[design-a-stack-with-increment-operation.py](./Python/design-a-stack-with-increment-operation.py)| Medium | |
| 1396|[Design Underground System](https://leetcode.com/problems/design-underground-system/)|[design-underground-system.py](./Python/design-underground-system.py)| Medium | |

## Linked List

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0019|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[remove-nth-node-from-end-of-list.py](./Python/remove-nth-node-from-end-of-list.py)| Medium | |
| 0082|[Remove-Duplicates-from-Sorted-List-II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)|[remove-duplicates-from-sorted-list-ii.py](./Python/remove-duplicates-from-sorted-list-ii.py)| Medium | |
| 0141|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|[linked-list-cycle.py](./Python/linked-list-cycle.py)| Easy | |
| 0203|[Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)|[remove-linked-list-elements.py](./Python/remove-linked-list-elements.py)| Easy | |
| 0234|[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)|[palindrome-linked-list.py](./Python/palindrome-linked-list.py)| Easy | |
| 0445|[Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)|[add-two-numbers-ii.py](./Python/add-two-numbers-ii.py)| Medium | |
| 0707|[Design Linked List](https://leetcode.com/problems/design-linked-list/)|[design-linked-list.py](./Python/design-linked-list.py)| Easy | |
| 0876|[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)|[middle-of-the-linked-list.py](./Python/middle-of-the-linked-list.py)| Easy | |
| 1290|[Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)|[convert-binary-number-in-a-linked-list-to-integer.py](./Python/convert-binary-number-in-a-linked-list-to-integer.py)| Easy | |
| 1367|[Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/)|[linked-list-in-binary-tree.py](./Python/linked-list-in-binary-tree.py)| Medium | |

## Graph

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0841|[Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)|[keys-and-rooms.py](./Python/keys-and-rooms.py)| Medium | |
| 0997|[Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)|[find-the-town-judge.py](./Python/find-the-town-judge.py)| Easy | |
| 1267|[Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/)|[count-servers-that-communicate.py](./Python/count-servers-that-communicate.py)| Medium | |

## Sort

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0056|[Merge Intervals](https://leetcode.com/problems/merge-intervals/)|[merge-intervals.py](./Python/merge-intervals.py)| Medium | |
| 0075|[Sort Colors](https://leetcode.com/problems/sort-colors/)|[sort-colors.py](./Python/sort-colors.py)| Medium | |
| 0242|[Valid Anagram](https://leetcode.com/problems/valid-anagram/)|[valid-anagram.py](./Python/valid-anagram.py)| Easy | |
| 0349|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)|[intersection-of-two-arrays.py](./Python/intersection-of-two-arrays.py)| Easy | |
| 0350|[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)|[intersection-of-two-arrays-ii.py](./Python/intersection-of-two-arrays-ii.py)| Easy | |
| 0922|[Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)|[sort-array-by-parity-ii.py](./Python/sort-array-by-parity-ii.py)| Easy | |
| 0969|[Pancake Sorting](https://leetcode.com/problems/pancake-sorting/)|[pancake-sorting.py](./Python/pancake-sorting.py)| Medium | |
| 1122|[Relative Sort Array](https://leetcode.com/problems/relative-sort-array/)|[relative-sort-array.py](./Python/relative-sort-array.py)| Easy | |
| 1356|[Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)|[sort-integers-by-the-number-of-1-bits.py](./Python/sort-integers-by-the-number-of-1-bits.py)| Easy | |
| 1366|[Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)|[rank-teams-by-votes.py](./Python/rank-teams-by-votes.py)| Medium | |
| 1370|[Increasing Decreasing String](https://leetcode.com/problems/increasing-decreasing-string/)|[increasing-decreasing-string.py](./Python/increasing-decreasing-string.py)| Easy | |
| 1383|[Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/)|[maximum-performance-of-a-team.py](./Python/maximum-performance-of-a-team.py)| Hard | |
| 1403|[Minimum Subsequence in Non-Increasing Order](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/)|[minimum-subsequence-in-non-increasing-order.py](./Python/minimum-subsequence-in-non-increasing-order.py)| Easy | |
| 1424|[Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/)|[diagonal-traverse-ii.py](./Python/diagonal-traverese-ii.py)| Medium | |

## Bit Manipulation

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0136|[Single Number](https://leetcode.com/problems/single-number/)|[single-number.py](./Python/single-number.py) | Easy | |
| 0169|[Majority Element](https://leetcode.com/problems/majority-element/)|[majority-element.py](./Python/majority-element.py)| Easy | |
| 0201|[Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)|[bitwise-and-of-numbers-range.py](./Python/bitwise-and-of-numbers-range.py)| Medium | |
| 0268|[Missing Number](https://leetcode.com/problems/missing-number)|[missing-number.py](./Python/missing-number.py)| Easy | |
| 0338|[Counting Bits](https://leetcode.com/problems/counting-bits/)|[counting-bits.py](./Python/counting-bits.py)| Medium | |
| 0762|[Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)|[prime-number-of-set-bits-in-binary-representation.py](./Python/prime-number-of-set-bits-in-binary-representation.py)| Easy | |
| 0784|[Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)|[letter-case-permutation.py](./Python/letter-case-permutation.py)| Easy | |
| 1255|[Maximum Score Words Formed by Letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/)|[maximum-score-words-formed-by-letters.py](./Python/maximum-score-words-formed-by-letters.py)| Hard | |
| 1290|[Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)|[convert-binary-number-in-a-linked-list-to-integer.py](./Python/convert-binary-number-in-a-linked-list-to-integer.py)| Easy | |
| 1297|[Maximum Number of Occurrences of a Substring](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/)|[maximum-number-of-occurrences-of-a-substring.py](./Python/maximum-number-of-occurrences-of-a-substring.py)| Medium | |
| 1356|[Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)|[sort-integers-by-the-number-of-1-bits.py](./Python/sort-integers-by-the-number-of-1-bits.py)| Easy | |
| 1404|[Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)|[number-of-steps-to-reduce-a-number-in-binary-representation-to-one.py](./Python/number-of-steps-to-reduce-a-number-in-binary-representation-to-one.py)| Medium | |

## Heap

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0451|[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)|[sort-characters-by-frequency.py](./Python/sort-characters-by-frequency.py)| Medium | |
| 1046|[Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)|[last-stone-weight.py](./Python/last-stone-weight.py)| Easy | |

## Sliding Window

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 1074|[Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)|[number-of-submatrices-that-sum-to-target.py](./Python/number-of-submatrices-that-sum-to-target.py)| Hard | |
| 1208|[Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/)|[get-equal-substrings-within-budget.py](./Python/get-equal-substrings-within-budget.py)| Medium | |
| 1423|[Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)|[maximum-points-you-can-obtain-from-cards.py](./Python/maximum-points-you-can-obtain-from-cards.py)| Medium | |

## Divide and Conquer

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0053|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[maximum-subarray.py](./Python/maximum-subarray.py)| Easy | |
| 0169|[Majority Element](https://leetcode.com/problems/majority-element/)|[majority-element.py](./Python/majority-element.py)| Easy | |

## Recursion

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 1137|[N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)|[n-th-tribonacci-number.py](./Python/n-th-tribonacci-number.py)| Easy | |

## Ordered Map

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0846|[Hand of Straights](https://leetcode.com/problems/hand-of-straights/)|[hand-of-straights.py](./Python/hand-of-straights.py)| Medium | |

## Brainteaser

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 1033|[Moving Stones Until Consecutive](https://leetcode.com/problems/moving-stones-until-consecutive/)|[moving-stones-until-consecutive.py](./Python/moving-stones-until-consecutive.py)| Easy | |

## Geometry

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0892|[Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/)|[surface-area-of-3d-shapes.py](./Python/surface-area-of-3d-shapes.py)| Easy | |
| 1232|[Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)|[check-if-it-is-a-straight-line.py](./Python/check-if-it-is-a-straight-line.py)| Easy | |
| 1266|[Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)|[minimum-time-visiting-all-points.py](./Python/minimum-time-visiting-all-points.py)| Easy | |
| 1401|[Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/)|[circle-and-rectangle-overlapping.py](./Python/circle-and-rectangle-overlapping.py)| Medium | |

## Line Sweep

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 1272|[Remove Interval](https://leetcode.com/problems/remove-interval/)|[remove-interval.py](./Python/remove-interval.py)| Medium | |
| 1288|[Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)|[remove-covered-intervals.py](./Python/remove-covered-intervals.py)| Medium | |

## Binary Search Tree

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 1038|[Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)|[binary-search-tree-to-greater-sum-tree.py](./Python/binary-search-tree-to-greater-sum-tree.py)| Medium | |
| 1382|[Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/)|[balance-a-binary-search-tree.py](./Python/balance-a-binary-search-tree.py)| Medium | |

## No Category

|  #  | Problem           |  Solution       | Difficulty    | Notes | 
|:---:|:-----------------:|:---------------:|:-------------:|:-----:|
| 0412|[Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)|[fizz-buzz.py](./Python/fizz-buzz.py)| Easy | |
| 0419|[Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/)|[battleships-in-a-board.py](./Python/battleships-in-a-board.py)| Medium | |
| 0482|[License Key Formatting](https://leetcode.com/problems/license-key-formatting/)|[license-key-formatting.py](./Python/license-key-formatting.py)| Easy | string |
| 0540|[Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)|[single-element-in-a-sorted-array.py](./Python/single-element-in-a-sorted-array.py)| Medium | binary search |
