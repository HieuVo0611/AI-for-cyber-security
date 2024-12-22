import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# Dữ liệu mẫu giả lập
sample_data = np.array([
    [80, 500, 1000, 10, 200],
    [443, 800, 1500, 15, 250],
    [53, 600, 1200, 12, 180],
    [22, 700, 1300, 11, 220],
])

# Khởi tạo scaler
scaler = StandardScaler()
scaler.fit(sample_data)

# Lưu scaler vào file
output_path = 'app/models/scaler.pkl'
joblib.dump(scaler, output_path)

print(f"Scaler saved successfully to {output_path}")