import matplotlib.pyplot as plt

def plot_predictions(y_true, y_pred, title="Prediction vs Ground Truth"):
    plt.figure(figsize=(10, 5))
    plt.plot(y_true, label='True Values', marker='o')
    plt.plot(y_pred, label='Predicted Values', marker='x')
    plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("Target Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
