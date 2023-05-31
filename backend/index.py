import rarfile

file = rarfile.RarFile("D:\\3000 and 600 words Anki.rar")
rarfile.RarFile.extractall(file)
