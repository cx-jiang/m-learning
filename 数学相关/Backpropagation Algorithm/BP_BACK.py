import numpy as np


def BP_BACK(training_example, eta):
    '''
    输入变量：  
    training_example:待训练的数据  
    eta： 学习速率  
    '''
    m, n = np.shape(training_example)
    sigma = np.zeros(n)

    #初始化权值矩阵-0.5~0.5之间
    np.random.seed(1)
    w = np.random.rand(2, 3) - 0.5
    v = np.random.rand(3, 2) - 0.5
    u = np.random.rand(2, 3) - 0.5
    for num in range(n):
        #按列取样本
        one_sample = training_example[:, num]
        #提取其中的输入
        x = one_sample[:3]
        #提取其中的输出
        y = one_sample[3:]
        #第一层求和值
        net2 = w * x
        hidden1 = np.zeros(len(w))
        for i in range(len(w)):
            #进行sigmoid处理输出
            hidden1[i] = 1 / (1 + np.exp(-sum(net2[i])))
        #print(hidden1)
        #第二层求和值
        net3 = v * hidden1.T
        hidden2 = np.zeros(len(v))
        for i in range(len(v)):
            #进行sigmoid处理输出
            hidden2[i] = 1 / (1 + np.exp(-sum(net3[i])))
        #print(hidden2)
        #第三层求和值,即输出层
        net4 = u * hidden2.T
        o = np.zeros(len(u))
        for i in range(len(u)):
            #进行sigmoid处理输出
            o[i] = 1 / (1 + np.exp(-sum(net4[i])))
        #print(o)
        #-------------反向传播算法，计算各层delta值（误差E对各层权值的导数）-----------------
        #最后一层delta值
        delta3 = np.zeros(len(u))
        for i in range(len(u)):
            delta3[i] = (y[i] - o[i]) * o[i] * (1 - o[i])
        #print(delta3)
        #第二个隐含层
        delta2 = np.zeros(len(v))
        for j in range(len(v)):
            delta2[j] = np.dot((hidden2[j] *
                                (1 - hidden2[j])) * delta3.reshape(1, 2),
                               u[:, j].reshape(2, 1))[0][0]
        #print(delta2)
        #第一个隐含层
        delta1 = np.zeros(len(w))
        for k in range(len(w)):
            #计算公式，与其后一层的delta值相关
            delta1[k] = np.dot((hidden1[k] *
                                (1 - hidden1[k])) * delta2.reshape(1, 3),
                               v[:, k].reshape(3, 1))[0][0]
        #print(delta1)

        #--------各层delta计算完后开始更新权值---------------------
        #计算公式  w = w + eta*delta*x
        #---更新u权值-----
        for i in range(len(u)):
            for j in range(len(v)):
                u[i][j] = u[i][j] + eta * delta3[i] * hidden2[j]
        #print(u)
        #---更新v权值-----
        for i in range(len(v)):
            for j in range(len(w)):
                v[i][j] = v[i][j] + eta * delta2[i] * hidden1[j]
        #print(v)
        #---更新w权值-----
        for i in range(len(w)):
            for j in range(len(x)):
                w[i][j] = w[i][j] + eta * delta1[i] * x[j]
        #print(w)

        #--------------记录一下这个过程后的误差值
        e = (o - y).reshape(2, 1)
        sigma[num] = np.dot(e.T, e)[0][0]

    return sigma