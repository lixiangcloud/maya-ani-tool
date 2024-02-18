import os
import maya.cmds as cmds

def close_window():
    if cmds.window(window, exists=True):
       cmds.deleteUI(window, window=True)

def get_file_list(folder_path):
    files = []
    ma_files = cmds.getFileList(folder=folder_path, filespec='*.ma')
    mb_files = cmds.getFileList(folder=folder_path, filespec='*.mb')
    files.extend(ma_files)
    files.extend(mb_files)
    return files

def update_file_list(file_list):
    cmds.textScrollList("myControlObj", e=True, removeAll=True)
    cmds.textScrollList("myControlObj", e=True, append=file_list, uniqueTag=file_list)

def get_filename(*args):
    close_window()
    current_path = cmds.file(q=True, sn=True)
    folder_path = os.path.dirname(current_path)
    file_list = get_file_list(folder_path)
    update_file_list(file_list)

def open_file(*args):
    file_name = cmds.textScrollList("myControlObj", query=True, selectUniqueTagItem=True)
    if file_name:
        file_path = os.path.join(filepathname, file_name[0])
        cmds.file(file_path, force=True, open=True, prompt=False)

def update_file_list_by_path(*args):
    path = cmds.textField(textpath, query=True, text=True)
    file_list = get_file_list(path)
    update_file_list(file_list)
 
 
close_window()

window = cmds.window(title="文件管理 by 李祥", resizeToFitChildren=True, sizeable=True, minimizeButton=False, maximizeButton=False)
cmds.columnLayout()
row_layout = cmds.rowLayout(numberOfColumns=3, columnAttach=(1, 'left', 0), columnWidth=[(1, 25), (3, 100), (3, 50)])
cmds.text(label='路径')
textpath = cmds.textField()
cmds.button(label='确认', command=update_file_list_by_path)
cmds.setParent('..')
cmds.button(label='读取文件', command=get_filename)
cmds.textScrollList("myControlObj", numberOfRows=15, allowMultiSelection=True, width=175,dcc=open_file)
cmds.button(label='打开文件', command=open_file)
cmds.showWindow(window)
