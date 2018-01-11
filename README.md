# random-sampling

## Description
This python function random_sampling helps users to draw from a given sample randomly with replacement and without replacement.

## Inputs
|    | Inputs         | Type | Description                                                                                                                                                                                              |
|----|----------------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | sample         | List | A non-empty list of samples for random drawing.                                                                                                                                                          |
| 2. | size           | Int  | Number of elements drawn from sample.  If is_replacement is True, then size can be greater than the length of sample. If is_replacement is False, then size cannot be greater than the length of sample. |
| 3. | is_replacement | Bool | If is_replacement is True, then the function draws with replacement. Otherwise, the function draws without replacement.                                                                                  |

## Returns
|    | Type | Description                                                                        |
|----|------|------------------------------------------------------------------------------------|
| 1. | List | A list contain drawn elements.  If size is 0, the function returns an empty list.  |

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
