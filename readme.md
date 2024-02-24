# GitHub Action 使用示例



## 打包Python程序

1. .github\workflows 下新增文件或者修改文件，实现基于Pyinstaller在不同操作系统打包, 具体参照仓库内的三个样例文件

2. 仓库中的 sdk/ 工具包为自定义的一些工具包
3. start.py 运行需要.env文件支持（.env 中有密钥，仓库内不提供具体数值）

3. 可以打包test.py文件测试

4. 有新的依赖包，加到requirements.txt中
5. 触发actions功能的是 .github\workflows 下的文件



