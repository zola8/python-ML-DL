import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# uncertain zone width = size^(-3/4) or size ** (-3/4)
# fill_percent 59.27 + uncertain zone width

size = 100
# threshold 59.27
fill_percent = 59.27
animation_delay = 1

total_cells = size * size
num_people = round(total_cells * fill_percent / 100)
grid = np.zeros((size, size), dtype=int)  # no person

positions = np.random.choice(total_cells, size=num_people, replace=False)
grid.flat[positions] = 1  # healthy

start = np.random.choice(positions)
start_row, start_col = divmod(start, size)
grid[start_row, start_col] = 2  # infected

frontier = [(start_row, start_col)]

frames = [grid.copy()]


def update(frame_index):
    frame = frames[frame_index]
    img.set_data(frame)
    infected_count_ = np.sum(frame == 2)
    title.set_text(f'Fill: {fill_percent}% | People: {num_people} | Infected: {infected_count_}')
    return img, title


if __name__ == '__main__':
    while frontier:
        new_frontier = []

        for row, col in frontier:
            neighbors = [
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col),
            ]

            for neighbor_row, neighbor_col in neighbors:
                if 0 <= neighbor_row < size and 0 <= neighbor_col < size:
                    if grid[neighbor_row, neighbor_col] == 1:
                        grid[neighbor_row, neighbor_col] = 2
                        new_frontier.append((neighbor_row, neighbor_col))

        frontier = new_frontier

        if frontier:
            frames.append(grid.copy())

    fig, ax = plt.subplots(figsize=(8, 8))
    img = ax.imshow(frames[0], interpolation='nearest', vmin=0, vmax=2)
    ax.axis('off')
    title = ax.set_title(f'Fill: {fill_percent}% | People: {num_people} | Infected: 1')

    animation = FuncAnimation(
        fig,
        update,
        frames=len(frames),
        interval=animation_delay,
        blit=False,
        repeat=False
    )

    plt.show()

