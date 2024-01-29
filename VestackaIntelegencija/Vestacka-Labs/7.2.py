import warnings
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.exceptions import ConvergenceWarning
from sklearn.preprocessing import LabelEncoder

dataset = [
    [9.2, 0.755, 0.18, 2.2, 0.148, 10.0, 103.0, 0.9969, 2.87, 1.36, 10.2, 8.476],
    [9.6, 0.6, 0.5, 2.3, 0.079, 28.0, 71.0, 0.9997, 3.5, 0.57, 9.7, 4.501],
    [9.6, 0.6, 0.5, 2.3, 0.079, 28.0, 71.0, 0.9997, 3.5, 0.57, 9.7, 1.962],
    [11.5, 0.31, 0.51, 2.2, 0.079, 14.0, 28.0, 0.9982, 3.03, 0.93, 9.8, 7.649],
    [11.4, 0.46, 0.5, 2.7, 0.122, 4.0, 17.0, 1.0006, 3.13, 0.7, 10.2, 4.368],
    [11.3, 0.37, 0.41, 2.3, 0.088, 6.0, 16.0, 0.9988, 3.09, 0.8, 9.3, 1.04],
    [8.3, 0.54, 0.24, 3.4, 0.076, 16.0, 112.0, 0.9976, 3.27, 0.61, 9.4, 4.215],
    [8.2, 0.56, 0.23, 3.4, 0.078, 14.0, 104.0, 0.9976, 3.28, 0.62, 9.4, 3.67],
    [10.0, 0.58, 0.22, 1.9, 0.08, 9.0, 32.0, 0.9974, 3.13, 0.55, 9.5, 4.789],
    [7.9, 0.51, 0.25, 2.9, 0.077, 21.0, 45.0, 0.9974, 3.49, 0.96, 12.1, 9.509],
    [6.8, 0.69, 0.0, 5.6, 0.124, 21.0, 58.0, 0.9997, 3.46, 0.72, 10.2, 3.616],
    [6.8, 0.69, 0.0, 5.6, 0.124, 21.0, 58.0, 0.9997, 3.46, 0.72, 10.2, 0.552],
    [8.8, 0.6, 0.29, 2.2, 0.098, 5.0, 15.0, 0.9988, 3.36, 0.49, 9.1, 1.877],
    [8.8, 0.6, 0.29, 2.2, 0.098, 5.0, 15.0, 0.9988, 3.36, 0.49, 9.1, 4.788],
    [8.7, 0.54, 0.26, 2.5, 0.097, 7.0, 31.0, 0.9976, 3.27, 0.6, 9.3, 7.918],
    [7.6, 0.685, 0.23, 2.3, 0.111, 20.0, 84.0, 0.9964, 3.21, 0.61, 9.3, 4.134],
    [8.7, 0.54, 0.26, 2.5, 0.097, 7.0, 31.0, 0.9976, 3.27, 0.6, 9.3, 9.288],
    [10.4, 0.28, 0.54, 2.7, 0.105, 5.0, 19.0, 0.9988, 3.25, 0.63, 9.5, 4.313],
    [7.6, 0.41, 0.14, 3.0, 0.087, 21.0, 43.0, 0.9964, 3.32, 0.57, 10.5, 6.104],
    [10.1, 0.935, 0.22, 3.4, 0.105, 11.0, 86.0, 1.001, 3.43, 0.64, 11.3, 0.133],
    [7.9, 0.35, 0.21, 1.9, 0.073, 46.0, 102.0, 0.9964, 3.27, 0.58, 9.5, 4.619],
    [8.7, 0.84, 0.0, 1.4, 0.065, 24.0, 33.0, 0.9954, 3.27, 0.55, 9.7, 3.569],
    [9.6, 0.88, 0.28, 2.4, 0.086, 30.0, 147.0, 0.9979, 3.24, 0.53, 9.4, 2.973],
    [9.5, 0.885, 0.27, 2.3, 0.084, 31.0, 145.0, 0.9978, 3.24, 0.53, 9.4, 0.794],
    [7.7, 0.915, 0.12, 2.2, 0.143, 7.0, 23.0, 0.9964, 3.35, 0.65, 10.2, 9.882],
    [8.9, 0.29, 0.35, 1.9, 0.067, 25.0, 57.0, 0.997, 3.18, 1.36, 10.3, 8.18],
    [9.9, 0.54, 0.45, 2.3, 0.071, 16.0, 40.0, 0.9991, 3.39, 0.62, 9.4, 4.621],
    [9.5, 0.59, 0.44, 2.3, 0.071, 21.0, 68.0, 0.9992, 3.46, 0.63, 9.5, 2.028],
    [9.9, 0.54, 0.45, 2.3, 0.071, 16.0, 40.0, 0.9991, 3.39, 0.62, 9.4, 1.607],
    [9.5, 0.59, 0.44, 2.3, 0.071, 21.0, 68.0, 0.9992, 3.46, 0.63, 9.5, 1.59],
    [9.9, 0.54, 0.45, 2.3, 0.071, 16.0, 40.0, 0.9991, 3.39, 0.62, 9.4, 3.249],
    [7.8, 0.64, 0.1, 6.0, 0.115, 5.0, 11.0, 0.9984, 3.37, 0.69, 10.1, 9.116],
    [7.3, 0.67, 0.05, 3.6, 0.107, 6.0, 20.0, 0.9972, 3.4, 0.63, 10.1, 1.561],
    [8.3, 0.845, 0.01, 2.2, 0.07, 5.0, 14.0, 0.9967, 3.32, 0.58, 11.0, 2.249],
    [8.7, 0.48, 0.3, 2.8, 0.066, 10.0, 28.0, 0.9964, 3.33, 0.67, 11.2, 6.606],
    [6.7, 0.42, 0.27, 8.6, 0.068, 24.0, 148.0, 0.9948, 3.16, 0.57, 11.3, 8.837],
    [10.7, 0.43, 0.39, 2.2, 0.106, 8.0, 32.0, 0.9986, 2.89, 0.5, 9.6, 3.886],
    [9.8, 0.88, 0.25, 2.5, 0.104, 35.0, 155.0, 1.001, 3.41, 0.67, 11.2, 3.057],
    [15.9, 0.36, 0.65, 7.5, 0.096, 22.0, 71.0, 0.9976, 2.98, 0.84, 14.9, 1.379],
    [9.4, 0.33, 0.59, 2.8, 0.079, 9.0, 30.0, 0.9976, 3.12, 0.54, 12.0, 5.886],
    [8.6, 0.47, 0.47, 2.4, 0.074, 7.0, 29.0, 0.9979, 3.08, 0.46, 9.5, 0.649],
    [9.7, 0.55, 0.17, 2.9, 0.087, 20.0, 53.0, 1.0004, 3.14, 0.61, 9.4, 4.651],
    [10.7, 0.43, 0.39, 2.2, 0.106, 8.0, 32.0, 0.9986, 2.89, 0.5, 9.6, 0.702],
    [12.0, 0.5, 0.59, 1.4, 0.073, 23.0, 42.0, 0.998, 2.92, 0.68, 10.5, 9.199],
    [7.2, 0.52, 0.07, 1.4, 0.074, 5.0, 20.0, 0.9973, 3.32, 0.81, 9.6, 8.679],
    [7.1, 0.84, 0.02, 4.4, 0.096, 5.0, 13.0, 0.997, 3.41, 0.57, 11.0, 0.572],
    [7.2, 0.52, 0.07, 1.4, 0.074, 5.0, 20.0, 0.9973, 3.32, 0.81, 9.6, 7.303],
    [7.5, 0.42, 0.31, 1.6, 0.08, 15.0, 42.0, 0.9978, 3.31, 0.64, 9.0, 2.426],
    [7.2, 0.57, 0.06, 1.6, 0.076, 9.0, 27.0, 0.9972, 3.36, 0.7, 9.6, 9.651],
    [10.1, 0.28, 0.46, 1.8, 0.05, 5.0, 13.0, 0.9974, 3.04, 0.79, 10.2, 8.719],
    [12.1, 0.4, 0.52, 2.0, 0.092, 15.0, 54.0, 1.0, 3.03, 0.66, 10.2, 2.549],
    [9.4, 0.59, 0.14, 2.0, 0.084, 25.0, 48.0, 0.9981, 3.14, 0.56, 9.7, 1.807],
    [8.3, 0.49, 0.36, 1.8, 0.222, 6.0, 16.0, 0.998, 3.18, 0.6, 9.5, 9.662],
    [11.3, 0.34, 0.45, 2.0, 0.082, 6.0, 15.0, 0.9988, 2.94, 0.66, 9.2, 5.325],
    [10.0, 0.73, 0.43, 2.3, 0.059, 15.0, 31.0, 0.9966, 3.15, 0.57, 11.0, 1.467],
    [11.3, 0.34, 0.45, 2.0, 0.082, 6.0, 15.0, 0.9988, 2.94, 0.66, 9.2, 6.94],
    [6.9, 0.4, 0.24, 2.5, 0.083, 30.0, 45.0, 0.9959, 3.26, 0.58, 10.0, 2.293],
    [8.2, 0.73, 0.21, 1.7, 0.074, 5.0, 13.0, 0.9968, 3.2, 0.52, 9.5, 3.172],
    [9.8, 1.24, 0.34, 2.0, 0.079, 32.0, 151.0, 0.998, 3.15, 0.53, 9.5, 0.48],
    [8.2, 0.73, 0.21, 1.7, 0.074, 5.0, 13.0, 0.9968, 3.2, 0.52, 9.5, 4.347],
    [10.8, 0.4, 0.41, 2.2, 0.084, 7.0, 17.0, 0.9984, 3.08, 0.67, 9.3, 9.726],
    [9.3, 0.41, 0.39, 2.2, 0.064, 12.0, 31.0, 0.9984, 3.26, 0.65, 10.2, 1.749],
    [10.8, 0.4, 0.41, 2.2, 0.084, 7.0, 17.0, 0.9984, 3.08, 0.67, 9.3, 9.986],
    [8.6, 0.8, 0.11, 2.3, 0.084, 12.0, 31.0, 0.9979, 3.4, 0.48, 9.9, 3.891],
    [8.3, 0.78, 0.1, 2.6, 0.081, 45.0, 87.0, 0.9983, 3.48, 0.53, 10.0, 0.532],
    [10.8, 0.26, 0.45, 3.3, 0.06, 20.0, 49.0, 0.9972, 3.13, 0.54, 9.6, 4.481],
    [13.3, 0.43, 0.58, 1.9, 0.07, 15.0, 40.0, 1.0004, 3.06, 0.49, 9.0, 3.679],
    [8.0, 0.45, 0.23, 2.2, 0.094, 16.0, 29.0, 0.9962, 3.21, 0.49, 10.2, 5.899],
    [8.5, 0.46, 0.31, 2.25, 0.078, 32.0, 58.0, 0.998, 3.33, 0.54, 9.8, 0.363],
    [8.1, 0.78, 0.23, 2.6, 0.059, 5.0, 15.0, 0.997, 3.37, 0.56, 11.3, 4.269],
    [9.8, 0.98, 0.32, 2.3, 0.078, 35.0, 152.0, 0.998, 3.25, 0.48, 9.4, 2.327],
    [8.1, 0.78, 0.23, 2.6, 0.059, 5.0, 15.0, 0.997, 3.37, 0.56, 11.3, 1.597],
    [7.1, 0.65, 0.18, 1.8, 0.07, 13.0, 40.0, 0.997, 3.44, 0.6, 9.1, 3.238],
    [9.1, 0.64, 0.23, 3.1, 0.095, 13.0, 38.0, 0.9998, 3.28, 0.59, 9.7, 0.47],
    [7.7, 0.66, 0.04, 1.6, 0.039, 4.0, 9.0, 0.9962, 3.4, 0.47, 9.4, 3.359],
    [8.1, 0.38, 0.48, 1.8, 0.157, 5.0, 17.0, 0.9976, 3.3, 1.05, 9.4, 2.198],
    [7.4, 1.185, 0.0, 4.25, 0.097, 5.0, 14.0, 0.9966, 3.63, 0.54, 10.7, 0.38],
    [9.2, 0.92, 0.24, 2.6, 0.087, 12.0, 93.0, 0.9998, 3.48, 0.54, 9.8, 1.092],
    [8.6, 0.49, 0.51, 2.0, 0.422, 16.0, 62.0, 0.9979, 3.03, 1.17, 9.0, 1.267],
    [9.0, 0.48, 0.32, 2.8, 0.084, 21.0, 122.0, 0.9984, 3.32, 0.62, 9.4, 4.224],
    [9.0, 0.47, 0.31, 2.7, 0.084, 24.0, 125.0, 0.9984, 3.31, 0.61, 9.4, 1.862],
    [5.1, 0.47, 0.02, 1.3, 0.034, 18.0, 44.0, 0.9921, 3.9, 0.62, 12.8, 7.591],
    [7.0, 0.65, 0.02, 2.1, 0.066, 8.0, 25.0, 0.9972, 3.47, 0.67, 9.5, 6.173],
    [7.0, 0.65, 0.02, 2.1, 0.066, 8.0, 25.0, 0.9972, 3.47, 0.67, 9.5, 6.18],
    [9.4, 0.615, 0.28, 3.2, 0.087, 18.0, 72.0, 1.0001, 3.31, 0.53, 9.7, 0.947],
    [11.8, 0.38, 0.55, 2.1, 0.071, 5.0, 19.0, 0.9986, 3.11, 0.62, 10.8, 9.786],
    [10.6, 1.02, 0.43, 2.9, 0.076, 26.0, 88.0, 0.9984, 3.08, 0.57, 10.1, 7.425],
    [7.0, 0.65, 0.02, 2.1, 0.066, 8.0, 25.0, 0.9972, 3.47, 0.67, 9.5, 9.568],
    [7.0, 0.64, 0.02, 2.1, 0.067, 9.0, 23.0, 0.997, 3.47, 0.67, 9.4, 8.263],
    [10.4, 0.44, 0.42, 1.5, 0.145, 34.0, 48.0, 0.99832, 3.38, 0.86, 9.9, 3.491],
    [11.6, 0.47, 0.44, 1.6, 0.147, 36.0, 51.0, 0.99836, 3.38, 0.86, 9.9, 0.532],
    [8.8, 0.685, 0.26, 1.6, 0.088, 16.0, 23.0, 0.99694, 3.32, 0.47, 9.4, 0.944],
    [7.6, 0.665, 0.1, 1.5, 0.066, 27.0, 55.0, 0.99655, 3.39, 0.51, 9.3, 0.785],
    [6.7, 0.28, 0.28, 2.4, 0.012, 36.0, 100.0, 0.99064, 3.26, 0.39, 11.7, 5.764],
    [6.7, 0.28, 0.28, 2.4, 0.012, 36.0, 100.0, 0.99064, 3.26, 0.39, 11.7, 8.84],
    [10.1, 0.31, 0.35, 1.6, 0.075, 9.0, 28.0, 0.99672, 3.24, 0.83, 11.2, 6.921],
    [6.0, 0.5, 0.04, 2.2, 0.092, 13.0, 26.0, 0.99647, 3.46, 0.47, 10.0, 3.465],
    [11.1, 0.42, 0.47, 2.65, 0.085, 9.0, 34.0, 0.99736, 3.24, 0.77, 12.1, 9.32],
    [6.6, 0.66, 0.0, 3.0, 0.115, 21.0, 31.0, 0.99629, 3.45, 0.63, 10.3, 3.078],
    [10.6, 0.5, 0.45, 2.6, 0.119, 34.0, 68.0, 0.99708, 3.23, 0.72, 10.9, 5.076],
    [7.1, 0.685, 0.35, 2.0, 0.088, 9.0, 92.0, 0.9963, 3.28, 0.62, 9.4, 0.828],
    [9.9, 0.25, 0.46, 1.7, 0.062, 26.0, 42.0, 0.9959, 3.18, 0.83, 10.6, 5.672],
    [6.4, 0.64, 0.21, 1.8, 0.081, 14.0, 31.0, 0.99689, 3.59, 0.66, 9.8, 0.147],
    [6.4, 0.64, 0.21, 1.8, 0.081, 14.0, 31.0, 0.99689, 3.59, 0.66, 9.8, 2.499],
    [7.4, 0.68, 0.16, 1.8, 0.078, 12.0, 39.0, 0.9977, 3.5, 0.7, 9.9, 5.048],
    [6.4, 0.64, 0.21, 1.8, 0.081, 14.0, 31.0, 0.99689, 3.59, 0.66, 9.8, 0.825],
    [6.4, 0.63, 0.21, 1.6, 0.08, 12.0, 32.0, 0.99689, 3.58, 0.66, 9.8, 0.432],
    [9.3, 0.43, 0.44, 1.9, 0.085, 9.0, 22.0, 0.99708, 3.28, 0.55, 9.5, 4.252],
    [9.3, 0.43, 0.44, 1.9, 0.085, 9.0, 22.0, 0.99708, 3.28, 0.55, 9.5, 3.61],
    [8.0, 0.42, 0.32, 2.5, 0.08, 26.0, 122.0, 0.99801, 3.22, 1.07, 9.7, 3.397],
    [9.3, 0.36, 0.39, 1.5, 0.08, 41.0, 55.0, 0.99652, 3.47, 0.73, 10.9, 6.264],
    [9.3, 0.36, 0.39, 1.5, 0.08, 41.0, 55.0, 0.99652, 3.47, 0.73, 10.9, 8.461],
    [7.6, 0.735, 0.02, 2.5, 0.071, 10.0, 14.0, 0.99538, 3.51, 0.71, 11.7, 8.02],
    [9.3, 0.36, 0.39, 1.5, 0.08, 41.0, 55.0, 0.99652, 3.47, 0.73, 10.9, 5.754],
    [8.2, 0.26, 0.34, 2.5, 0.073, 16.0, 47.0, 0.99594, 3.4, 0.78, 11.3, 6.298],
    [11.7, 0.28, 0.47, 1.7, 0.054, 17.0, 32.0, 0.99686, 3.15, 0.67, 10.6, 5.097],
    [6.8, 0.56, 0.22, 1.8, 0.074, 15.0, 24.0, 0.99438, 3.4, 0.82, 11.2, 7.14],
    [7.2, 0.62, 0.06, 2.7, 0.077, 15.0, 85.0, 0.99746, 3.51, 0.54, 9.5, 1.595],
    [5.8, 1.01, 0.66, 2.0, 0.039, 15.0, 88.0, 0.99357, 3.66, 0.6, 11.5, 5.603],
    [7.5, 0.42, 0.32, 2.7, 0.067, 7.0, 25.0, 0.99628, 3.24, 0.44, 10.4, 3.295],
    [7.2, 0.62, 0.06, 2.5, 0.078, 17.0, 84.0, 0.99746, 3.51, 0.53, 9.7, 4.694],
    [7.2, 0.62, 0.06, 2.7, 0.077, 15.0, 85.0, 0.99746, 3.51, 0.54, 9.5, 3.626],
    [7.2, 0.635, 0.07, 2.6, 0.077, 16.0, 86.0, 0.99748, 3.51, 0.54, 9.7, 3.773],
    [6.8, 0.49, 0.22, 2.3, 0.071, 13.0, 24.0, 0.99438, 3.41, 0.83, 11.3, 9.929],
    [6.9, 0.51, 0.23, 2.0, 0.072, 13.0, 22.0, 0.99438, 3.4, 0.84, 11.2, 7.175],
    [6.8, 0.56, 0.22, 1.8, 0.074, 15.0, 24.0, 0.99438, 3.4, 0.82, 11.2, 8.8],
    [7.6, 0.63, 0.03, 2.0, 0.08, 27.0, 43.0, 0.99578, 3.44, 0.64, 10.9, 9.165],
    [7.7, 0.715, 0.01, 2.1, 0.064, 31.0, 43.0, 0.99371, 3.41, 0.57, 11.8, 6.849],
    [6.9, 0.56, 0.03, 1.5, 0.086, 36.0, 46.0, 0.99522, 3.53, 0.57, 10.6, 0.484],
    [7.3, 0.35, 0.24, 2.0, 0.067, 28.0, 48.0, 0.99576, 3.43, 0.54, 10.0, 3.679],
    [9.1, 0.21, 0.37, 1.6, 0.067, 6.0, 10.0, 0.99552, 3.23, 0.58, 11.1, 8.272],
    [10.4, 0.38, 0.46, 2.1, 0.104, 6.0, 10.0, 0.99664, 3.12, 0.65, 11.8, 8.446],
    [8.8, 0.31, 0.4, 2.8, 0.109, 7.0, 16.0, 0.99614, 3.31, 0.79, 11.8, 6.403],
    [7.1, 0.47, 0.0, 2.2, 0.067, 7.0, 14.0, 0.99517, 3.4, 0.58, 10.9, 3.292],
    [7.7, 0.715, 0.01, 2.1, 0.064, 31.0, 43.0, 0.99371, 3.41, 0.57, 11.8, 6.079],
    [8.8, 0.61, 0.19, 4.0, 0.094, 30.0, 69.0, 0.99787, 3.22, 0.5, 10.0, 9.456],
    [7.2, 0.6, 0.04, 2.5, 0.076, 18.0, 88.0, 0.99745, 3.53, 0.55, 9.5, 0.385],
    [9.2, 0.56, 0.18, 1.6, 0.078, 10.0, 21.0, 0.99576, 3.15, 0.49, 9.9, 0.136],
    [7.6, 0.715, 0.0, 2.1, 0.068, 30.0, 35.0, 0.99533, 3.48, 0.65, 11.4, 6.845]]


