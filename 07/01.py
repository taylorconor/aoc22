with open('07/input.txt') as f:
    lines = f.read().splitlines()[1:]

class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name
    name = ""
    size = 0

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files = {}
        if parent is not None:
            self.full_id = parent.full_id + "/" + name
    def file_size(self):
        return sum([f.size for f in self.files.values()])
    full_id = ""

fs = Dir("/", None)
root = fs
for line in lines:
    if line == "$ ls":
        continue
    if line == "$ cd ..":
        if fs.parent is not None:
            fs = fs.parent
        continue
    if line.startswith("$ cd "):
        name = line.split()[-1]
        if name not in fs.dirs:
            continue
        fs = fs.dirs[name]
        continue
    if line.startswith("dir"):
        name = line.split()[-1]
        fs.dirs[name] = Dir(name, fs)
        continue
    size, name = line.split()
    fs.files[name] = File(int(size), name)

size = 0
def add_sizes(root):
    global size
    result = root.file_size() + sum([add_sizes(f) for f in list(root.dirs.values())])
    if result <= 100000:
        size += result
    return result

add_sizes(root)
print("size = " + str(size))