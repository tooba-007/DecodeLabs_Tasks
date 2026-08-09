
# Steps:
# 1. Load and understand the dataset
# 2. Split data into training and testing sets
# 3. Apply a simple classification algorithm (Decision Tree)
# 4. Check how accurate the model is

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# STEP 1: Load and understand the dataset
df = pd.read_csv("Dataset_for_Data_Analytics_-_Sheet1.csv")

print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset shape (rows, columns):", df.shape)
print("\nColumn names:", list(df.columns))
print("\nWhat we are predicting -> OrderStatus")
print(df["OrderStatus"].value_counts())

# STEP 2: Pick the features (inputs) and the target (output)
# We keep it simple: only use a few easy-to-understand columns.
# Target (what we want to predict): OrderStatus
# Features (clues the model uses to predict): Quantity, UnitPrice,
# ItemsInCart, TotalPrice, PaymentMethod, ReferralSource

features = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice",
            "PaymentMethod", "ReferralSource"]
target = "OrderStatus"

data = df[features + [target]].copy()

# converting to labels
encoders = {}
for col in ["PaymentMethod", "ReferralSource", target]:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le  # save it, in case we want to decode predictions later

X = data[features]      # inputs
y = data[target]        # output we want to predict

# STEP 3: Split data into training and testing sets
# 80% train, 20% testt
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# STEP 4: Apply a simple classification algorithm
# Decision Tree is one of the simplest and most beginner-friendly
# classification algorithms. It works like a flowchart of yes/no
# questions that leads to a final prediction.
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# STEP 5: Test the model and check accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed performance report:")
print(classification_report(
    y_test, predictions, target_names=encoders[target].classes_
))

# STEP 6: Try predicting a brand new order
# Example new order: Quantity=3, UnitPrice=200, ItemsInCart=5,
# TotalPrice=600, PaymentMethod="Credit Card", ReferralSource="Email"
new_order = pd.DataFrame([{
    "Quantity": 3,
    "UnitPrice": 200,
    "ItemsInCart": 5,
    "TotalPrice": 600,
    "PaymentMethod": encoders["PaymentMethod"].transform(["Credit Card"])[0],
    "ReferralSource": encoders["ReferralSource"].transform(["Email"])[0],
}])

predicted_status = model.predict(new_order)
predicted_label = encoders[target].inverse_transform(predicted_status)
print(f"\nPrediction for a new sample order -> {predicted_label[0]}")
