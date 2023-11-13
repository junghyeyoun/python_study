# 배포
import joblib
import pandas as pd

mymodel = joblib.load('linear06_ex2m.model')

# 예측 2 : 새로운 'Price', 'Advertising', 'Age', 'Income' 값으로 Sales를 추정
x_new2 = pd.DataFrame({'Price':[200.0,250.0, 170.0], 'Advertising':[11, 15, 13],
                       'Age':[33, 44, 39], 'Income':[65.0, 72.0, 70.0]})
new_pred2 = mymodel.predict(x_new2)
print('Sales 추정값 : ', new_pred2.values)
# Sales 추정값 :  [4.14940819 1.30801688 5.86970866]
