import h5py
try:
    with h5py.File('models/lstm_model.h5', 'r') as f:
        print("HDF5 file is valid.")
except OSError as e:
    print(f"Error opening HDF5 file: {e}")
