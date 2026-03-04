# generate_crop_dataset.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define crop types and their optimal conditions
CROPS = {
    'rice': {
        'N': (60, 90), 'P': (40, 70), 'K': (40, 70),
        'temperature': (22, 32), 'humidity': (70, 90),
        'ph': (5.5, 7.0), 'rainfall': (150, 250)
    },
    'wheat': {
        'N': (50, 80), 'P': (30, 60), 'K': (30, 60),
        'temperature': (15, 25), 'humidity': (50, 70),
        'ph': (6.0, 7.5), 'rainfall': (60, 120)
    },
    'maize': {
        'N': (70, 100), 'P': (40, 70), 'K': (40, 70),
        'temperature': (20, 30), 'humidity': (60, 80),
        'ph': (5.5, 7.0), 'rainfall': (100, 180)
    },
    'cotton': {
        'N': (80, 110), 'P': (40, 70), 'K': (40, 70),
        'temperature': (25, 35), 'humidity': (50, 70),
        'ph': (6.0, 7.5), 'rainfall': (80, 150)
    },
    'sugarcane': {
        'N': (70, 100), 'P': (40, 70), 'K': (50, 80),
        'temperature': (24, 32), 'humidity': (70, 85),
        'ph': (6.0, 7.5), 'rainfall': (150, 250)
    },
    'groundnut': {
        'N': (20, 40), 'P': (30, 60), 'K': (30, 60),
        'temperature': (24, 32), 'humidity': (60, 80),
        'ph': (6.0, 7.0), 'rainfall': (50, 120)
    },
    'potato': {
        'N': (60, 90), 'P': (40, 70), 'K': (50, 80),
        'temperature': (15, 25), 'humidity': (70, 85),
        'ph': (5.5, 6.5), 'rainfall': (120, 200)
    },
    'tomato': {
        'N': (60, 90), 'P': (40, 70), 'K': (50, 80),
        'temperature': (20, 27), 'humidity': (65, 80),
        'ph': (6.0, 7.0), 'rainfall': (100, 160)
    },
    'onion': {
        'N': (50, 80), 'P': (30, 60), 'K': (40, 70),
        'temperature': (13, 24), 'humidity': (60, 75),
        'ph': (6.0, 7.0), 'rainfall': (80, 140)
    },
    'banana': {
        'N': (70, 100), 'P': (30, 60), 'K': (80, 120),
        'temperature': (24, 32), 'humidity': (75, 90),
        'ph': (6.0, 7.5), 'rainfall': (180, 280)
    }
}

def generate_sample(crop, conditions):
    """Generate a single sample for a given crop"""
    text_templates = [
        "The soil has {N} ppm nitrogen, {P} ppm phosphorus, and {K} ppm potassium. Temperature is {temp}°C, humidity is {hum}%, pH is {ph}, and annual rainfall is {rain} mm. What crop should I plant?",
        "Soil analysis shows N:{N}, P:{P}, K:{K}. Weather conditions: {temp}°C, {hum}% humidity, pH {ph}, rainfall {rain}mm. Suggest a suitable crop.",
        "My soil parameters: Nitrogen {N}, Phosphorus {P}, Potassium {K}. Climate data: {temp}°C temperature, {hum}% humidity, pH {ph}, {rain}mm rainfall. Recommend a crop.",
        "With soil NPK levels ({N}, {P}, {K}), temperature {temp}°C, humidity {hum}%, pH {ph}, and rainfall {rain}mm, which crop is best?",
        "Agricultural analysis report: Nitrogen {N}ppm, Phosphorus {P}ppm, Potassium {K}ppm. Environmental factors: {temp}°C, {hum}% RH, pH {ph}, {rain}mm rain. Crop recommendation needed."
    ]
    
    # Generate values within optimal range
    N = np.random.randint(conditions['N'][0], conditions['N'][1] + 10)
    P = np.random.randint(conditions['P'][0], conditions['P'][1] + 10)
    K = np.random.randint(conditions['K'][0], conditions['K'][1] + 10)
    temp = np.random.uniform(conditions['temperature'][0], conditions['temperature'][1] + 2)
    hum = np.random.uniform(conditions['humidity'][0], conditions['humidity'][1] + 5)
    ph = np.random.uniform(conditions['ph'][0], conditions['ph'][1] + 0.3)
    rain = np.random.uniform(conditions['rainfall'][0], conditions['rainfall'][1] + 30)
    
    # Format text
    text = random.choice(text_templates).format(
        N=N, P=P, K=K, temp=round(temp, 1), 
        hum=round(hum, 1), ph=round(ph, 1), rain=round(rain, 1)
    )
    
    return text, crop

def generate_edge_case():
    """Generate samples with conditions not optimal for any specific crop"""
    crops = list(CROPS.keys())
    
    # Generate random conditions
    N = np.random.randint(0, 150)
    P = np.random.randint(0, 150)
    K = np.random.randint(0, 150)
    temp = np.random.uniform(5, 40)
    hum = np.random.uniform(20, 95)
    ph = np.random.uniform(4.0, 8.5)
    rain = np.random.uniform(20, 350)
    
    # Find which crop is closest to these conditions
    best_crop = None
    min_distance = float('inf')
    
    for crop, cond in CROPS.items():
        distance = (
            abs(N - np.mean(cond['N'])) / 50 +
            abs(P - np.mean(cond['P'])) / 50 +
            abs(K - np.mean(cond['K'])) / 50 +
            abs(temp - np.mean(cond['temperature'])) / 20 +
            abs(hum - np.mean(cond['humidity'])) / 30 +
            abs(ph - np.mean(cond['ph'])) / 2 +
            abs(rain - np.mean(cond['rainfall'])) / 150
        )
        if distance < min_distance:
            min_distance = distance
            best_crop = crop
    
    # Generate text
    text_templates = [
        "Soil test results: N:{N}, P:{P}, K:{K}. Current conditions: {temp}°C, {hum}% humidity, pH {ph}, rainfall {rain}mm. What should I plant?",
        "My field has N={N}, P={P}, K={K}. Temperature is {temp}°C, humidity {hum}%, pH {ph}, rainfall {rain}mm. Which crop is suitable?"
    ]
    
    text = random.choice(text_templates).format(
        N=N, P=P, K=K, temp=round(temp, 1), 
        hum=round(hum, 1), ph=round(ph, 1), rain=round(rain, 1)
    )
    
    return text, best_crop

# Generate dataset
print("Generating synthetic dataset...")
data = []
crop_names = list(CROPS.keys())

# Generate 1000 samples per crop
for crop in crop_names:
    for _ in range(1000):
        text, label = generate_sample(crop, CROPS[crop])
        data.append({'text': text, 'label': label})

# Generate 2000 edge cases
for _ in range(2000):
    text, label = generate_edge_case()
    data.append({'text': text, 'label': label})

# Create DataFrame
df = pd.DataFrame(data)
print(f"Total samples generated: {len(df)}")
print(f"Label distribution:\n{df['label'].value_counts()}")

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save dataset
df.to_csv('crop_recommendation_dataset.csv', index=False)
print("Dataset saved to crop_recommendation_dataset.csv")

# Create train/validation/test splits
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42, stratify=df['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42, stratify=temp_df['label'])

print(f"Train size: {len(train_df)}, Validation size: {len(val_df)}, Test size: {len(test_df)}")

# Save splits
train_df.to_csv('train.csv', index=False)
val_df.to_csv('val.csv', index=False)
test_df.to_csv('test.csv', index=False)