import joblib
import random

import pandas as pd


def predict_label(pure_input_data,
                  classifier_filename="ml_part/FitnessGroup_xgboost_classifier.joblib",
                  scaler_filename="ml_part\scaler_classification.joblib",
                  intensity_group_filename="ml_part\IntensityGroup_knn_classifier.joblib"
                  ):

	loaded_classifier = joblib.load(classifier_filename)

	# Load the scaler
	loaded_scaler = joblib.load(scaler_filename)

	intensity_group = joblib.load(intensity_group_filename)

	# Recommendations (challenges) for each laziness group
	recommendations = {
		(0, 0): [
			"Light Walks: Start with 10-minute leisurely walks, 3 days a week."
		],
		(0, 1): [
			"Evening Unwind: Spend 30 minutes before bed doing a relaxing activity."
		],
		(1, 0): [
			"Moderate Walks: Increase to 20-minute walks, 4 days a week."
		],
		(1, 1): [
			"Bedtime Yoga: 15 minutes of gentle yoga or stretching before bed."
		],
		(2, 0): [
			"Interval Training: Engage in 30-minute sessions, 3 times a week."
		],
		(2, 1): [
			"Mindful Meditation: 10 minutes before bed to relax the mind."
		],
		(3, 0): [
			"High-Intensity Training: 45-minute workouts, 4 times a week."
		],
		(3, 1): [
			"Sleep Restriction Therapy: Follow a strict sleep schedule."
		],
	}

	# Iterate over each row in the input data
	for index, row in pure_input_data.iterrows():
		# Scale the row
		data = pd.DataFrame([row.values], columns=pure_input_data.columns)

		scaled_row = loaded_scaler.transform(data)

		input_data = pd.DataFrame(scaled_row, columns=pure_input_data.columns)

		# Predict the output for the scaled row
		fitness_group_predicted = loaded_classifier.predict(input_data)[0]

		intensity_group_predicted = intensity_group.predict(input_data)[0]

		# Select two random challenges for the predicted group
		selected_challenges = random.sample(recommendations[(fitness_group_predicted, intensity_group_predicted)], 1)

		fitnees_group_scores = {0: 1, 2: 2, 3: 3, 1: 4}

		return (fitnees_group_scores[int(fitness_group_predicted)],
		          selected_challenges)
	return 1, "GO"
