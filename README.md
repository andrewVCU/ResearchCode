### YungSlug Research Scripts

- **BlastFilter**
  A Python script that takes a protein fasta, a blast output file, and an organism name, and returns a filtered version of 
  the blast output. The protein fasta file is used to filter out the self hits. Filtering criteria is set to E value <= 1.0E-7
  and percent identity >= 30.00%.
  
  **Usage:** BlastFilter.py <proteins.fa> <blast.out> <organism_name>
  
  **Sample Commandline Run:**
    
    ```console
    ======================
    B L A S T  F I L T E R
    ======================
    Blast File:    D:\IndependentStudy\Scripts\YungSlug\YSblast_AllHits_Mar14.out
    Protein Fasta: D:\IndependentStudy\Scripts\YungSlug\YungSlug_proteins.fasta
    Organism:      YungSlug

    ---------------------------------------------
    Running pullProtIDs on: D:\IndependentStudy\Scripts\YungSlug\YungSlug_proteins.fasta
    ---------------------------------------------

    Pulling Protein IDs: 100%

    Self Protein IDs Pulled

    ---------------------------------------------
    Running blastFilter on: D:\IndependentStudy\Scripts\YungSlug\YungSlug_proteins.fasta
    ---------------------------------------------

    Filtering: 99%

    Blast Filtered
    ```
    
- **BatchEntrezTrim**
  This is a script that parses through a summary file output of batch entrez in order to obtain the taxonomy string from a 
  given accession number. It will then append the blast file that is given as input with the taxonomy string in the final column
  
  **Usage:** python BatchEntrezTrim.py <Entrez.out> <FilteredBlast.out> <Out_File_Name> 
 
- **TopVirusAndBacterialHits**
  This script sorts through the output file from BatchEntrezTrim and returns a file that has the top hit labeled as virus and top hit 
  labeled as bacteria, per protein sequence. For each sequence there is a viral and bacterial hit. 
  
  **Usage:** No usage as of now. Files are given to the script from the editor or IDE.

  **SharedHits.py**
  This script takes two Blast output files and currates a list of shared hits between the two files with the corresponding query numbers from both files.  

  **Usage:** python SharedHits.py --file1 <FirstBlastFile.out> --file2 <SecondBlastFile.out> --outfile <Out_File_Name>

  **Out File Example**
  '''console
    Shared Hits: 94
    Query1	Query2	Match
    YungSlug-final_77	0305phi8-36_ORF087	MBK8467753.1
    YungSlug-final_NlpC/P60	0305phi8-36_ORF147	AYP68591.1
    YungSlug-final_NlpC/P60	0305phi8-36_ORF147	YP_002300361.1
    YungSlug-final_NlpC/P60	0305phi8-36_ORF147	YP_008770021.1
    YungSlug-final_NlpC/P60	0305phi8-36_ORF147	QMV48392.1
    YungSlug-final_NlpC/P60	0305phi8-36_ORF147	QPX71646.1
    .
    .
    .
    .
    .
  '''