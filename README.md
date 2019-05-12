# Image-Filtering
Simple image filtering app by kirtanp98 and myself
Includes a web-based and standalone version

## Readme
### Standalone Version
1. With all requirements installed, run finalprojq.py
2. Choose a filter then upload your image
3. Choosing a new filter or uploading a new image will generate a new filtered image for you
### Web Version
  http://imagefilterru.azurewebsites.net/

## Requirements
### Standalone Version
EITHER
  Spyder 3.6 or later
OR
  NumPy
  SciPy
  Skimage
  matplotlib
  PIL
All available via pip
### Web Version
  in requirements.txt
  
## Writeup
Passing a function as a value is a newer development that has a lot of uses, especially in making certain types of programs more organized and structured. We see it as a core feature of functional programming, where functions are just lists that can be passed back and forth with ease. Python 3 has this feature built-in, and we used it in a very clear way - image filtering. 

Each filter is a function defined in filters.py, which takes in a numpy image array and modifies it in some way. The functions are put into a dictionary which corresponds to the selection made by the user. The uploaded image is then put through the selected function by passing that function as a value, and it returns the filtered image. 

Since we tried to emulate functional-style programming in Python, there are some similarities and differences. On a surface level, the image functions don’t change any greater state - they take an image as input and output another image - nothing else. However, in order to get UI working properly, extra-functional variables were used, which would absolutely not be possible in a pure functional language. Additionally, loops were used to modify each pixel, although it could easily have been modified to use recursive calls instead. 

In addition to passing functions as values, we used a few more advanced Python features, including NumPy, OpenCV2, skimage, scipy, and matplotlib. Many of these were used in creating specific filters for images. Additionally, list comprehension, which was discussed in the Python section of the class, was used in the parallel processing experiment (although it did not make it to the final version).

One big change in design we should do is abstract out the image functions. They all have the same structure, and rewriting them is tedious. Making a system with easier function creation would not be too difficult with more time.

### Problems:
Runtime
Compared to applications like Gimp and Paint.net, ours runs extremely slow. For example, a black and white filter on an image roughly the size of the chimpanzee image we tested with took roughly half a second on Paint.net, while it took our application 1.6 seconds more or less. There is a lot of optimization to be done, although research suggested that parallel processing is the only real optimization available for image filtering.

UI
The main decision to make was whether we wanted our application to run in browser using Quart or to run as its own standalone application using tkinter. Long processing times on a web app are an issue due to high amounts of possible interference, as well as requiring a server that can handle the heavy lifting. A standalone tkinter app had issues of portability and relatively ugly UI. 
