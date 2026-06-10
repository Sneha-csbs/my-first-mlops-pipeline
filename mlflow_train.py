import mlflow
import mlflow.sklearn
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Set the name of your experiment challenge
mlflow.set_experiment("Iris_Flower_Classifier")

# 2. Tell MLflow to start recording this specific run
with mlflow.start_run():
    
    # Define your parameters
    estimators = 200  # Change this from 150 to 80
    max_depth = 8
    
    # Log parameters directly to MLflow dashboard
    mlflow.log_param("n_estimators", estimators)
    mlflow.log_param("max_depth", max_depth)
    
    # Train the model
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
    
    model = RandomForestClassifier(n_estimators=estimators, max_depth=max_depth)
    model.fit(X_train, y_train)
    
    # Calculate performance metrics
    accuracy = model.score(X_test, y_test)
    
    # Log metrics to MLflow dashboard
    mlflow.log_metric("accuracy", accuracy)
    
    # Save and log the model artifact files directly into MLflow registry
    mlflow.sklearn.log_model(model, "iris_random_forest_model")
    
    print(f"Run completed! Accuracy logged: {accuracy}")