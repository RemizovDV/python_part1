import easy_lib as easy 
dirs = ['dir_' + str(n) for n in range(1, 10)]
for cur_dir in dirs:
    easy.MakeDirectory(cur_dir)
for cur_dir in dirs:
    easy.DeleteDirectory(cur_dir)