from pathlib import Path


def rename_files(directory, mode, text='', target='', replacement=''):
    """ 重命名一个文件夹内所有文件

    功能：
    - 在文件名的头部添加文本
    - 在文件名的尾部添加文本（不改变扩展名）
    - 替换文件名中的文本
    - 重命名为序列化文件名
    """
    path = Path(directory)

    if mode == 'serize':
        for idx, file_path in enumerate(path.iterdir()):
            if file_path.is_file():
                new_name = text + f"_{idx}" + file_path.suffix

                new_path = file_path.with_name(new_name)
                file_path.rename(new_path)
                

    for file_path in path.iterdir():
        if file_path.is_file():
            new_name = file_path.name

            if mode == 'prefix':
                new_name = text + file_path.name
            elif mode == 'suffix':
                new_name = file_path.stem + text + file_path.suffix
            elif mode == 'replace':
                new_name = file_path.name.replace(target, replacement)


            new_path = file_path.with_name(new_name)
            file_path.rename(new_path)


def main():
    print("欢迎使用批量重命名工具！请选择以下操作：")
    print("1. 在文件名前增加前缀")
    print("2. 在文件名后增加后缀（不改变后缀）")
    print("3. 替换文件名中的部分内容")
    print("4. 重命名为序列化文件名")

    choice = input("请输入操作编号（1/2/3/4）：")

    if choice not in {'1', '2', '3', '4'}:
        print("错误：无效选择，程序退出。")
        return

    directory = input("请输入文件所在的目录路径：")
    if not Path(directory).exists():
        print("错误：路径不存在！")
        return
    if not Path(directory).is_dir():
        print("错误：路径不是文件夹！")
        return
    if choice == '1':
        text = input("请输入要添加的前缀：")
        rename_files(directory, mode='prefix', text=text)
    elif choice == '2':
        text = input("请输入要添加的后缀：")
        rename_files(directory, mode='suffix', text=text)
    elif choice == '3':
        target = input("请输入要替换的内容：")
        if not target:
            print("错误：待替换内容不能为空！")
            return
        replacement = input("请输入替换后的内容：")
        rename_files(directory, mode='replace', target=target, replacement=replacement)
    elif choice == '4':
        text = input("请输入要序列化的文件名：")
        if not text:
            print("错误：输入不能为空！")
            return
        rename_files(directory, mode='serize', text=text)

if __name__ == "__main__":
    main()