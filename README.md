# GitTar

GitTar is a simple backup utility for creating and extracting incremental backups of your directories. It uses `tar` utility for backup creation and extraction and `gzip` for compression. Incremental backups enable you to store only the changes made since the last backup, saving storage space and improving efficiency.

## Installation

Before using GitTar, make sure Python 3.6 or later and pip are installed in your system. You can install required packages using:

```bash
pip install -r requirements.txt
```

## Configuration

To configure GitTar, create a `.env` file in the same directory as the scripts and set the following variables:

```
SOURCE_DIR=<your-source-directory>
BACKUP_DIR=<your-backup-directory>
EXTRACT_DIR=<your-extraction-directory>
```

- `SOURCE_DIR` is the directory you want to backup.
- `BACKUP_DIR` is the directory where the backup file will be stored.
- `EXTRACT_DIR` is the directory where the backup will be extracted.

## Usage

To create a backup, run the `gittar_create.py` script:

```bash
python3 gittar_create.py
```

To extract a backup, run the `gittar_extract.py` script:

```bash
python3 gittar_extract.py
```

Both scripts also support the `-f` flag for full backups or extractions. For `gittar_create.py`, if `-f` flag is passed, it will create a new snapshot file and a full backup. For `gittar_extract.py`, if `-f` flag is passed, it will only extract on a clean folder.

```bash
python3 gittar_create.py -f
python3 gittar_extract.py -f
```

## License

GitTar is released under the MIT license. See `LICENSE` for more information.