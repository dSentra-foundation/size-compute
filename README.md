# Size Compute
### Motivation
This can be used to compute the allocated memory of N instances of a defined class. 

Sometimes we need to know how to structure our data inside a class (or multiple classes). One of the questions when thinking about this problem is the overhead created by composing/splitting classes.

This is a util that computes the total memory allocation of N instances of a class.

### What
There are two files here:
- `main.py` this will to the computation
- `my_class.py` in this file we define all the members of the instance we want to measure

### How
`main.py` instantiates `num_instances` of `my_class` and outputs the result to the terminal.

In order to run multiple computations we should organize ourselves in a workflow that is not destructive for previous/future test cases.

### Proposed workflow
We should use the main branch as an immutable starting point for all our computations.

When we need to create another computation case:
- we branch from `main`
- we give the branch a obvious name eg.: `calculate-size-of-validators-merged`
- we edit the `my_class.py` file, fill in all the required data and stubs
- we run main with `python main.py`

We should never merge back to main, let's keep things separated.


