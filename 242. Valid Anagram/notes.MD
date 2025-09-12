Started this off by just using the sorted method - sorted(s) == sorted(t)

Wanted to make my time complexity smaller since sorted has a O(nlogn) so decided to use a frequency table to check if the number of letters in each list are the same ASSUMING the lengths are the same. If the frequency table is the same, we know that the two strings are anagrams.
