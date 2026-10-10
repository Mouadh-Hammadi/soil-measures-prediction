# Crop Prediction Using Soil Data

## About

This project explores how soil measurements can help predict which crop is best suited for a particular field.

The dataset contains nitrogen (N), phosphorus (P), potassium (K) and pH measurements, along with the crop considered most suitable for those conditions.

The goal is to build a classification model and find out which single soil measurement is the most useful for predicting the crop.

## What I did

- Checked the dataset for missing values.
- Split the data into training and testing sets.
- Trained Logistic Regression models using one soil feature at a time.
- Compared the models using the weighted F1-score.
- Identified the feature with the best predictive performance.

## Tools

- Python
- Pandas
- Scikit-learn

## Dataset

The project uses `soil_measures.csv`, with the following columns:

| Column | Description |
|---|---|
| `N` | Nitrogen content in the soil |
| `P` | Phosphorus content in the soil |
| `K` | Potassium content in the soil |
| `ph` | Soil pH value |
| `crop` | Target crop to predict |

## How to run

1. Clone this repository.
2. Make sure `soil_measures.csv` is in the same directory as the notebook or Python script.
3. Install the required libraries:

   ```bash
   pip install pandas scikit-learn
   ```

4. Run the notebook or Python script.

## What I learned

This project gave me some practical experience with supervised learning, multiclass classification and model evaluation. It also helped me understand how to compare individual features instead of assuming that every input variable contributes equally to a prediction.

## Credits

This project was completed as part of my DataCamp learning path.
