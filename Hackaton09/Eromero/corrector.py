import os

migrations_dir = './migrations'
migration_files = os.listdir(migrations_dir)
sorted_migration_files = sorted(migration_files)

for i, file_name in enumerate(sorted_migration_files, 1):
    new_file_name = f'2023_05_06_{i:04}_{file_name}'
    os.rename(os.path.join(migrations_dir, file_name), os.path.join(migrations_dir, new_file_name))
    print(f'Renamed {file_name} to {new_file_name}')
