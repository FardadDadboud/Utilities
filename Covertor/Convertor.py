import cv2
import glob
import os

# loc = '/Users/fardad/Desktop/data/labels/'
#
# for i in range(6*60*30,9*60*30+900):
#     f = open(loc + 'frame_'+'{:0>6}'.format(i)+'.txt', 'w')
#     f.write('')
#     f.close()


vidDir = 'test.avi'
labelDir = '/labels/'
targetDir = '/target/'

if len(glob.glob(targetDir+'train.txt')) > 0:
    os.remove(targetDir+'train.txt')
tmpList = glob.glob(targetDir+'labels/*.txt')
if len(tmpList) > 0:
    for i, k in enumerate(tmpList):
        os.remove(k)

vidName = vidDir[vidDir.rfind('/')+1:vidDir.rfind('.')]

cap = cv2.VideoCapture(vidDir)
cFrame = -1
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cFrame += 1
        f = open(targetDir+'train.txt', 'a')
        f.write('target/labels/frame_' + '{:0>6}'.format(cFrame)+'.txt\n')
        f.close()
        if len(glob.glob(labelDir+vidName+'_'+str(cFrame+1)+'.txt'))>0:
            f = open(labelDir+vidName+'_'+str(cFrame+1)+'.txt', "r")
            text = f.readlines()
            f.close()
            for i, k in enumerate(text):
                cont = k.split()
                f = open('target/labels/frame_' + '{:0>6}'.format(cFrame)+'.txt', "a")
                for j, z in enumerate(cont[0:5]):
                    f.write(z+' ')
                f.write('\n')
                f.close()
        else:
            f = open('target/labels/frame_'+'{:0>6}'.format(cFrame)+'.txt', "w")
            f.close()
    else:
        break

cap.release()
