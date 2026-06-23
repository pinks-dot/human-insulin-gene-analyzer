# HUMAN INSULIN GENE ANALYZER

file = open("insulin_gene.txt", "r")
sequence = file.read().replace("\n", "")
file.close()

print("===========================")
print("HUMAN INSULIN GENE ANALYZER")
print("===========================")
print()

print("Insulin Gene Sequence:")
print(sequence[:100] + "...")
print()

print("Gene Length:", len(sequence))
print()

print("A:", sequence.count("A"))
print("T:", sequence.count("T"))
print("G:", sequence.count("G"))
print("C:", sequence.count("C"))
print()


gc = sequence.count("G") + sequence.count("C")
gc_content = gc / len(sequence) * 100
print("GC Content:", round(gc_content, 2), "%")

at = sequence.count("A") + sequence.count("T")
at_content = at / len(sequence) * 100
print("AT Content:", round(at_content, 2), "%")

start_codon = sequence.count("ATG")
print("Start Codons (ATG):", start_codon)

reverse_sequence = sequence[::-1]
print()
print("Reverse Sequence:")
print(reverse_sequence[:80], "...")
