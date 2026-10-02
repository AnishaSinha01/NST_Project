from PIL import Image
import os

root = "large_Dataset"

bad = []
total = 0

for base, _, files in os.walk(root):
    for f in files:
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            total += 1
            path = os.path.join(base, f)

            try:
                with Image.open(path) as im:
                    im.verify()
            except Exception as e:
                bad.append((path, str(e)))

print("Total checked:", total)
print("Bad images:", len(bad))

for path, error in bad:
    print(path, "->", error)
