import requests

API_BASE_URL = "http://localhost:8000"

def put_metadata(endpoint, data):
    response = requests.put(f"{API_BASE_URL}/{endpoint}/", json={"meta_data": data})
    if response.status_code == 200:
        print(f"Successfully updated metadata for {endpoint[:-1]}: {response.json()}")
        return response.json()
    else:
        print(f"Failed to update metadata for {endpoint[:-1]}: {response.status_code} - {response.text}")
        return None

def generate_metadata(index: int):
    metadata = {
        "key": f"value_{index}",
        "description": f"This is a detailed sample description for item {index}, which contains more information.",
        "tags": [f"tag_{index % 10}", f"tag_{index % 5}", f"tag_{index % 3}"],
        "created_at": f"2024-12-31T10:00:{index:02d}Z",
        "updated_at": f"2024-12-31T12:00:{index:02d}Z",
        "priority": "high" if index % 2 == 0 else "low",
        "status": "active" if index % 3 == 0 else "inactive"
    }
    return metadata

def load_metadata_for_existing_connections(count=50):
    for index in range(1, count + 1):
        metadata = generate_metadata(index)
        updated_connection = put_metadata(f"connections/{index}", metadata)
        if updated_connection:
            print(f"Metadata updated for connection {index}")
        else:
            print(f"Failed to update metadata for connection {index}")

def main():
    print("Loading metadata for existing connections...")
    load_metadata_for_existing_connections(count=50)
    print("Metadata loading completed.")

if __name__ == "__main__":
    main()