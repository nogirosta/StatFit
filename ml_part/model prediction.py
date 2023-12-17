import joblib
import pandas as pd

def predict_label(classifier_filename, scaler_filename, pure_input_data):
    # Load the model
    loaded_classifier = joblib.load(classifier_filename)

    # Load the scaler
    loaded_scaler = joblib.load(scaler_filename)

    # Use the scaler to transform new data
    input_data = pd.DataFrame(loaded_scaler.transform(pure_input_data), columns=pure_input_data.columns)

    output_data = loaded_classifier.predict(input_data)[0]

    loaded_classifier_prediction = pure_input_data
    loaded_classifier_prediction[classifier_filename.split("_")[0]] = output_data
    
    return loaded_classifier_prediction

FitnessGroup_classification_filename = "FitnessGroup_xgboost_classifier.joblib"
IntensityGroup_classification_filename = "IntensityGroup_knn_classifier.joblib"
scaler_filename = "scaler_classification.joblib"

pure_input_data = pd.DataFrame({
    "Calories": [1797], 
    "Steps": [10735], 
    "TotalMinutesAsleep": [384.0]
})

label_prediction = predict_label(
    FitnessGroup_classification_filename,
    scaler_filename,
    pure_input_data
)

print(label_prediction)