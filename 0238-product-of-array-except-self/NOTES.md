# Notes

## Idea
* Create two array that computes the products of the left and right products of all of the elements before the current index (left products) and after the current index (right products)
* Product of array except self will be the left_products[i-1] * right_products[i+1]

## Complexity
* Time complexity is *O(N)* to create the left and right product arrays
* Space complexity is *O(N)* to store the two product arrays
