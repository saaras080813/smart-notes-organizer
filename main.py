# ================================
# SMART NOTES ORGANIZER
# ================================

# ---------- SETUP (given to you) ----------
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample file 'class-notes.txt' created.")


# ---------- PART 1: read(40) ----------
print("\nPART 1: Preview with read(40)")
file = open("class-notes.txt", "r")
print(file.read(40))
file.close()


# ---------- PART 2: readlines() ----------
print("\nPART 2: readlines()")
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

print(f"Total lines in file: {len(lines)}")
for index, line in enumerate(lines, start=1):
    print(f"{index} -> {line.strip()}")


# ---------- PART 3: loop line by line ----------
print("\nPART 3: Loop line by line")
file = open("class-notes.txt", "r")
for line in file:
    print(f"Reading: {line.strip()}")
file.close()


# ---------- PART 4: filter with a condition ----------
print("\nPART 4: Filter with a condition")
kept_count = 0
skipped_count = 0

file = open("class-notes.txt", "r")
for line in file:
    clean_line = line.strip()
    if clean_line.startswith("SKIP"):
        print(f"Skipped: {clean_line}")
        skipped_count += 1
    else:
        print(f"Kept: {clean_line}")
        kept_count += 1
file.close()

print(f"Kept {kept_count} lines and skipped {skipped_count} lines.")


# ---------- PART 5: copy selected lines ----------
print("\nPART 5: Copy selected lines to a new file")
source_file = open("class-notes.txt", "r")
all_lines = source_file.readlines()
source_file.close()

dest_file = open("organized-notes.txt", "w")
copied_count = 0

for line in all_lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        dest_file.write(line)
        copied_count += 1

dest_file.close()
print(f"Copied {copied_count} lines into 'organized-notes.txt'.")


# ---------- PART 6: show the result ----------
print("\nPART 6: Organized notes")
organized_file = open("organized-notes.txt", "r")
for line in organized_file:
    print(line.strip())
organized_file.close()
