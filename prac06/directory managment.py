#create_list_dirs
import os

# Кірістірілген каталогтар жасау
os.makedirs("nested/dir/example", exist_ok=True)
# Файлдар мен папкаларды шығару
for root, dirs, files in os.walk("."):
    print("Root:", root)
    print("Dirs:", dirs)
    print("Files:", files)

#move_files
import shutil

# Файлдарды кеңейтуі бойынша табу
import glob
txt_files = glob.glob("*.txt")
print("TXT files:", txt_files)

# Файлды басқа каталогқа көшіру
shutil.move("sample.txt", "nested/sample.txt")