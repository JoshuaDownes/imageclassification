pca = RandomizedPCA(n_components=5)
train_x = pca.fit_transform(train_x)
test_x = pca.transform(fit_x)

print train_x[:5]

knn = KNeighborsClassifier()
knn.fit(train_x, train_y)

