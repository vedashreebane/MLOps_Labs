import pandas as pd
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from kneed import KneeLocator


def load_data():
    # Load the vehicle dataset
    data = pd.read_csv('/opt/airflow/data/vehicle.csv')
    
    print(f"Data loaded successfully. Shape: {data.shape}")
    print(f"Columns: {data.columns.tolist()}")
    
    # Serialize the data
    serialized_data = pickle.dumps(data)
    
    return serialized_data


def data_preprocessing(serialized_data):
    # Deserialize the data
    data = pickle.loads(serialized_data)
    
    print("Starting data preprocessing...")
    
    # Remove the 'Class' column as it's the target variable (we're doing unsupervised clustering)
    if 'Class' in data.columns:
        data = data.drop('Class', axis=1)
    
    # Check for and handle missing values
    data = data.dropna()
    
    # Select only numeric columns for clustering
    numeric_data = data.select_dtypes(include=['int64', 'float64'])
    
    print(f"Numeric data shape after preprocessing: {numeric_data.shape}")
    
    # Standardize the features (important for K-Means)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)
    
    print("Data preprocessing completed.")
    
    # Serialize the preprocessed data
    serialized_preprocessed_data = pickle.dumps(scaled_data)
    
    return serialized_preprocessed_data


def build_save_model(serialized_data, filename):
    # Deserialize the data
    data = pickle.loads(serialized_data)
    
    print("Building K-Means clustering model...")
    
    # Calculate SSE (Sum of Squared Errors) for different numbers of clusters
    # This is for the elbow method
    sse_values = []
    k_range = range(1, 11)  # Test from 1 to 10 clusters
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10, max_iter=300)
        kmeans.fit(data)
        sse_values.append(kmeans.inertia_)
        print(f"K={k}, SSE={kmeans.inertia_:.2f}")
    
    # Build the final model with a reasonable number of clusters
    # You can adjust this based on your elbow method results
    final_n_clusters = 4  # Vehicle dataset typically works well with 4 clusters
    
    print(f"\nTraining final model with {final_n_clusters} clusters...")
    final_kmeans = KMeans(n_clusters=final_n_clusters, random_state=42, n_init=10, max_iter=300)
    final_kmeans.fit(data)
    
    # Save the model to the working_data directory
    model_path = f'/opt/airflow/working_data/{filename}'
    with open(model_path, 'wb') as f:
        pickle.dump(final_kmeans, f)
    
    print(f"Model saved successfully to {model_path}")
    print(f"Model has {final_kmeans.n_clusters} clusters")
    print(f"Model inertia: {final_kmeans.inertia_:}")
    
    # Return SSE values for elbow method analysis
    return sse_values


def load_model_elbow(filename, sse):
    # Load the saved model
    model_path = f'/opt/airflow/working_data/{filename}'
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    print(f"Model loaded successfully from {model_path}")
    
    # Use KneeLocator to find the optimal number of clusters (elbow point)
    kl = KneeLocator(
        range(1, 11), 
        sse, 
        curve='convex', 
        direction='decreasing'
    )
    
    optimal_clusters = kl.elbow
    
    print("\n" + "="*50)
    print("ELBOW METHOD RESULTS")
    print("="*50)
    print(f"Optimal number of clusters (elbow point): {optimal_clusters}")
    print(f"Model was trained with: {model.n_clusters} clusters")
    print(f"\nSSE values for K=1 to K=10:")
    for i, sse_val in enumerate(sse, 1):
        marker = " <-- Elbow" if i == optimal_clusters else ""
        print(f"  K={i}: SSE={sse_val:.2f}{marker}")
    print("="*50)
    
    result = {
        'optimal_clusters': optimal_clusters,
        'sse_values': sse,
        'model_clusters': model.n_clusters,
        'model_inertia': model.inertia_,
        'cluster_centers': model.cluster_centers_.tolist()
    }
    
    return result
