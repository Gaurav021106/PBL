import sys
import subprocess

required = ["pandas", "numpy", "scikit-learn"]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("\n📦 Checking & Installing Required Libraries...\n")
for pkg in required:
    try:
        __import__(pkg)
        print(f"✅ {pkg} already installed")
    except ImportError:
        print(f"⏳ Installing {pkg}...")
        install(pkg)

print("\n🎉 All required libraries are ready!\n")


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv("symptoms_disease.csv")


X = data.drop("disease", axis=1)


y = data["disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

medicines = {
    "Flu": "Paracetamol, Cough Syrup, Warm fluids, Rest",
    "Malaria": "Antimalarial tablets (Chloroquine/Artemisinin), Hydration, Doctor consult",
    "Cold": "Steam inhalation, Ginger tea, Cough Syrup",
    "Typhoid": "Antibiotics (as per doctor), Hydration, Soft diet",
    "Heart Attack": "Aspirin (if available), Immediate hospitalization, Call emergency services",
    "Kidney Failure": "Low-salt diet, Avoid painkillers, Dialysis may be required → Consult nephrologist",
    "Stroke": "Immediate hospitalization, Blood thinner medicines (as per doctor), CT/MRI scan",
    "Dengue": "Paracetamol (no aspirin), Hydration, Platelet monitoring, Doctor consult",
    "Bronchitis": "Cough Syrup, Warm fluids, Inhaler (if prescribed), Rest",
    "Food Poisoning": "ORS solution, Hydration, Light diet, Antibiotics (if prescribed)"
}


print("\n--- Rural Healthcare AI Assistant ---")
print("Enter your symptoms (yes=1 / no=0)")

fever = int(input("Fever (1/0): "))
cough = int(input("Cough (1/0): "))
headache = int(input("Headache (1/0): "))
fatigue = int(input("Fatigue (1/0): "))
nausea = int(input("Nausea (1/0): "))
chest_pain = int(input("Chest Pain (1/0): "))
shortness_of_breath = int(input("Shortness of Breath (1/0): "))
confusion = int(input("Confusion / Dizziness (1/0): "))
swelling_legs = int(input("Swelling in Legs (1/0): "))
vision_problem = int(input("Vision Problem (1/0): "))


user_symptoms = [[
    fever, cough, headache, fatigue, nausea,
    chest_pain, shortness_of_breath, confusion,
    swelling_legs, vision_problem
]]

prediction = model.predict(user_symptoms)[0]
print(f"\n🔎 Possible Disease: {prediction}")
print(f"💊 Recommended Medicine/Remedy: {medicines.get(prediction, 'Consult a doctor')}")

if prediction in ["Heart Attack", "Kidney Failure", "Stroke", "Malaria", "Typhoid", "Dengue"]:
    print("⚠️ Please consult a doctor IMMEDIATELY for further treatment.")
else:
    print("✅ You may recover with basic medicines, but see a doctor if symptoms worsen.")