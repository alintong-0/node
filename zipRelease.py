import shutil
 
# 函数
shutil.make_archive('./release', 'zip', './out/Release/')
 
# 注释
# zipfile_path = 'E:\YQ_HLW'        打包后保存的文件路径及名称
# 'zip' ： 打包后的文件格式，也可为tar等
# Date_file ='E:\DataFile1'   被打包的文件夹名称
