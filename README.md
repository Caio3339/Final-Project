# Personalized Workout & Calorie Burn Tracker
## Video: https://youtu.be/So_vvEXE8FA 

The **Personalized Workout & Calorie Burn Tracker** is a Python-based Streamlit application designed to help users optimize their fitness goals by calculating their Basal Metabolic Rate (BMR), estimating calories burned from various activities, and providing tailored workout plans. The project leverages **Streamlit** for an interactive user interface and **Matplotlib** for data visualization.

## Purpose
This project was created to provide users with a simple yet effective tool to manage their fitness journey. By integrating scientific formulas and workout recommendations, the application enables users to:
- Understand their **BMR** and daily calorie needs.
- Estimate **calories burned** from physical activities.
- Receive **personalized workout plans** based on their fitness level and goals.
- Visualize their fitness data through **interactive graphs**.

## Features
- **BMR Calculation**: Uses the Mifflin-St Jeor Equation to calculate daily calorie needs.
- **Calorie Burn Estimation**: Determines energy expenditure based on MET values for different exercises.
- **Workout Plan Recommendation**: Provides tailored workout plans for beginners, intermediates, and advanced users.
- **Data Visualization**: Includes bar charts for BMR input factors and pie charts for calories burned.
- **Interactive UI**: Powered by Streamlit, enabling easy user input and real-time feedback.

## Files and Their Functionality
### 1. `project.py`
This is the main file containing all the logic for the application. It includes:
- **Function `calculate_bmr(weight, height, age, gender)`**: Computes the Basal Metabolic Rate.
- **Function `estimate_calories_burned(activity, duration, weight)`**: Calculates calories burned based on activity type and duration.
- **Function `recommend_workout_plan(fitness_level, goal)`**: Suggests a workout routine based on user preferences.
- **`main()` function**: Implements the Streamlit interface and integrates all functionalities, including visualizations using Matplotlib.
- **Citations**: Comments within the code cite the use of AI-based tools such as ChatGPT for optimization and debugging.

### 2. `test_project.py`
Contains unit tests for the main functions using **pytest**:
- Tests the **accuracy** of `calculate_bmr()`.
- Verifies that `estimate_calories_burned()` handles valid and invalid inputs correctly.
- Ensures `recommend_workout_plan()` provides correct recommendations for each category.

### 3. `requirements.txt`
Lists all dependencies required to run the project:
- `streamlit` – UI framework.
- `pytest` – Testing framework.
- `matplotlib` – Data visualization.
- `numpy` – Numerical calculations.

### 4. `README.md`
This document explains the project’s **purpose, structure, and implementation details**.

## Design Choices & Considerations
### **1. Why Streamlit?**
We chose **Streamlit** for its simplicity and ability to quickly build web applications without requiring extensive front-end development. It allows real-time interactivity, making it an excellent choice for a fitness tracker.

### **2. Handling Edge Cases**
During development, several **edge cases** were considered:
- **Invalid Gender Inputs**: The BMR function defaults to `None` for incorrect gender inputs.
- **Unknown Activities**: If an activity is not recognized, the function returns `None` instead of producing an incorrect estimate.
- **Negative Values**: Inputs like negative weight, height, or age are prevented using Streamlit's `min_value` parameter.

### **3. Testing & Debugging**
- `pytest.approx()` was used in tests to handle floating-point precision errors.
- Debugging was done iteratively using Streamlit's built-in rerun feature to ensure a smooth user experience.

## Academic Integrity & AI Usage
This project was primarily built based on knowledge acquired in the course, but AI-based tools like **ChatGPT & CS50 duck** were used to enhance productivity, debug errors, and refine code structure. 

## Running the Application
### **1. Install Dependencies**
Run the following command to install required libraries:
```bash
pip install -r requirements.txt
```
### **2. Run the Streamlit App**
Execute the following command in the terminal:
```bash
streamlit run project.py
```

## Future Improvements
- **More Activities**: Expand the MET table to support additional exercises.
- **User Data Persistence**: Allow users to save and track their progress over time.
- **Diet Recommendations**: Integrate a meal planner based on caloric needs.


The **Personalized Workout & Calorie Burn Tracker** is a powerful yet simple tool for anyone looking to improve their fitness. By combining scientific methods with an intuitive interface, users can **make data-driven decisions** about their health. The project demonstrates the practical application of Python, **data visualization**, and **user interface design** using Streamlit
