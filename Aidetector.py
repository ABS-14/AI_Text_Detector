# Import necessary libraries
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Sample data
# You can replace this with your own dataset where you have examples of AI and non-AI related texts
ai_texts = ["Supervised Machine Learning : As its name suggests, Supervised machine learning is based on supervision. It means in the supervised learning technique, we train the machines using the labelled dataset, and based on the training, the machine predicts the output. Here, the labelled data specifies that some of the inputs are already mapped to the output. More preciously, we can say; first, we train the machine with the input and corresponding output, and then we ask the machine to predict the output using the test dataset.",
            "Supervised machine learning can be classified into two types of problems, which are given below : Classification &Regression",
            "Unsupervised Machine Learning : Unsupervised learning is different from the Supervised learning technique; as its name suggests, there is no need for supervision. It means, in unsupervised machine learning, the machine is trained using the unlabeled dataset, and the machine predicts the output without any supervision.",
            "Unsupervised Learning can be further classified into two types, which are given below : Clustering & Association",
            "Support Vector Machine Algorithm : Support Vector Machine or SVM is one of the most popular Supervised Learning algorithms, which is used for Classification as well as Regression problems. However, primarily, it is used for Classification problems in Machine Learning.The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so that we can easily put the new data point in the correct category in the future. This best decision boundary is called a hyperplane."]

non_ai_texts = ["The students are present in the class",
                "I love playing football",
                "Humans are top predators",
                "Tomorrow, he is going to complete his academics",
                "My name is Aditya B Suryawanshi, u can call me ABS"]

# Label the data
ai_labels = [1] * len(ai_texts)
non_ai_labels = [0] * len(non_ai_texts)

# Combine the data
all_texts = ai_texts + non_ai_texts
all_labels = ai_labels + non_ai_labels

# Convert text data into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(all_texts)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, all_labels, test_size=0.2, random_state=42)

# Initialize SVM classifier
clf = svm.SVC(kernel='linear')

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Function to predict whether a text is AI related or not
def predict_ai(text):
    text_features = vectorizer.transform([text])
    prediction = clf.predict(text_features)
    if prediction[0] == 1:
        return "AI related"
    else:
        return "Not AI related"

# Test the function with some example texts
example_texts = ["Classification is a supervised learning technique",
                 "My Name is ABS",
                 "Clustering is an unsupervised learning tecnique"]
for text in example_texts:
    print(text, "->", predict_ai(text))

