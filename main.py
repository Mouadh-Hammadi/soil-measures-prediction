import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

crops = pd.read_csv("soil_measures.csv")
print(crops.isna().sum().sort_values())
crops_dummies=pd.get_dummies(crops)
print(crops_dummies.columns)
X=crops.drop("crop", axis=1)
y=crops["crop"]
X_train, X_test , y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)
features_dict={'N':None ,'P':None, 'K':None , 'ph':None}
feature_names=['N','P','K','ph']
for feature in feature_names:
    log=LogisticRegression()
    X1=X_train[feature].values
    X1=X1.reshape(-1,1)
    X2=X_test[feature].values
    X2=X2.reshape(-1,1)
    log.fit(X1,y_train)
    y_pred=log.predict(X2)
    features_dict[feature]=metrics.f1_score(y_test,y_pred,average='weighted')
    
best_key, max_val = max(features_dict.items(), key=lambda x: x[1])
best_predictive_feature={best_key: max_val}

print(best_predictive_feature)
