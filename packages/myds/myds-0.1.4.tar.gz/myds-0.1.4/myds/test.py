import myds
url = "myds://ml.category.cifar10:/../mnist"

q=myds.HttpQuerier()
print(q.getQueryUrl(url))
print(myds.HttpQuerier().query(url))
print(myds.simpleQuery('ml.category.cifar10'))