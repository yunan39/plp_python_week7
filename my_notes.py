
with open("my_notes.txt", "w") as f:
    f.write("Python is fun\n")
    
    f.write("Files are useful\n")
    
    f.write("Week 7 is going well\n")

with open("my_notes.txt", "a") as f:
    f.write("I added this later\n")
    
print("--- My notes ---")
with open("my_notes.txt", "r") as f:
    for line in f:

        print(line.strip())

with open("my_notes.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))