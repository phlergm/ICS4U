import os
for root, dirs, files in os.walk("/home/humza/Music/DCIM"):
    for file in files:
        if file.endswith(".mp3"):
             print(os.path.join(root, file))
