import pickle
import pandas as pd

model, encoder = pickle.load(open("model.pkl", "rb"))

input_data = pd.DataFrame({
    "node_density":[45],
    "packet_rate":[120],
    "retry_count":[6],
    "mobility_speed":[3],
    "signal_strength":[-72],
    "transmission_range":[85]
})

prediction = model.predict(input_data)

label = encoder.inverse_transform(prediction)

print("Predicted congestion level:", label[0])