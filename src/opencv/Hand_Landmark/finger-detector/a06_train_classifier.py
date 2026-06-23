import pickle

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    data_dict = pickle.load(open('./data.pickle', 'rb'))

    data = np.asarray(data_dict['data'])
    labels = np.asarray(data_dict['labels'])

    print(data.shape)
    print(labels.shape)
    print(data[:1])
    print(labels[:1])

    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
    # stratify = we have the same proportion in train/test dataset, same % of labels

    model = RandomForestClassifier()

    model.fit(x_train, y_train)

    y_predict = model.predict(x_test)

    score = accuracy_score(y_predict, y_test)

    print('{}% of samples were classified correctly !'.format(score * 100))

    # f = open('model.p', 'wb')
    # pickle.dump({'model': model}, f)
    # f.close()
