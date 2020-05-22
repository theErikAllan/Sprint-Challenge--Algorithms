#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0                     # O(1)
   while (a < n * n * n):    # O(n^3)
       a = a + n * n         # O(n^2)

## Setting a variable takes the same amount of time no matter how large the variable is, so a = 0 has a constant O(1) runtime. The next line has a runtime complexity of O(n^3) because the number of times the while loop runs depends on the cube of the input n. On the last line we are making a single calculation of (c + n * n) which can be simplified to (c + n^2). If this is pseudocode, n could represent an array, in which case the runtime complexity of O(n^2) is the worst case. If this was not pseudocode, the last line would be a single calculation regardless of how large n becomes, making it O(1). However, we are looking for worst case, so O(n^2) is my final answer. Overall, because O(n^3) is the worst case, O(n^3) is the overall runtime complexity. 

b) sum = 0              # O(1)
   for i in range(n):   # O(n)
       j = 1            # O(1)
       while j < n:     # O(n)
           j *= 2       # O(1)
           sum += 1     # O(1)

## Most of this snippet has a runtime complexity of O(1) because all lines except the second and fourth will not change as the input grows in size. Lines 2 and 4 have a runtime complexity of O(n) because the number of loops/operations performed will increase as the size of n increases. Lastly, since the while loop is nested in the for loop, we can multiply the two O(n) runtime values together and get a final runtime complexity of O(n^2).

c) def bunnyEars(bunnies):                  # O(1)
       if bunnies == 0:                     # O(1)
           return 0                         # O(1)

       return 2 + bunnyEars(bunnies-1)      # O(n)

## In this case, the first three lines have a constant runtime complexity of O(1) because the number of operations to be performed does not depend on the size of the input. The last line has a linear runtime complexity of O(n-1) which can be reduced to O(n) as the number of recursions grows linearly with the size of the input bunnies.




## Exercise II