# pip 安装第三方库使用示例

## 安装第三方库

确保已安装好Python。打开终端，键入如下命令以安装`requests`库：

```bash
pip install requests
```

可以通过逻辑等于符号（`==`）指定版本。例如，通过如下命令安装`2.0.1`版本的`xlrd`库：

```bash
pip install xlrd==2.0.1
```

## 卸载第三方库

通过如下命令卸载`xlrd`库：

```bash
pip uninstall xlrd
```

## 查看已安装的库

通过如下命令查看已安装的库：

```bash
pip list
```

## 安装文件中的所有库

若将所需安装的第三方库卸载文件`requirements.txt`中（每一行是一个库的名称），例如：

```
numpy
scipy
matplotlib
jupyter
```

则可以通过如下命令安装文件`requirements.txt`中的所有库：

```bash
pip install -r requirements.txt
```



