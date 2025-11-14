#Assignment 5 (Static Nested Dictionary Explorer Using Only Dictionary)
filesystem = {
    "home": {
        "documents": {
            "notes.txt": "notes data",
            "todo.txt": "todo data"
        },
        "pictures": {
            "img1.jpg": "binary",
            "img2.png": "binary"
        }
    }
}

# Predefined navigation examples (no loops)
current_directory = filesystem["home"]["documents"]

print("File System:", filesystem)
print("Current Directory:", current_directory)