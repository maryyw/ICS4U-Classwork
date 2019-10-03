"""with open("file.txt", 'w') as f:
        f.write("hello\napple\nflabbergasted\ngamma")

with open("file.txt", 'r') as f:
        for line in f:
                print(line.strip())"""

with open("file.txt", 'r') as f:
        for line in f:
                if line.startswith("f"):
                        print(line.strip())
