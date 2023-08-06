import matplotlib.pyplot as plt

def show_img(images, titles, grid, figsize):
    '''
    :param images: array of images
    :param titles: array of titles
    :param grid: tuple grid plot
    :param figsize: tuple size of window
    :return:
    '''

    fig, ax = plt.subplots(grid[0], grid[1], figsize=figsize)
    ax = ax.flatten()
    i = 0
    for a in ax:
        if i < len(images):
            a.imshow(images[i])
            a.set_title(titles[i])
            i += 1
        a.set_xticks([])
        a.set_yticks([])
    plt.show()
