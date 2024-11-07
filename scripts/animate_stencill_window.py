import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

input = np.array([
  [2, 2, 2, 1, 1, 1],
  [2, 2, 2, 1, 1, 1],
  [2, 2, 2, 1, 1, 1],
  [2, 2, 2, 1, 1, 1],
  [2, 2, 2, 1, 1, 1],
  [2, 2, 2, 1, 1, 1]
])

kernel = np.array([
  [1, 0, -1],
  [1, 0, -1],
  [1, 0, -1]
])

input_rows, input_cols = input.shape
kernel_rows, kernel_cols = kernel.shape
output_rows, output_cols = input_rows - kernel_rows + 1, input_cols - kernel_cols + 1

output = np.array([[''] * output_cols for _ in range(output_rows)])

def draw_matrix(matrix, top_left, title, highlight_box=None):
  rows, cols = matrix.shape
  for i in range(rows):
    for j in range(cols):
      x = top_left[0] + j
      y = top_left[1] - i
      ax.add_patch(patches.Rectangle((x, y), 1, -1, 
                                      edgecolor="black", facecolor="whitesmoke"))
      ax.text(x + 0.5, y - 0.5, f"{matrix[i, j]}", 
              ha="center", va="center", fontsize=12)

  if highlight_box:
    x = top_left[0] + highlight_box[1]
    y = top_left[1] - highlight_box[0]
    length = highlight_box[2]
    rect = patches.Rectangle((x, y), length, -length,
                              linewidth=2, edgecolor="blue", facecolor="none")
    ax.add_patch(rect)

  ax.text(top_left[0] + (cols / 2), top_left[1] + 0.5, title, 
          ha="center", va="center", fontsize=12, fontweight="bold")

for i in range(output_rows):
  for j in range(output_cols):
    fig, ax = plt.subplots(figsize=(10, 4))
    output[i][j] = np.sum(np.multiply(input[i:i+3, j:j+3], kernel))

    draw_matrix(input, (0, 0), "Input", [i, j, 3])
    draw_matrix(kernel, (8, -1.5), "Kernel")
    draw_matrix(output, (13, -1), "Output", [i, j, 1])

    ax.text(7, -3.15, "*", fontsize=12, ha="center")
    ax.text(12, -3.1, "=", fontsize=12, ha="center")

    ax.set_xlim(-0.1, 17.1)
    ax.set_ylim(-6.1, 0.1)
    ax.axis('off')
    plt.tight_layout()

    plt.savefig(f"scripts/img/stencil_{i * 4 + j:02}.png", dpi=300)
    plt.close()
