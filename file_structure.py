
import os

# Define folder structure
folders = ['data_stream', 'data_processing', 'batch_processing', 'data_storage', 'visualization']

# Loop through folders and create them if they don't exist
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f'Created folder: {folder}')

# Create empty files in each folder
for folder in folders:
    for i in range(5):
        filename = f'{folder}/file_{i}.txt'
        with open(filename, 'w') as f:
            f.write('')
            print(f'Created empty file: {filename}')
