import os, time

path = r"./"

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if not ".md" in name: continue
        print(name)
        _path = os.path.join(root, name)
        #editTime = time.strptime(os.path.getmtime(_path), "%Y-%m-%d %H:%M:%S")
        editTime = time.localtime(os.path.getmtime(_path))
        editTime = time.strftime("%Y-%m-%d %H:%M:%S", editTime)
        _name = name[:len(name)-3]
        with open(_path, "r+", encoding="utf-8") as f:
            old = f.read()
            f.seek(0)
            f.write("---\n")
            f.write("title: %s\n" %_name)
            f.write("date: %s\n" %editTime)
            f.write("categories:\n")
            f.write("tags:\n")
            f.write("---\n")
            f.write(old)