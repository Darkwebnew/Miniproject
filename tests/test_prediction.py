import numpy as np
from utils.prediction import predict_disease

class MockModel:
    def predict(self, image):
        output = np.zeros((1, 12))
        output[0,0] = 0.95
        return output

def test_predict_normal():
    result = predict_disease(MockModel(), np.zeros((1,128,128,1)))
    assert result['class'] == 'Normal'
