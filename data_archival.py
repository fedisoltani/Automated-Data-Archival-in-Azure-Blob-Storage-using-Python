from azure.storage.blob import BlobServiceClient
from datetime import datetime, timedelta
import os

def list_blobs(container_name, connection_string):
    """List all blobs in the specified container."""
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    return container_client.list_blobs()

def archive_old_blobs(source_container_name, destination_container_name, days_old, connection_string):
    """
    Move blobs older than the specified number of days from the source container to the destination container.
    
    Args:
    - source_container_name: Name of the source Azure Blob Storage container.
    - destination_container_name: Name of the destination Azure Blob Storage container.
    - days_old: Number of days to determine which blobs to archive.
    - connection_string: Azure Blob Storage connection string.
    """
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    source_container_client = blob_service_client.get_container_client(source_container_name)
    destination_container_client = blob_service_client.get_container_client(destination_container_name)
    
    # Calculate the cutoff date
    cutoff_date = datetime.utcnow() - timedelta(days=days_old)
    
    # List and move blobs
    for blob in source_container_client.list_blobs():
        blob_properties = source_container_client.get_blob_client(blob.name).get_blob_properties()
        blob_last_modified = blob_properties['last_modified']
        
        if blob_last_modified < cutoff_date:
            source_blob_client = source_container_client.get_blob_client(blob.name)
            destination_blob_client = destination_container_client.get_blob_client(blob.name)
            
            # Copy the blob to the destination container
            destination_blob_client.start_copy_from_url(source_blob_client.url)
            
            # Delete the blob from the source container
            source_blob_client.delete_blob()

def delete_old_blobs(container_name, days_old, connection_string):
    """
    Delete blobs older than the specified number of days from the specified container.
    
    Args:
    - container_name: Name of the Azure Blob Storage container.
    - days_old: Number of days to determine which blobs to delete.
    - connection_string: Azure Blob Storage connection string.
    """
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Calculate the cutoff date
    cutoff_date = datetime.utcnow() - timedelta(days=days_old)
    
    # List and delete blobs
    for blob in container_client.list_blobs():
        blob_properties = container_client.get_blob_client(blob.name).get_blob_properties()
        blob_last_modified = blob_properties['last_modified']
        
        if blob_last_modified < cutoff_date:
            blob_client = container_client.get_blob_client(blob.name)
            blob_client.delete_blob()

if __name__ == "__main__":
    # Define your Azure Blob Storage connection string
    connection_string = "<your_connection_string>"
    
    # Define the source and destination containers
    source_container_name = "sourcecontainer"
    destination_container_name = "archivecontainer"
    
    # Archive blobs older than 30 days
    archive_old_blobs(source_container_name, destination_container_name, 30, connection_string)
    
    # Delete blobs older than 60 days
    delete_old_blobs(destination_container_name, 60, connection_string)
