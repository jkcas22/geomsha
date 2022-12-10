

import numpy as np


def gen_grid_image(images, grid):
    img_size = len(images[0])
    num_grid = grid[0]*grid[1]

    grid_img = np.zeros((1+(img_size+1)*grid[0],1+(img_size+1)*grid[1]))
    grid_pos = []
    for i, img in enumerate(images[:num_grid]):
        x = i//grid[1]
        y = i%grid[1]
        grid_pos.append((x,y))
        grid_img[1+(img_size+1)*x:1+(img_size+1)*x+img_size,1+(img_size+1)*y:1+(img_size+1)*y+img_size] = img
    return (grid_img, grid_pos)