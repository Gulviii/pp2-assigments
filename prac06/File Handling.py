with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Gulvira!\nThis is sample data.\n")


# Файлды оқу
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

#copy_delete_files.py
import shutil, os

# Файлға қосымша жазу
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("New line appended.\n")

# Көшіру және резерв жасау
shutil.copy("sample.txt", "backup.txt")

# Қауіпсіз жою
if os.path.exists("backup.txt"):
    os.remove("backup.txt")