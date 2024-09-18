import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error


class DataProcessor:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = None
        self.encoded_df = None
        self.normalizer = StandardScaler()

    def load_data(self):
        self.df = pd.read_csv(self.dataset_path)
        print("Data loaded successfully.")

    def encode_and_normalize(self):
        # Encoding categorical columns
        categorical_cols = self.df.select_dtypes(
            include=["object"]).columns.to_list()
        ordinal_encoder = OrdinalEncoder()
        encoded_categorical_cols = ordinal_encoder.fit_transform(
            self.df[categorical_cols])
        encoded_categorical_df = pd.DataFrame(
            encoded_categorical_cols, columns=categorical_cols)

        # Dropping categorical columns from original dataframe and concatenating the encode ones
        numerical_df = self.df.drop(categorical_cols, axis=1)
        self.encoded_df = pd.concat(
            [numerical_df, encoded_categorical_df], axis=1)

        # Normalizing data
        dataset_arr = self.normalizer.fit_transform(self.encoded_df)
        print("Data encoded and normalized successfully. \n")
        return dataset_arr


class ModelTrainer:
    def __init__(self, dataset_arr, model_type="decision_tree", random_state=1, test_size=0.3, shuffle=True):
        self.X = dataset_arr[:, 1:]
        self.Y = dataset_arr[:, 0]
        self.random_state = random_state
        self.test_size = test_size
        self.shuffle = shuffle
        self.model_type = model_type
        self.regressor = self._initialize_model()

    def _initialize_model(self):
        if self.model_type == "decision_tree":
            return DecisionTreeRegressor(random_state=self.random_state)
        elif self.model_type == "random_forest":
            return RandomForestRegressor(random_state=self.random_state)
        elif self.model_type == "adaboost":
            return AdaBoostRegressor(random_state=self.random_state)
        elif self.model_type == "gradient_boost":
            return GradientBoostingRegressor(random_state=self.random_state)
        else:
            raise ValueError("Unknow model type")

    def split_data(self):
        self.X_train, self.X_val, self.Y_train, self.Y_val = train_test_split(
            self.X, self.Y, test_size=self.test_size, random_state=self.random_state, shuffle=self.shuffle)

    def train_model(self):
        self.regressor.fit(self.X_train, self.Y_train)
        print("Model trained successfully.")

    def evaluate_model(self):
        Y_pred = self.regressor.predict(self.X_val)
        MAE = mean_absolute_error(self.Y_val, Y_pred)
        MSE = mean_squared_error(self.Y_val, Y_pred)
        print(f"Evaluation result on validation set for {self.model_type}: ")
        print(f"Mean Absolute Error: {MAE}")
        print(f"Mean Squared Error: {MSE} \n")
        return Y_pred


class Visualizer:
    @staticmethod
    def visualize_result(X_val, Y_val, Y_pred):
        plt.figure()
        plt.scatter(X_val[:20, 0], Y_val[:20], s=20,
                    edgecolors="black", c="green", label="True")
        plt.scatter(X_val[:20, 0], Y_pred[:20], s=20, edgecolors="black",
                    c="darkorange", label="Prediction")
        plt.xlabel("Area")
        plt.ylabel("Price")
        plt.title("Regression Model Result")
        plt.legend()
        plt.show()


# Main execution
if __name__ == "__main__":
    # Data Processing
    dataset_path = "Housing.csv"
    data_processor = DataProcessor(dataset_path)
    data_processor.load_data()
    dataset_arr = data_processor.encode_and_normalize()

    # list of model types to train and evaluate
    model_types = ["decision_tree", "random_forest",
                   "adaboost", "gradient_boost"]

    for model_type in model_types:
        print(f"Training and evaluating model: {model_type}")

        # Model training and Evaluation
        model_trainer = ModelTrainer(dataset_arr, model_type)
        model_trainer.split_data()
        model_trainer.train_model()
        Y_pred = model_trainer.evaluate_model()

        # Visualization
        Visualizer.visualize_result(
            model_trainer.X_val, model_trainer.Y_val, Y_pred)
