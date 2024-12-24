from Bio import SeqIO

seq_count = {}

with open('sorted_sheep_heavylight.txt', 'w') as file:
    for i, record in enumerate(SeqIO.parse('mereged_partial.assembled.fastq', 'fastq')):
        seq_data = str(record.seq)
        print(seq_data)
        if seq_data in seq_count:
            seq_count[seq_data] += 1
        else:
            seq_count[seq_data] = 1
    sorted_seq_count = sorted(seq_count.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_seq_count:
        file.write(f'{key}:{value}\n')

