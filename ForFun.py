import numpy as np
import random
def closest(arr, num):
    idx = (np.abs(arr-num)).argmin()
    return arr[idx]

def check_arrays(arr1, arr2):
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    return np_arr1 == np_arr2

mass = np.array([random.random()*100 for i in range(100)])
print(mass)
print(closest(mass, 40))
arr1 = [
   None,
   "Marvel",
   "2.0.17",
   {
       "name": "Hulk",
       "color": "green",
       "age": 31,
       "abilities": ["crash", "smash"]
   },
   {
       "name": "Iron Man",
       "age": 35,
       "stillAlive": True
   },
   ["Captain America", "Thor", "Captain Marvel"]
]

arr2 = [
   None,
   "Marvel",
   "2.0.17",
   {
       "name": "Hulk",
       "color": "green",
       "age": 31,
       "abilities": ["crash", "smash"]
   },
   {
       "name": "Iron Man",
       "age": 35,
       "stillAlive": True
   },
   ["Captain America", "Thor", "Captain Marvel"]
]

print(check_arrays(arr1, arr2))
