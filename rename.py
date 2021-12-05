import glob
import os
import re

files = glob.glob("./files_dir/*")

for f in files:
    filename = os.path.basename(f)
    replaced = re.sub(r"-min.png", ".png", filename)
    os.rename("./files_dir/" + filename, "./files_dir/" + replaced)
