
# write to
with open('writing_files.txt', 'w') as file:  # context manager
    file.write("Hello friend")

# append
with open('writing_files.txt', 'a') as file:  # context manager
    file.write("\n\tHello friend 2")
