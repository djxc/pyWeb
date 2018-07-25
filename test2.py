# -*- coding: utf-8 -*-
import threading
import time
import requests
import PIL.Image as Image

def wirteFile(filename):
    with open(filename, 'w') as f:
        print(filename)
        f.write(filename)


def run(i, j):
    filename = str(i) + '.txt'
    wirteFile(filename)

def run1(n, m):
    print(n)


def wirtePicture():    
    z = '&z=21'
    url = "http://www.google.cn/maps/vt?lyrs=s@803&gl=cn&x="    # 1731111&y=836147&z=21"   
    for y in range(835900, 835908):        
        for x in range(1730000, 1730100):        
            img_url = url + str(x) + '&y=' + str(y) + z
            img = requests.get(img_url) 
            file = 'data1/%s.jpg' %( str(x) + '****' + str(y))
            print(file)
            with open(file,'ab') as f: #存储图片，多媒体文件需要参数b（二进制文件）
                f.write(img.content) #多媒体存储content


def getImg(y_, d):
    getImg1(y_)



def getImg1(y_):
    z = '&z=21'
    url = "http://www.google.cn/maps/vt?lyrs=s@803&gl=cn&x="    # 1731111&y=836147&z=21"   
    y = int(y_) + 835900
    for x in range(1730800, 1731050):   
        img_url = url + str(x) + '&y=' + str(y) + z
        img = requests.get(img_url) 
        file = 'data/%s.jpg' %( str(x) + '****' + str(y))
        print(file)
        with open(file,'ab') as f: #存储图片，多媒体文件需要参数b（二进制文件）
            f.write(img.content) #多媒体存储content



def mutilWirtePicture():    
   for i in range(40):#40
        thread_list = []
        for y in range(0, 5):        
            n = str(y + i * 5)
            if i < 1:
                t = threading.Thread(target=getImg1, args=(n))
            else:
                t = threading.Thread(target=getImg, args=(n, None))
            thread_list.append(t)
        for t in thread_list:
            t.setDaemon(True)
            t.start()
    
        for t in thread_list:
            t.join()
        print("*****************")
        
        


def mutilThread(j):
    print('****************', j)
    thread_list = []
    for i in range(5):
        name = str(i + j * 5)
        t = threading.Thread(target=run, args=(name, name))
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    for t in thread_list:
        t.join()


def oneThread(j):
    for i in range(5):
        name = str(i + j * 5)
        run(name, i)


def image_joint(image_list,opt):#opt= vertical ,horizontal 选择水平显示拼接的图像，或者垂直拼接
    image_num=len(image_list)
    image_size=image_list[0].size
    height=image_size[1]
    width=image_size[0]
    
    if opt=='vertical':
        new_img=Image.new('RGB',(width,image_num*height),255)
    else:
        new_img=Image.new('RGB',(image_num*width,height),255)
    x=y=0
    count=0
    for img in image_list:
        
        new_img.paste(img,(x,y))
        count+=1
        if opt=='horizontal':
            x+=width
        else : y+=height
    return new_img



def mergePicture():
    img_list = []
    for y in range(836100, 836150):             
        imlist = []
        for x in range(1730900, 1730950):     
            file = 'data/%s.jpg' %( str(x) + '****' + str(y))
            print(file)
            img = Image.open(file)       
            imlist.append(img)
        jimg = image_joint(imlist, 'horizontal')        
        img_list.append(jimg)
    limg = image_joint(img_list, 'vertical')   
#    limg.show()
    limg.save('demo31.jpg', 'jpeg')
    
    

def mergePicture1():
    y1 = 836100
    x1 = 1731050
    for m in range(5):
        x_ = 50
        for n in range(4):
            y_ = 50
            img_list = []
            for y in range(y1 + n*y_, y1 + (n+1)*y_):             
                imlist = []
                for x in range(x1 + m*x_, x1 + (m+1)*x_):     
                    file = '../data1/%s.jpg' %( str(x) + '****' + str(y))
    #                print(file)
                    img = Image.open(file)       
                    imlist.append(img)
                jimg = image_joint(imlist, 'horizontal')        
                img_list.append(jimg)
            limg = image_joint(img_list, 'vertical')   
        #    limg.show()
            filename = 'result4/demo%d%d.jpg' %(m, n)
            limg.save(filename, 'jpeg')
            print(filename + " save successfully!")


if __name__ == '__main__':
    start_time = time.time()
#    for i in range(50):
#        mutilThread(i)
#        oneThread(i)
#    wirtePicture()
#    mutilWirtePicture()
    mergePicture1()
   
    print('一共用时：', time.time()-start_time)
