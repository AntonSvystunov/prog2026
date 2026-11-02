import json
from pathlib import Path

sandbox_folder = Path("sandbox")

data = {
    "version": 1,
    "test": True,
    "files": [],
    "root_dir": str(sandbox_folder.absolute())
}

for file_path, dirs, files in sandbox_folder.walk():
    data["files"].extend(files)

# print(data)
print(json.dumps(data, indent=4))

with open("result.json", "w") as f:
    f.write(json.dumps(data, indent=4))

with open("result1.json", "w") as f:
    json.dump(data, f, indent=4)


with open("result.json", "r") as f:
    data_loaded = json.load(f)
    print(data_loaded)

with open("result1.json", "r") as f:
    data_loaded1 = f.read()
    print(json.loads(data_loaded1))