import numpy as np
import pandas as pd
import cv2

img = cv2.imread('./images/artwork_atest28.png', 1)

one_dim = img.reshape(-1, 3)
df = pd.DataFrame(one_dim)
df.columns = ['b', 'g', 'r']

print(df.value_counts().head(50))

