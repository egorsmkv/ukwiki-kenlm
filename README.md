# ukwiki-kenlm

Instruction about building a KenLM model based on Ukrainian Wikipedia data

## Install

You need Python 3 and pip for text processing.

### Libraries

```bash
pip install mwxml tqdm
```

## Steps

### Step 1: Find the latest backup for Ukrainian Wikipedia data

Go to https://dumps.wikimedia.org/backup-index.html and find the "ukwiki: Dump complete" line. Follow the "ukwiki" link.

### Step 2: Find "Recombine all pages, current versions only." link

On the page, find the "Recombine all pages, current versions only." link and download BZ2 archive.

### Step 3: Uncompress the BZ2 archive

### Step 4: Extract text data from the "*-pages-meta-current.xml" file

```bash
python extract_text_from_dump.py ukwiki-20220701-pages-meta-current.xml > uncleaned_text.txt
```

### Step 5: Clean `uncleaned_text.txt` file

```bash
python cleaner.py --corpus-path uncleaned_text.txt --corpus-clean cleaned_text.txt --n-workers 5 --min-words 2
```

### Step 6: Install KenLM

```bash
sudo apt install build-essential cmake libboost-system-dev libboost-thread-dev libboost-program-options-dev libboost-test-dev libeigen3-dev zlib1g-dev libbz2-dev liblzma-dev

wget -O - https://kheafield.com/code/kenlm.tar.gz | tar xz

mkdir kenlm/build && cd kenlm/build && cmake .. && make -j2
```

### Step 7: Build a KenLM in the ARPA format

```bash
kenlm/build/bin/lmplz -o 5 < "cleaned_text.txt" > "uk_wiki.arpa"
```

### Step 8: Fix a KenLM model

```bash
python fix_kenlm.py --arpa-file-in uk_wiki.arpa --arpa-file-out uk_wiki_corrected.arpa
```

### Step 9: Build a KenLM in the binary format

```bash
kenlm/build/bin/build_binary uk_wiki_corrected.arpa uk_wiki_corrected.bin
```
