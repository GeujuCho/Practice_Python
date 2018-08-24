# seed값 생성
np.random.seed(0)
tf.set_random_seed(0)
learning_rate=0.1
# seed값을 설정한다는 것은 그 랜덤 테이블 중에서 몇 번째 테이블을 불어와 쓸지를 정하는 것
#텐서플로 기반으로 딥러닝을 구현할 때는 일정한 결과 값을 얻기 위해 넘파이 seed값과 텐서플로 seed값을 모두 설정해줘야 한다.

# 데이터 로드
dataset=np.loadtxt("../bigdata/pima-indians-diabetes.csv", delimiter=",")
X_data=dataset[:,0:8]
Y_data=dataset[:,[8]]
print(X_data.shape)
print(Y_data.shape)

X_data=np.array(X_data, dtype=np.float32)
Y_data=np.array(Y_data, dtype=np.float32)

X=tf.placeholder(tf.float32, [768 ,8])
Y=tf.placeholder(tf.float32, [768,1])
print(X.shape)
print(Y.shape)

W1=tf.Variable(tf.random_normal([8,12]),name='weight1')
b1=tf.Variable(tf.random_normal([12]),name='bias1')
# layer1=tf.sigmoid(tf.matmul(X,W1)+b1)
layer1=tf.nn.relu(tf.matmul(X,W1)+b1)

W2=tf.Variable(tf.random_normal([12,8]),name='weight2')
b2=tf.Variable(tf.random_normal([8]),name='bias2')
layer2=tf.sigmoid(tf.matmul(layer1,W2)+b2)
# layer2=tf.nn.relu(tf.matmul(layer1,W2)+b2)

W3=tf.Variable(tf.random_normal([8,1]),name='weight2')
b3=tf.Variable(tf.random_normal([1]),name='bias2')
hypothesis=tf.sigmoid(tf.matmul(layer2,W3)+b3)
hypothesis.shape

cost=-tf.reduce_mean(Y*tf.log(hypothesis)+(1-Y)*tf.log(1-hypothesis))
train=tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)
predicted=tf.cast(hypothesis>0.5, dtype=tf.float32)
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted, Y),dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(1001):
        sess.run(train, feed_dict={X:X_data, Y:Y_data})
        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X:X_data, Y:Y_data}), sess.run([W1,W2,W3]))
    h,c, a=sess.run([hypothesis,predicted,accuracy],feed_dict={X:X_data, Y:Y_data})
    print("\nHypothesis: ",h,"\nCorredct: ",c,"\nAccuracy: ",a)