def trainee_factory(set):
    x = [row[:-1] for row in set]
    y = [row[-1] for row in set]
    return x, y


def transform_dataset(dataset_tmp):
    new_dataset = list()
    for row in dataset_tmp:
        new_row = list()
        new_row = row[:-1]
        if (row[-1]) >= 5:
            new_row.append(1)
        else:
            new_row.append(0)
        new_dataset.append(new_row)
    return new_dataset


def divide_sets(set, x):
    test_set = set[:int(x * len(set))]
    train_set = set[int(x * len(set)):]
    return train_set, test_set


def create_new_set(set, least_important_feature):
    new_x = list()
    for row in set:
        new_row = [row[i] for i in range(len(row)) if i != least_important_feature]
        new_x.append(new_row)
    return new_x

def calculate_accuracy(test_x,test_y,classifier):
    accuracy = 0
    for x, y in zip(test_x, test_y):
        predicted = classifier.predict([x])[0]
        if (predicted == y):
            accuracy += 1
    return  accuracy/len(test_y)

if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=ConvergenceWarning)
    x = (int(input()) / 100)
    tree = DecisionTreeClassifier(criterion="gini", random_state=0)
    train_set, test_set = divide_sets(transform_dataset(dataset), x)
    train_x, train_y = trainee_factory(train_set)
    test_x, test_y = trainee_factory(test_set)
    tree.fit(train_x, train_y)
    features = list(tree.feature_importances_)
    least_important_feature = features.index(min(features))
    new_train_x = create_new_set(train_x, least_important_feature)
    new_test_x=create_new_set(test_x,least_important_feature)
    classifier=MLPClassifier(15,activation="relu",learning_rate_init=0.001,max_iter=200,random_state=0)
    standard_scaler=StandardScaler()
    standard_scaler.fit(new_train_x)
    classifier.fit(standard_scaler.transform(new_train_x),train_y)
    new_test_x_standard=standard_scaler.transform(new_test_x)
    print(f"Tocnost so StandardScaler: {calculate_accuracy(new_test_x_standard,test_y,classifier)}")
    min_max_scaler=MinMaxScaler()
    min_max_scaler.fit(new_train_x)
    classifier.fit(min_max_scaler.transform(new_train_x),train_y)
    new_test_x_min_max=min_max_scaler.transform(new_test_x)
    print(f"Tocnost so MinMaxScaler: {calculate_accuracy(new_test_x_min_max,test_y,classifier)}")


