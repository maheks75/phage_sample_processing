{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bef43a52-15b4-4df9-bd40-c58a019d0003",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Bio import SeqIO\n",
    "\n",
    "seq_count = {}\n",
    "\n",
    "with open('sorted_sheep_heavylight.txt', 'w') as file:\n",
    "    for i, record in enumerate(SeqIO.parse('mereged_partial.assembled.fastq', 'fastq')):\n",
    "        seq_data = str(record.seq)\n",
    "        print(seq_data)    \n",
    "        if seq_data in seq_count:\n",
    "            seq_count[seq_data] += 1\n",
    "        else:\n",
    "            seq_count[seq_data] = 1\n",
    "    sorted_seq_count = sorted(seq_count.items(), key=lambda x: x[1], reverse=True)\n",
    "    for key, value in sorted_seq_count:\n",
    "        file.write(f'{key}:{value}\\n')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
