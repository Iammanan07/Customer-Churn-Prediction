Customer Churn Prediction 📈
Predicting customer attrition with data-driven insights (98% accuracy) Customer churn prediction involves identifying customers who are likely to leave a service. Retaining customers is often far less expensive than acquiring new ones
avaus.com
, so building models to flag at-risk customers is crucial. Churn happens when customers stop using a service and even small increases in churn can significantly harm revenue
medium.com
. In fact, “losing customers is costly for any business”
sagemaker-examples.readthedocs.io
, which motivates our use of ML to identify unhappy customers early and intervene before it’s too late. Our analysis pipeline includes thorough Exploratory Data Analysis (EDA) and modeling. We first explore the data with charts and summary statistics to uncover patterns (as recommended for churn projects
github.com
). After cleaning (handling missing values, encoding categories, balancing classes), we train and compare multiple classification models using cross-validation. Performance is evaluated with metrics like accuracy, precision, recall, and confusion matrices on a hold-out test set. The best-performing model achieves ~98% accuracy, indicating strong predictive power for distinguishing churners from non-churners.
Key Features
Exploratory Data Analysis (EDA): Visualize feature distributions and churn correlations (bar charts, histograms, etc.).
Preprocessing: Clean data by handling missing values, encoding categorical variables (One-Hot or Label Encoding), and addressing class imbalance (e.g. SMOTE or class weighting).
Feature Engineering: Create and select features that improve model performance (e.g. tenure buckets, interaction terms).
Model Training: Implement multiple classifiers (with train/test split or cross-validation) to predict churn.
Evaluation: Use performance metrics (accuracy, precision, recall, F1-score) and confusion matrices to assess models. ROC curves and other plots are generated to visualize results.
Visualization: Present insights with clear plots (churn rate by tenure, feature importance, etc.) and tables.
Machine Learning Models Used
We implement and compare several common ML algorithms (as noted in churn analytics
github.com
), 
including:
Logistic Regression – a baseline linear classifier.
Decision Tree – an interpretable tree-based model.
Random Forest – an ensemble of trees for robust predictions.
Gradient Boosting (XGBoost) – a powerful boosting algorithm for high accuracy.
Support Vector Machine (SVM) – a margin-based classifier.
K-Nearest Neighbors (KNN) – a distance-based algorithm.
[Optional:] Other models (e.g. Naive Bayes, Neural Networks) can also be added.
These cover diverse approaches (linear models, trees, ensembles, etc.) that are widely used in churn prediction
github.com
.
Results and Performance
Our top model achieves around 98% accuracy on the test set, demonstrating strong predictive performance. A classification report and confusion matrix are provided in the notebook, showing high precision and recall for both churn classes. For example, the model correctly labels most churners and non-churners, indicating it is learning meaningful patterns (not just guessing the majority class). Such high accuracy suggests that the pipeline – from EDA through tuning – effectively identifies at-risk customers in this dataset. The analysis includes rich visualizations (see figure above) to illustrate churn patterns and model outcomes. For instance, bar plots of churn rate by tenure or charge buckets reveal how long-term customers behave differently from short-term ones. These charts (as symbolized above) are used alongside metric tables to help stakeholders interpret the results and make data-driven decisions.
Setup Instructions
Clone the repository: git clone https://github.com/Iammanan07/Customer-Churn-Prediction-.git and cd Customer-Churn-Prediction-.
Environment: Use Python 3.x. It’s recommended to create a virtual environment.
Install dependencies: Run pip install -r requirements.txt, or manually install key libraries:
pip install pandas numpy scikit-learn matplotlib seaborn xgboost
Data: Ensure the Telco Customer Churn dataset is available (either by placing the provided CSV in the repo or downloading it from Kaggle).
Running the Notebook
Open the Jupyter notebook file (Customer_Churn_Prediction_EDA_and_Model_98%_ACC.ipynb) in Jupyter Notebook or JupyterLab.
Execute the cells sequentially. This will perform the EDA, preprocessing, training, and evaluation as outlined.
Alternatively, upload the notebook to Google Colab and run it there. All plots and output tables will be generated inline.
Conclusion and Future Work
This project demonstrates an end-to-end workflow for predicting customer churn, achieving ~98% accuracy on the dataset. The results indicate that ML models can reliably flag potential churners, enabling proactive retention strategies. For example, in a telecom setting one could use these predictions to offer incentives to at-risk customers – an approach noted to be “much more cost-effective than losing and reacquiring” customers
sagemaker-examples.readthedocs.io
. Future work could include refining the model (hyperparameter tuning, feature selection), deploying it as a real-time service, or integrating new data sources (like customer feedback). Overall, the notebook provides a clear, reproducible framework for churn prediction that can be extended and integrated into business workflows. Sources: Concepts and approaches are informed by industry best practices and studies in churn analysis
