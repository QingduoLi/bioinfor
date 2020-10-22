import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import os
from sklearn.decomposition import PCA
import imageio

df = sns.load_dataset('iris')

my_dpi = 96
plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)

# Keep the 'specie' column appart + make it numeric for coloring
df['species'] = pd.Categorical(df['species'])
my_color = df['species'].cat.codes
df = df.drop('species', 1)

# Run The PCA
pca = PCA(n_components=3)
pca.fit(df)

# Store results of PCA in a data frame
result = pd.DataFrame(pca.transform(df), columns=['PCA%i' % i for i in range(3)], index=df.index)

# 20 plots, for 20 different angles
for angle in range(70, 210, 2):
    # Plot initialisation
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(result['PCA0'], result['PCA1'], result['PCA2'], c=my_color, cmap="Set2_r", s=60)

    # make simple, bare axis lines through space:
    xAxisLine = ((min(result['PCA0']), max(result['PCA0'])), (0, 0), (0, 0))
    ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')
    yAxisLine = ((0, 0), (min(result['PCA1']), max(result['PCA1'])), (0, 0))
    ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')
    zAxisLine = ((0, 0), (0, 0), (min(result['PCA2']), max(result['PCA2'])))
    ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r')

    ax.view_init(30, angle)

    # label the axes
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")
    ax.set_title("PCA Iris Dataset")
    filename = 'PCA/PCA_angle' + str(angle) + '.png'
    plt.savefig(filename, dpi=96)


def make_gif(input_folder, save_filepath):
    episode_frames = []
    time_per_step = 0.25
    for root, _, files in os.walk(input_folder):
        file_paths = [os.path.join(root, file) for file in files]
        # sorted by modified time
        file_paths = sorted(file_paths, key=lambda x: os.path.getmtime(x))
        episode_frames = [imageio.imread(file_path)
                          for file_path in file_paths if file_path.endswith('.png')]
    episode_frames = np.array(episode_frames)
    imageio.mimsave(save_filepath, episode_frames, duration=time_per_step)


make_gif('./PCA/', './PCA/PCA.gif')