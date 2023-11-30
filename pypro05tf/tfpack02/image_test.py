import numpy as np
import cv2
import keras
import matplotlib.pyplot as plt

np.random.seed(1)
path = 'myimages'  # myimages 폴더 밑에 cat:이미지 두 개, dog:이미지 두 개 준비

# 이미지를 불러올 때 폴더명에 맞춰서 자동으로 labelling하는 flow_from_directory( ) 함수의 기능을 활용하기 위함.
# ImageDataGenerator 클래스의 몇 가지 클래스 함수들로 이미지 로드, augmentation을 지원한다.

generator = keras.preprocessing.image.ImageDataGenerator(rotation_range=20,
           width_shift_range=0.2, height_shift_range=0.2, rescale=1. / 255)
batch_size = 4  # myimages 폴더에 있는 이미지 4장을 한 번에 읽어들이기 위해 4로 설정
images = []
obj = generator.flow_from_directory(path, target_size=(150, 150), batch_size=batch_size, class_mode='binary')

# class_mode는 어떤 방식으로 폴더명에 따른 labelling을 진행할 수 있는 파라미터dla
# 'binary'로 설정하면 0 or 1로 labelling이 진행된다.   'categorical'
# 아래의 for문에서 obj.next( )를 한 번 호출할 때 마다
# 1) obj는 설정된 경로에서 2) batch_size에 맞춰서
# 3) 이미지를 target_size로 resizing 한 후 4) 폴더명을 기반으로 'binary' 방식에 맞춰 labelling까지 진행해서 이미지를 불러온다.
# 그래서 obj.next( ) 한 번 호출하면 4개의 이미지를 150 x 150 size로 label 정보와 함께 호출한다.

for _ in range(1):  # augmentatoin을 1번 적용
     img, label = obj.next()
     print('label : ', label)
     n_img = len(label)
     base = cv2.cvtColor(img[0], cv2.COLOR_RGB2BGR)  # keras는 RGB, openCV는 BGR라고 변경함.

     for idx in range(n_img - 1):
           img2 = cv2.cvtColor(img[idx + 1], cv2.COLOR_RGB2BGR)
           base = np.hstack((base, img2))
     images.append(base)
 
print(images)
 
for img in images:
     plt.imshow(img)
plt.show()
