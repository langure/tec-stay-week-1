# Week 1: Introduction to Natural Language Processing (NLP) and Python Basics

## What is Machine Learning?
Machine Learning is a subfield of artificial intelligence that empowers computers to learn patterns and make predictions from data without being explicitly programmed. In this course, we will delve into one of the exciting applications of machine learning, Natural Language Processing (NLP).

## What is NLP?
Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and human language. It enables computers to understand, interpret, and generate human language, making it an essential component in various AI applications.

## Readings:

[Introduction to Natural Language Processing](https://surface.syr.edu/cgi/viewcontent.cgi?article=1043&context=istpub)

[Commercial applications of Natural Language Processing](https://dl.acm.org/doi/pdf/10.1145/219717.219778)

[Natural language processing: an introduction](https://academic.oup.com/jamia/article/18/5/544/829676?login=false)


## Why Choose Python for Machine Learning?
Python has emerged as one of the most popular programming languages for machine learning and NLP due to its simplicity, readability, and rich ecosystem of libraries. It provides powerful tools and frameworks like TensorFlow, PyTorch, and scikit-learn that facilitate seamless development and experimentation with machine learning models.

## How to Install Python?
To begin your journey in NLP and machine learning with Python, you need to install Python on your machine. Visit the official Python website (https://www.python.org/) and download the latest version compatible with your operating system. Follow the installation instructions provided for your platform.

## How to Set Up a Virtual Environment Using venv?
Virtual environments are essential for managing dependencies and isolating projects. We will use Python's built-in module venv to create a dedicated virtual environment for our course. Follow these steps to set up a virtual environment:

1. Open a terminal or command prompt.

2. Navigate to your project's root directory.

3. Create a virtual environment:
    ```
    python -m venv venv
    ```
4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. You will see the virtual environment name appear in your command prompt or terminal, indicating that the virtual environment is active.


6. You are now ready to install Python packages specific to this project within the virtual environment.

# Installing Pip Dependencies from requirements.txt

To ensure a smooth setup of the project and to have all the required Python packages installed, we will use the `requirements.txt` file. This file lists all the necessary Python packages and their versions. Here's how to install the pip dependencies from `requirements.txt`:

1. **Activate the Virtual Environment:**
   If you haven't already, activate your virtual environment. Use the following commands based on your operating system:

   - On Windows:
     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

2. **Install Dependencies:**
   With the virtual environment active, you can now install the required packages from `requirements.txt` using the `pip` package manager. Run the following command in your terminal or command prompt:

    ```
    pip install -r requirements.txt
    ```


This will automatically read the contents of `requirements.txt` and install all the specified packages and their versions into your virtual environment.

3. **Verification:**
After the installation is complete, you can verify that all the required dependencies are installed in your virtual environment by running the following command:

    ```
    pip list
    ```


This will display a list of all installed packages along with their versions.

Congratulations! You have successfully installed all the necessary pip dependencies for your project using the `requirements.txt` file. You are now ready to move forward with the NLP and text emotion detection course. Happy coding!


Once you have successfully set up the virtual environment, you can proceed with the first practical exercise using Python to solidify your understanding of basic programming concepts.

Happy learning!
