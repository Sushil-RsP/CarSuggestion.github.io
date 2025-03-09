''' import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline , make_pipeline
from sklearn.tree import DecisionTreeClassifier
import joblib

def train_model():
    # Load the dataset
    data = pd.read_csv(r"C:\Users\LENOVO\Documents\Presentation_mini\car_customers web.csv")

    x = data.drop(["CarModel","Price","Purchased"], axis=1)
    y = data['CarModel']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Categorical and Numerical Columns
    categorical_cols = ['BodyType', 'Manufacturer', 'FuelType', 'DesiredFeatures']
    numerical_cols = ['SafetyRating', 'Budget', 'Age', 'Family Size']

    preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
    ('num', 'passthrough', numerical_cols)
    ])

    model_pipeline = make_pipeline(preprocessor, DecisionTreeClassifier(random_state=42))

    model_pipeline.fit(x_train, y_train)

    return model_pipeline

# Use the trained model to predict car
def predict_car_model(model_pipeline, BodyType, Manufacturer, FuelType, SafetyRating, Budget, DesiredFeatures, Age, FamilySize):
    future_data = {
        'BodyType': [BodyType],
        'Manufacturer': [Manufacturer],
        'FuelType': [FuelType],
        'SafetyRating': [SafetyRating],
        'Budget': [Budget],
        'DesiredFeatures': [DesiredFeatures],
        'Age': [Age],
        'FamilySize': [FamilySize]
    }

    input_df = pd.DataFrame(future_data)
    
    prediction = model_pipeline.predict(input_df)
    return prediction[0]
'''