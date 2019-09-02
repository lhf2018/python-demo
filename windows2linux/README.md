#### 本例实现从windows上传文件到linux文件夹

备注
* 源地址为windows系统路径，目标地址为linux文件夹
* 如果目标地址没有该文件则会创建出相应文件，然后再自动写入
* paramiko 和 pycrypto 的版本很重要，新版本的pycrypto会废弃一些旧接口，不能和旧版本的paramiko搭配、不然会出现运行失败，本例 paramiko版本2.4、pycrypto版本2.4
