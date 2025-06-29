# Iris Flower Classification Model

A machine learning project that predicts the species of iris flowers using the classic Iris dataset. This project includes model training, evaluation, and a user-friendly web interface built with Streamlit.

## 🌸 Project Overview

This project implements a Random Forest classifier to predict iris flower species based on physical characteristics:
- **Sepal Length**
- **Sepal Width** 
- **Petal Length**
- **Petal Width**

The model classifies flowers into three species:
- **Iris Setosa**
- **Iris Versicolour**
- **Iris Virginica**

## 📁 Project Structure

```
Iris/
├── Iris.ipynb          # Jupyter notebook with model training and evaluation
├── Website.py          # Streamlit web application
├── iris_model.pkl      # Trained Random Forest model (serialized)
├── iris_columns.pkl    # Feature column names (serialized)
└── Readme.md          # Project documentation
```

## 🚀 Features

- **Model Training**: Random Forest classifier with sklearn
- **Model Persistence**: Serialized model using joblib
- **Web Interface**: Interactive Streamlit app for predictions
- **Performance Metrics**: Accuracy, classification report, and confusion matrix
- **Easy Deployment**: Ready-to-run web application

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Iris
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pandas scikit-learn joblib numpy matplotlib seaborn
   ```

## 📊 Usage

### Running the Jupyter Notebook
Open and run `Iris.ipynb` to:
- Load and explore the Iris dataset
- Train the Random Forest model
- Evaluate model performance
- Save the trained model

### Running the Web Application
Launch the Streamlit app:
```bash
streamlit run Website.py
```

The web interface will open in your browser where you can:
1. Enter flower measurements (sepal/petal length and width)
2. Click "Predict" to get the species classification
3. View the predicted iris species

## 🎯 Model Performance

The Random Forest classifier achieves high accuracy on the Iris dataset:
- **Algorithm**: Random Forest Classifier
- **Train-Test Split**: 80% training, 20% testing
- **Random State**: 42 (for reproducibility)

Performance metrics are displayed in the Jupyter notebook including:
- Accuracy score
- Classification report (precision, recall, F1-score)
- Confusion matrix

## 📈 Technical Details

### Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms and metrics
- **matplotlib & seaborn**: Data visualization
- **streamlit**: Web application framework
- **joblib**: Model serialization

### Model Features
- **Input Features**: 4 numerical features (sepal length, sepal width, petal length, petal width)
- **Output**: 3 classes (iris species)
- **Model Type**: Random Forest (ensemble method)
- **Preprocessing**: Standard scaling applied where needed

## 🔧 File Descriptions

- **`Iris.ipynb`**: Complete machine learning pipeline including data loading, model training, evaluation, and serialization
- **`Website.py`**: Streamlit web application for real-time predictions
- **`iris_model.pkl`**: Serialized trained Random Forest model
- **`iris_columns.pkl`**: Serialized feature column names for consistency

## 🌟 Future Enhancements

- Add more visualization features to the web app
- Implement model comparison with other algorithms
- Add data validation and error handling
- Include feature importance visualization
- Deploy to cloud platforms (Heroku, Streamlit Cloud, etc.)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

*Built with ❤️ using Python, scikit-learn, and Streamlit*