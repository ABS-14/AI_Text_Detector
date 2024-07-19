# AI Text Classification

This project is designed to classify texts as AI-related or non-AI-related using a Support Vector Machine (SVM) classifier. The classifier is trained on a sample dataset of AI-related and non-AI-related texts and uses TF-IDF vectorization to convert text data into numerical features.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
- [Testing](#testing)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ai-text-classification.git
    cd ai-text-classification
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Train the model:**
    Run the Python script to train the SVM classifier:
    ```bash
    python train.py
    ```

2. **Make predictions:**
    Use the `predict_ai` function in the script to predict whether a given text is AI-related or not.

## Data

The dataset consists of two categories of texts:
- **AI-related texts:** Examples related to machine learning, supervised and unsupervised learning, etc.
- **Non-AI-related texts:** General sentences unrelated to AI.

You can replace the sample dataset with your own data in the script.

## Model

The model uses:
- **TF-IDF Vectorization:** To convert text data into numerical features.
- **Support Vector Machine (SVM):** A popular supervised learning algorithm for classification.

## Testing

The script splits the dataset into training and testing sets (80% training, 20% testing) and evaluates the model's accuracy on the test set.

## Functionality

### Predicting AI-related Texts

You can use the `predict_ai` function to predict if a text is AI-related or not. Here is an example of how to use this function:

```python
example_texts = ["Classification is a supervised learning technique",
                 "My name is John Doe",
                 "Clustering is an unsupervised learning technique"]

for text in example_texts:
    print(text, "->", predict_ai(text))
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request to contribute to the project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides detailed instructions on how to set up, use, and contribute to your AI text classification project. Make sure to replace `https://github.com/yourusername/ai-text-classification.git` with the actual URL of your Git repository.
