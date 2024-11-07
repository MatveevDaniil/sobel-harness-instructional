import re
import matplotlib.pyplot as plt

flop = (7112 - 2) * (5146 - 2) * (9 + 9 + 2 + 1 + 1) / 10 ** 9
runtimes = []
for T in [1, 2, 4, 8, 16]:
  with open(f'build/results/sobel-cpu-{T}') as f:
    output = f.read()
    match = re.search(r"Elapsed time is : ([\d.]+)", output)
    if match:
      runtime = float(match.group(1))
  runtimes.append(flop / runtime)

plt.scatter([1, 2, 4, 8, 16], runtimes)
plt.plot([1, 2, 4, 8, 16], runtimes, label='GFLOPs(T threads)')
plt.xlabel("Number of threads")
plt.ylabel("Theoretical GFLOPs")
plt.title("Sobel Performance VS Number of Threads")
plt.axhline(y=8 * runtimes[0], color='r', linestyle='--', label='GFLOPs(1 thread) * 8')
plt.axhline(y=16 * runtimes[0], color='g', linestyle='--', label='GFLOPs(1 thread) * 16')
plt.legend()
plt.savefig('scripts/img/sobel_cpu_time.png', dpi=300)