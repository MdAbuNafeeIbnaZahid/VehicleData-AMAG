# VehicleData-AMAG


# How to run it
Download the repo.
1. You need python3 for running the repo.
2. Download and come to the root folder of the repo.
3. Run `pip install -r requirement.txt`
4. Modify / Write your input function inside the file `./framework/input_function.py`. 
And change the line from `input_function = len_is_69` to `input_function = your_input_function`
5. Run `python3 ./main.py ./path_to_your_data_file`

# How to run unit test

1. Need to run `python -m unittest`  (It's added in gitlab ci as well)

# Assumptions
## 1.

It's written that filter just takes an input function. For example it takes length, which returns an int. 
```
def length(trajectory):
  return len(trajectory)

list_of_lats_lngs = obj.filter(length)
```
But we have assumed that our input function needs to return a boolean. 
If it is true, then `Segment` actually included in filter. 
Otherwise `Segment` is filtered out.
So it's like:
```
def length_is_5(trajectory):
  return len(trajectory) == 5

list_of_segments = obj.filter(length_is_5)
```
## 2
It's written that the plot also needs to have the ability to plot only filtered
segments.
 ```
list_of_lats_lngs = obj.filter()
# Plots and shows only the list of segments we filtered
obj.plot(list_of_lats_lngs)
```
But it didn't show any function being passed to filter. Also output of filter should be a list of `Segment`. 
So it should be 
```
list_segment = obj.filter()
# Plots and shows only the list of segments we filtered
obj.plot(list_segments)
```



