# VehicleData-AMAG

# Assumptions
1. It's written that filter just takes an input function. For example length, which returns an int. 
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
2. It's written that the plot also needs to have the ability to plot only filtered
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


# How to run it


