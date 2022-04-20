# 将本地环境部署到离线环境中

1. 进入外网python虚拟环境

2. 导入虚拟环境中已安装包的信息到requirements.txt 文件中

   pip freeze --all >requirements.txt



4. 创建一个临时目录，将安装包下载到该目录下

   1. mkdir whls
   2. cd whls
   3. pip download -r ../requirements.txt -d .

5. 将创建好的虚拟环境打包，拷贝到新的环境中

6. 解压，激活该虚拟环境

7. 将whls 目录拷贝解压到新环境的目录下

8. 执行安装命令安装

   pip install --no-index --find-links=whls -r requirements.txt

