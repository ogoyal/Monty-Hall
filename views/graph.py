
import matplotlib.pyplot as plt

def plot_prob(x,y1,y2,trials):

    #plt.title(title)
    plt.xlabel('Trials')
    plt.ylabel('Probability')

    plt.axis([0, trials, 0, 1])
    plt.grid(True)

    plt.plot(x, y1, 'r-o')
    plt.plot(x, y2, 'b-o')

    plt.show()


