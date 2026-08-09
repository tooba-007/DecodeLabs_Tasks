# Project 2 – Data Classification Using AI
**DecodeLabs AI Industrial Training Kit**

## What this project does
This project trains a simple **Decision Tree** classifier to predict the
**status of an e-commerce order** (`Shipped`, `Cancelled`, `Returned`,
`Delivered`, or `Pending`) using basic order details such as quantity,
price, payment method, and referral source.

## Dataset
`Dataset_for_Data_Analytics_-_Sheet1.csv` — 1200 e-commerce orders with
columns like `Quantity`, `UnitPrice`, `PaymentMethod`, `ItemsInCart`,
`ReferralSource`, `TotalPrice`, and the target column `OrderStatus`.

## Steps followed (matches the project requirements)
1. **Load and understand the dataset** — read the CSV with pandas, inspect
   shape, columns, and class distribution.
2. **Split data into training and testing sets** — 80% train / 20% test
   using `train_test_split`.
3. **Apply a simple classification algorithm** — `DecisionTreeClassifier`
   from scikit-learn.
4. Evaluate the model with accuracy and a classification report, then
   predict the status of one brand-new sample order.

## How to run
```bash
pip install pandas scikit-learn
python classification.py
```

## Notes
- Text columns (`PaymentMethod`, `ReferralSource`, `OrderStatus`) are
  converted to numbers with `LabelEncoder`, since ML models only work
  with numeric input.
- Accuracy on this dataset is low because the order status here doesn't
  strongly depend on the chosen features (the data is fairly random).
  That's expected and okay — the goal of this project is to correctly
  build the pipeline (load → split → train → evaluate), not to hit a
  perfect score. Feel free to experiment with other features or
  algorithms (e.g. `RandomForestClassifier`, `LogisticRegression`) to see
  if you can improve it.
