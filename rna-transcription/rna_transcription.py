def to_rna(dna_strand):
    
    DNA = {"A": "U", 
           "C": "G", 
           "G": "C",
           "T": "A"}
    
    if not dna_strand:
        return ""

    RNA = []
    for each_DNA_molecule in dna_strand:
        RNA.append(DNA[each_DNA_molecule])
    
    return "".join(RNA)

