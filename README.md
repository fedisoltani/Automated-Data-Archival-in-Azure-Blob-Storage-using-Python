# Automated Data Archival in Azure Blob Storage using Python

This repository contains a Python script to automate the archival and deletion of data in Azure Blob Storage based on the age of the blobs.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Listing All Blobs in a Container](#listing-all-blobs-in-a-container)
  - [Archiving Old Blobs](#archiving-old-blobs)
  - [Deleting Old Blobs](#deleting-old-blobs)
  - [Examples](#examples)
- [License](#license)

## Introduction

This project demonstrates how to manage data in Azure Blob Storage by automatically archiving and deleting blobs based on their age. The solution uses the `azure-storage-blob` library to interact with Azure Blob Storage.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/data-archival-azure-blob.git
    cd data-archival-azure-blob
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Listing All Blobs in a Container

To list all blobs in a specified Azure Blob Storage container, use the following script:

```python
from data_archival import list_blobs

connection_string = "<your_connection_string>"
container_name = "sourcecontainer"

blobs = list_blobs(container_name, connection_string)
for blob in blobs:
    print(blob.name)
```

#### Explanation:
- `list_blobs` function connects to the Azure Blob Storage container using the provided connection string and lists all blobs in the specified container.

### Archiving Old Blobs

To archive blobs that are older than a specified number of days from the source container to a destination container, use the following script:

```python
from data_archival import archive_old_blobs

connection_string = "<your_connection_string>"
source_container_name = "sourcecontainer"
destination_container_name = "archivecontainer"

# Archive blobs older than 30 days
archive_old_blobs(source_container_name, destination_container_name, 30, connection_string)
```

#### Explanation:
- `archive_old_blobs` function moves blobs older than the specified number of days (`30` in this case) from the source container to the destination container.
- `source_container_name` is the name of the container from which blobs will be moved.
- `destination_container_name` is the name of the container to which blobs will be moved.
- `days_old` parameter specifies the age of the blobs to be archived.

### Deleting Old Blobs

To delete blobs that are older than a specified number of days from a container, use the following script:

```python
from data_archival import delete_old_blobs

connection_string = "<your_connection_string>"
container_name = "archivecontainer"

# Delete blobs older than 60 days
delete_old_blobs(container_name, 60, connection_string)
```

#### Explanation:
- `delete_old_blobs` function deletes blobs older than the specified number of days (`60` in this case) from the specified container.
- `container_name` is the name of the container from which blobs will be deleted.
- `days_old` parameter specifies the age of the blobs to be deleted.

## Examples

Here are a few usage scenarios to illustrate how to use the scripts:

### Example 1: Listing Blobs

This example demonstrates how to list all blobs in a container named "mycontainer":

```python
from data_archival import list_blobs

connection_string = "your_connection_string_here"
container_name = "mycontainer"

blobs = list_blobs(container_name, connection_string)
for blob in blobs:
    print(blob.name)
```

### Example 2: Archiving Blobs Older Than 7 Days

This example shows how to move blobs older than 7 days from "sourcecontainer" to "archivecontainer":

```python
from data_archival import archive_old_blobs

connection_string = "your_connection_string_here"
source_container_name = "sourcecontainer"
destination_container_name = "archivecontainer"

# Archive blobs older than 7 days
archive_old_blobs(source_container_name, destination_container_name, 7, connection_string)
```

### Example 3: Deleting Blobs Older Than 90 Days

This example demonstrates how to delete blobs older than 90 days from the "archivecontainer":

```python
from data_archival import delete_old_blobs

connection_string = "your_connection_string_here"
container_name = "archivecontainer"

# Delete blobs older than 90 days
delete_old_blobs(container_name, 90, connection_string)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
