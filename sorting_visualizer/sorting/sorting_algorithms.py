from . import algorithms
from .algorithms import *
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import rc
from IPython.display import HTML

#User input to create list of numbers to be sorted and choose sorting algorithm

#algo = int(input("Choose algorithm:\n  1.Bubble \n 2.Insertion \n 3.Quick \n 4.Selection \n 5.Merge Sort \n"))
# algo = algorithm
# print(algo)
def random_array(n=0):
    if n < 1:
        n = random.randint(15, 100)
        n = 40
    array = [i + 1 for i in range(n)]
    color_array = [0 for j in range(n)]
    random.shuffle(array)
    return array, color_array, n




def bubble(n=0):
    array, color_array, n = random_array(n)
    
    title = "Bubble Sort"
    print("Bubble Sort")
    algorithm = bubble_sort(array, color_array)
    play(array, color_array, algorithm, title, n)

def insertion(n=0):
    array, color_array, n = random_array(n)
    title = "Insertion Sort"
    print("Insertion Sort")
    algorithm = insertion_sort(array, color_array)
    play(array, color_array, algorithm, title, n)

def quick(n=0):
    array, color_array, n = random_array(n)
    title = "Quick Sort"
    print("Quick Sort")
    algorithm = quick_sort(array,0,n-1, color_array)
    play(array, color_array, algorithm, title, n)

# elif(algo==4):
#     title="Selection Sort"
    
#     algorithm = selection_sort(array)

def merge(n=0):
    array, color_array, n = random_array(n)
    title = "Merge Sort"
    print("Merge Sort")
    algorithm = merge_sort(array,0,n-1, color_array)
    play(array, color_array, algorithm, title, n)

def play(array, color_array, algorithm, title, n):
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rec = ax.bar(range(len(array)), array, align='edge', width=0.7)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    epochs = [0]

    def update_plot(array, rec, epochs, color_array):
        for rec, val, color in zip(rec, array, color_array):
            rec.set_height(val)
            if color == 1:
                rec.set_color('r')
            else:
                rec.set_color('b')
        epochs[0]+= 1
        text.set_text("No.of operations :{}".format(epochs[0]))


    if n > 65:
        interval = 35
    else:
        interval = 75
    animation = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs, color_array), frames=algorithm, interval=interval, repeat=False,save_count=15000)
    # animation.to_html5_video()
    # return animation.to_html5_video()
    # # display(fig)
    # # # animation.save('animation.mp4', writer='imagemagick')
    # # plt.show()

    with open("C:/Users/theos/Documents/Resume Projects/Sorting Visualizer/sorting_visualizer/sorting/templates/myvideo.html", "w") as f:
        print(animation.to_html5_video(), file=f)

