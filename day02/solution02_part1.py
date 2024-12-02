import numpy as np

num_safe = 0

with open("input.txt", 'r', encoding='utf-8') as f:
  levels = []
  for line in f:
    level = [int(i) for i in line.rstrip().split(" ")]
    levels.append(level)

    level = np.array(level)
    level_diffs = np.diff(level)

    if (np.all(level_diffs > 0) or np.all(level_diffs < 0)) and (0 < np.max(np.abs(level_diffs)) <= 3):
      num_safe +=1

print(num_safe)
