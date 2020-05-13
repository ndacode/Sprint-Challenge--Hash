# Merging Two Packages

Given a

package with a weight limit `limit`

and a list `weights` of item weights,

implement a

function `get_indices_of_item_weights`

<!--iterate  -->

finds

<!-- if item 1 + item 2 = `limit` -->

two items
whose sum of weights
equals the weight limit `limit`.

<!-- append item 1 and item 2 to a tuple -->
<!-- return tuple -->

return an instance of an `Answer` tuple

that has the
following form:

```
(zero, one)
```

where
each element represents the
item weights of the
two packages.

<!-- [(it_1,it_2),(it_3,it_4),etc...] -->

\_\*\*The higher valued index

<!-- if it_1 < it_2, it_1 = it_2 and it_2 = it_1 (use a temp variable)> -->

should be placed in the `zeroth` index and
the smaller index
should be placed in the `first` index.

\*\*\_ If such a pair doesn’t exist for the given inputs, your function should return
`None`.

<!-- if it_1 and it_2 are not 'limit' return None -->

<!-- make this happen in a hashtable -->

Your solution should run in linear time.

Example:

````key = [ 4, 6, 10, 15, 16 ]
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21```
        value  = [ 0, 1,  2,  3,  4 ]

<!-- if the output is a tuple of indices, the hash of the input should return those indices, we're hashing the weight values and assigning them to an index -->
<!-- so in our function we're looking to add the value of the index to the next value and then compare to see if they equal 21  -->
````

output: [ 3, 1 ] # since these are the indices of weights 15 and 6 whose sum equals 21

```

## Hints

* A brute-force solution would involve two nested loops, yielding a
  quadratic-runtime solution. How can we use a hash table in order to
  implement a solution with a better runtime?


<!-- should we be storing the divisible by 21 as the key? -->
<!-- I'm not sure but I think we're looking to store what items added sum to 21 -->
* Think about what we can store in the hash table in order to help us to
  solve this problem more efficiently.

* What if we store each weight in the input list as keys?
  What would be
  <!-- maybe a true/false for 'can sum to 21'? -->
  a useful thing to store as the value for each key?

* If we store each weight's list index as its value, we can then check
  <!-- so we get to a sum of 21 by setting 21 as the limit and subtracting each weight from it -->
  <!-- i.e "does the table have an entry for 21-4? If there's no entry in the table for 17, then 4 won't sum to 21 -->
  to see if the hash table contains an entry for `limit - weight`. If it
  <!-- if the table does have an entry for 21 minus the weight, that weight and the weight of the entry which makes it sum to 21 is the tuple we're looking for -->
  does, then we've found the two items whose weights sum up to the
  `limit`!
```
