import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calculate_bmr(weight, height, age, gender):
    """Calculates Basal Metabolic Rate (BMR) using Mifflin-St Jeor Equation."""
    if gender.lower() == "male":
        return 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif gender.lower() == "female":
        return 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    else:
        return None

def estimate_calories_burned(activity, duration, weight):
    """Estimates calories burned based on activity, duration (minutes), and weight (kg)."""
    activity_met = {
        "running": 9.8,
        "cycling": 7.5,
        "walking": 3.8,
        "swimming": 8.0,
        "jump rope": 12.0
    }
    
    met = activity_met.get(activity.lower(), 0)
    return (met * 3.5 * weight / 200) * duration if met else None

def recommend_workout_plan(fitness_level, goal):
    """Recommends a workout plan based on fitness level and goal."""
    plans = {
        "beginner": {
            "weight loss": "30 min cardio, 3x per week + light strength training",
            "muscle gain": "Full body strength training 3x per week",
            "general fitness": "Mix of cardio and strength, 4x per week"
        },
        "intermediate": {
            "weight loss": "45 min HIIT, 4x per week + moderate strength training",
            "muscle gain": "Upper-lower split strength training, 4x per week",
            "general fitness": "Balanced cardio and weights, 5x per week"
        },
        "advanced": {
            "weight loss": "1-hour HIIT and strength, 5x per week",
            "muscle gain": "Body part split strength training, 5-6x per week",
            "general fitness": "Intense cardio and strength mix, 5x per week"
        }
    }
    
    return plans.get(fitness_level.lower(), {}).get(goal.lower(), "No plan available")

def main():
    """Main function for handling user input and displaying results in Streamlit."""
    st.title("Personalized Workout & Calorie Burn Tracker")
    
    st.header("Calculate BMR")
    weight = st.number_input("Enter weight (kg):", min_value=1.0)
    height = st.number_input("Enter height (cm):", min_value=1.0)
    age = st.number_input("Enter age:", min_value=1)
    gender = st.selectbox("Select gender:", ["Male", "Female"])
    
    if st.button("Calculate BMR"):
        bmr = calculate_bmr(weight, height, age, gender)
        if bmr:
            st.success(f"Your BMR is {bmr:.2f} calories/day.")
            
           
            labels = ['Weight', 'Height', 'Age']
            values = [weight, height, age]
            
            fig, ax = plt.subplots()
            ax.bar(labels, values, color=['blue', 'green', 'red'])
            ax.set_ylabel('Value')
            ax.set_title('BMR Input Factors')
            st.pyplot(fig)
        else:
            st.error("Invalid gender selection.")
    
    st.header("Estimate Calories Burned")
    activity = st.selectbox("Select activity:", ["Running", "Cycling", "Walking", "Swimming", "Jump Rope"])
    duration = st.number_input("Enter duration (minutes):", min_value=1)
    
    if st.button("Calculate Calories Burned"):
        calories_burned = estimate_calories_burned(activity, duration, weight)
        if calories_burned:
            st.success(f"You burned approximately {calories_burned:.2f} calories.")
            
            fig, ax = plt.subplots()
            bmr_value = calculate_bmr(weight, height, age, gender) if weight and height and age else 2000
            ax.pie([calories_burned, max(bmr_value - calories_burned, 0)], 
                   labels=["Burned", "Remaining"], 
                   autopct='%1.1f%%', 
                   colors=['orange', 'gray'])
            ax.set_title("Calories Burned vs Remaining")
            st.pyplot(fig)
        else:
            st.error("Invalid activity selection.")
    
    st.header("Get a Workout Plan")
    fitness_level = st.selectbox("Select fitness level:", ["Beginner", "Intermediate", "Advanced"])
    goal = st.selectbox("Select goal:", ["Weight Loss", "Muscle Gain", "General Fitness"])
    
    if st.button("Get Plan"):
        plan = recommend_workout_plan(fitness_level, goal)
        st.info(plan)

if __name__ == "__main__":
    main()
