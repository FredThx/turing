import matplotlib.pyplot as plt
import keyboard

def sir(x):
    if x%2==0:
        return x//2
    else:
        return 3*x+1


def siracuse(x,n=0, verb = False):
    if verb:
        print(x)
    n +=1
    if x!=1:
        return siracuse(sir(x),n, verb)
    else:
        return n

def store(val, nb_iter, filename = 'siracuse.csv'):
    '''Stock dans un fichier
    '''
    with open(filename, 'a') as file:
        file.write(f"{val};{nb_iter}\n")


if __name__ == '__main__':
    pause = False
    def switch_pause(e):
        global pause
        pause = not pause
    keyboard.on_press_key('space', switch_pause)


    plt.ion()
    i=1
    data=[0]
    while True:
        if pause:
            plt.pause(1)
        else:
            S = siracuse(i)
            data.append(S)
            store(i,S)
            print(f"{i}=>{S}")
            i +=1
            plt.clf()
            plt.plot(data,linestyle = 'None',marker = '.')
            plt.draw()
            plt.pause(0.01)
