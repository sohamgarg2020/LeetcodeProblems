I really liked this problem.

Originally started with using a defaultdict and then appending the values to it. After that sorted the dictionary using lambda x: x[1], reverse=True to get all the values in reverse order making it from highest-> lowest.

Was talking to a friend and he introduced me to bucket sort so decided to read more about it and wrote this solution. Really really nice. It creates n+1 buckets and then you just append the value in the bucket corresponding to the frequency of the value. Then you just read from the highest bucket to the lowest bucket and append that value in a new list.
