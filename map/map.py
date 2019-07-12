from PIL import Image
from pylab import *
import csv



"""计算结果"""
def tik():
    """找到第一个点"""
    x1 = check()
    for i in x1:
        print(i[0])
    print('输入经度：')
    pos1=[]
    pos1.append(float(input()))
    print('输入纬度：')
    pos1.append(float(input()))
    """找到第二个点"""
    x2=check()
    print('输入经度：')
    pos2 = []
    pos2.append(float(input()))
    print('输入纬度：')
    pos2.append(float(input()))
    print(pos1)
    # 横坐标和经度的比例
    scale1=(pos1[0]-pos2[0])/(float(x1[0][0])-float(x2[0][0]))
    # 纵坐标和纬度的比例
    scale2=(pos1[1]-pos2[1])/(float(x1[0][1])-float(x2[0][1]))

    time.sleep(1)

    # 要解析的图片的位置
    im = array(Image.open('D:\\images\\a.jpg'))
    imshow(im)
    print('请点击点坐标，最多100个，按回车提前结束点击')
    y = ginput(100, timeout=-1)

    # 要写入的文件的位置
    out = open('D:\\result.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    # 输出当前时间
    csv_write.writerow(str(time.strftime("%Y%m%d%H:%M:%S", time.localtime())))
    for i in y:
        result=[]
        result.append(float(pos1[0])+scale1*(float(i[0])-float(x1[0][0])))
        result.append(float(pos1[1])+scale2*(float(i[1])-float(x1[0][1])))
        # 要写入的文件的位置
        out = open('D:\\result.csv', 'a', newline='')
        csv_write = csv.writer(out, dialect='excel')
        csv_write.writerow(result)
        print('you clicked:', result)
        # show()

"""确定两个点的坐标和经纬度"""
def check():
    im = array(Image.open('D:\\images\\a.jpg'))
    imshow(im)
    x = ginput(1)
    print('you clicked:', x)
    return x


if __name__ == "__main__":
    tik()
