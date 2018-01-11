# random-sampling

## Description
This python function random_sampling helps users to draw from a given sample randomly with replacement and without replacement.

## Inputs

## Returns

## Examples
### Example 1: Random Sampling with Replacement
```python
from random_sampling import random_sampling

lst = ['A','B', 'C', 'D']
a = random_sampling(lst,3)
print(a)
```
The output (one of the possible outputs) is
```
['D', 'D', 'C']
```

### Example 2: Random Sampling without Replacement
```python
from random_sampling import random_sampling

lst = ['A','B', 'C', 'D']
a = random_sampling(sample=lst,size=3,is_replacement)
print(a)
```
The output (one of the possible outputs) is
```
['D', 'B', 'A']
```
