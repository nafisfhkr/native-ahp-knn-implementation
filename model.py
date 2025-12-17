import numpy as np
import pandas as pd
from collections import Counter

class HybridKNN:
    def __init__(self, k=15, weights=None):
        self.k = k
        self.weights = np.array(weights)

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def weighted_euclidean_distance(self, row1, row2):
        diff = row1 - row2
        sq_diff = diff ** 2
        weighted_sq_diff = self.weights * sq_diff
        return np.sqrt(np.sum(weighted_sq_diff))

    def predict_single(self, x_input):
        distances = []
        for i in range(len(self.X_train)):
            dist = self.weighted_euclidean_distance(x_input, self.X_train[i])
            distances.append((dist, self.y_train[i]))
        
        
        distances.sort(key=lambda tup: tup[0])
        
        
        k_neighbors = distances[:self.k]
        k_labels = [label for (_, label) in k_neighbors]
        
       
        vote_result = Counter(k_labels).most_common(1)[0][0]
        return vote_result

def load_and_train_model():
    df = pd.read_csv('data/loan_data.csv') 

    df.rename(columns={
        'ApplicantIncome': 'pendapatan_panen',
        'CoapplicantIncome': 'pendapatan_sampingan',
        'LoanAmount': 'jumlah_pinjaman_kur',
        'Loan_Amount_Term': 'durasi_pinjaman',
        'Credit_History': 'riwayat_kredit_digital',
        'Property_Area': 'lokasi_lahan',
        'Loan_Status': 'status_kelayakan'
    }, inplace=True)

    df = df.dropna() 
    df['riwayat_kredit_digital'] = df['riwayat_kredit_digital'].astype(float)
    
    mapping_lokasi = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}
    df['lokasi_lahan'] = df['lokasi_lahan'].map(mapping_lokasi)
    
    feature_cols = ['pendapatan_panen', 'pendapatan_sampingan', 'jumlah_pinjaman_kur',
                    'durasi_pinjaman', 'riwayat_kredit_digital', 'lokasi_lahan']
    
    X_raw = df[feature_cols].values
    y = df['status_kelayakan'].values
    
   
    data_min = X_raw.min(axis=0)
    data_max = X_raw.max(axis=0)
    
    
    X_normalized = (X_raw - data_min) / (data_max - data_min)


    ahp_weights = [0.2129, 0.0840, 0.1370, 0.0771, 0.4508, 0.0382]
    
    model = HybridKNN(k=11, weights=ahp_weights)
    model.fit(X_normalized, y)
    
    return model, data_min, data_max