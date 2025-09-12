First started with the brute force case by using two for loops and then checking for the values sum if they added up to the target. That had a time complexity of O(n^2).

Then decided to use a hashmap to check for the previous values that have already been seen in the list. We can add that to a dictionary and check if that item has already been seen. Since we know from the problem that a UNIQUE solution exists, we don't care about duplicates since either they are the solutions (3, 3) or if two 3s do exist none of them exist IN the solution.
