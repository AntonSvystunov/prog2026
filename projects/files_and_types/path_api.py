from pathlib import Path
import os

sandbox_folder = Path("sandbox")
sandbox_folder.mkdir(exist_ok=True)

file_path = sandbox_folder / "example.txt"
file_path.write_text("Hello, world!")

print(file_path)

with open(file_path, "r") as f:
    content = f.read()
    print(content)

for file_path, dirs, files in sandbox_folder.walk():
    print(file_path, dirs, files)


for root, dirs, files in os.walk(sandbox_folder):
    print(root, dirs, files)
