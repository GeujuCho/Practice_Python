from keras.datasets import mnist

(X_train,Y_class_train),(X_test,Y_class_test)=mnist.load_data()
# X:불러온 이미지 데이터/이 이미지에 0~9까지 붙인 이름표를 Y_class로 구분하여 명명
# train:70,000개 중 학습에 사용될 부분 저장
# test: 테스트에 사용될 부분

print("학습셋 이미지 수: %d 개" % (X_train.shape[0]))  #=>케라스의 MNIST데이터에서 학습용과 테스트용으로 미리 구분해 놓음
print("테스트셋 이미지 수: %d 개" % (X_test.shape[0]))

import matplotlib.pyplot as plt
import sys

#이미지 출력
plt.imshow(X_train[0], cmap='Greys') #흑백으로 출력
plt.show()

for x in X_train[0]:
    for i in x:
        sys.stdout.write('%d|t0'%i)
    sys.stdout.write('|n')
