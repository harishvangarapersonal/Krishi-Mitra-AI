import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

print("--- Starting REAL Yield Prediction Model Training ---")

yield_files = {
    'AP': 'AP.csv',
    'TS': 'TS.csv',
    'JH': 'JK.csv'
}

if not os.path.exists('models'):
    os.makedirs('models')

for state_code, filename in yield_files.items():
    file_path = os.path.join('data', filename)
    print(f"\n--- Processing: {file_path} ---")
    
    try:
        df = pd.read_csv(file_path)
        print(f"  -> Loaded '{filename}' with {len(df)} rows.")

        # Robust 'Area' and 'Year' column cleaning
        df['Area'] = pd.to_numeric(df['Area'], errors='coerce')
        df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})').iloc[:, 0]
        df.dropna(subset=['Area', 'Year', 'Production'], inplace=True)
        
        if df.empty:
            print(f"  -> [ERROR] No usable data found in {filename} after cleaning. Skipping file.")
            continue

        df = df[df['Area'] > 0]
        df['Yield'] = df['Production'] / df['Area']
        
        features = df[['Year', 'Season', 'Crop', 'Area']]
        target = df['Yield']
        
        features_processed = pd.get_dummies(features, columns=['Season', 'Crop'], drop_first=True)
        
        X_train, X_test, y_train, y_test = train_test_split(features_processed, target, test_size=0.2, random_state=42)

        print(f"  -> Training yield model for {state_code}...")
        yield_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
        yield_model.fit(X_train, y_train)
        
        model_filename = f'models/yield_model_{state_code}.joblib'
        joblib.dump(yield_model, model_filename)
        print(f"     ✅ Saved REAL yield model as '{model_filename}'")

    except Exception as e:
        print(f"  -> [ERROR] An error occurred with {filename}: {e}")

print("\n--- Yield Prediction Model Training Finished ---")