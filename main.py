import os
import requests
from tqdm import tqdm

url = 'https://storage.googleapis.com/tf-datasets/tfds-goemotions/v1.0.2/downloads/summarized.csv.gz'
filename = 'goemotions.csv.gz'

# Check if the file already exists
if not os.path.exists(filename):
    # Download the file with progress bar
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    # Check if the download was successful
    if total_size != 0 and progress_bar.n != total_size:
        print('Error: Failed to download the file')
        os.remove(filename)
else:
    print(f'The file {filename} already exists')
