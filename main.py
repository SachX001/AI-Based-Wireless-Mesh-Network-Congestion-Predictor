import pickle
import pandas as pd


def run_prediction():

    print("\nMesh Network Congestion Predictor\n")

    node_density = int(input("Enter node density: "))
    packet_rate = int(input("Enter packet rate: "))
    retry_count = int(input("Enter retry count: "))
    mobility_speed = int(input("Enter mobility speed: "))
    signal_strength = int(input("Enter signal strength: "))
    transmission_range = int(input("Enter transmission range: "))

    model, encoder = pickle.load(open("model.pkl", "rb"))

    input_data = pd.DataFrame({
        "node_density": [node_density],
        "packet_rate": [packet_rate],
        "retry_count": [retry_count],
        "mobility_speed": [mobility_speed],
        "signal_strength": [signal_strength],
        "transmission_range": [transmission_range]
    })

    prediction = model.predict(input_data)

    label = encoder.inverse_transform(prediction)

    print("\nPredicted Congestion Level:", label[0])


if __name__ == "__main__":
    run_prediction()