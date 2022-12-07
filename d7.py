cmds = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

class Folder:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.path + ' ' + str(self.files)
        self.size = 0
        self.directories = []
        self.visited = False
    def __str__(self):
        return self.path + ' ' + str(self.files)
 
path = ''
cmds = cmds.splitlines()
pointer = 0

folders = {'/':Folder('/')}

while pointer < len(cmds):
    cmd = cmds[pointer].split()
    # Handle path
    if cmd[0] == '$' and cmd[1] == 'cd':
        if cmd[2] == '/':
            path = '/'
        elif cmd[2] == '..':
            temp = path.split('/')[1:-2]
            temp = '/'.join(temp)
            path = '/'+ temp
        else:
            path += cmd[2] + '/'

        pointer += 1
    if cmd[0] == '$' and cmd[1] == 'ls':
        pointer += 1
        while pointer < len(cmds) and cmds[pointer][0] != '$' :
            # print(path, cmds[pointer])
            line = cmds[pointer].split()
            
            # work on directories
            if line[0] == 'dir':
                new_folder_path = path + line[1] + '/'
                if new_folder_path not in folders.keys():
                    folders[new_folder_path] = Folder(new_folder_path)
                folders[path].directories.append(new_folder_path)
                
                
            
            else:
                # folders[path].files.append((int(line[0]), line[1]))
                folders[path].files.append(int(line[0])) # just file sizes
            pointer += 1
        


keys = folders.keys()

def size(folder):
    if folder.visited:
        return folder.size
    if folder.directories == []:
        folder.size = sum(folder.files)
        folder.visited = True
        return folder.size
    total = 0
    for dir in folder.directories:
        total += size(dir)
    folder.size = total
    folder.visited = True

size('/')
