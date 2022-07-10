# ukwiki-kenlm

Instruction about building a KenLM model based on Ukrainian Wikipedia data

## Install

You need Python 3 and pip for text processing.

### Libraries

```bash
pip install mwxml
```

## Steps

### Step 1: Found the latest backup snapshot

Go to https://dumps.wikimedia.org/backup-index.html and find the "ukwiki: Dump complete" line. Follow the "ukwiki" link.

### Step 2: Find "Recombine all pages, current versions only." link

On the page, find the "Recombine all pages, current versions only." link and download BZ2 archive.

### Step 3: Uncompress the BZ2 archive

### Step 4: Extract text data from the "*-pages-meta-current.xml" file

```bash
python extract_text_from_dump.py ukwiki-20220701-pages-meta-current.xml > uncleaned_text.txt
```
