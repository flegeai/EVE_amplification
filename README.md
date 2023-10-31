# EVE_amplification
code and data for EVE local DNA amplification in the parasitoid wasp *Hyposoter didymator*

So far, it includes 2 notebooks and 1 script:

## Notebooks:
- Count_tables.ipynb: notebook for generating tables of coverage (in FPKM) from counts for each locus (evREP, proviral segments and random loci). It generates as well figure 2 and 3.
- RU_grap.ipynb: notebook for generating RU amplification plots, with locus in red and other regions inblack

## Scripts: 
- bigwig_ratio.py: python scripts for calculating ratio of coverage between St3 abd St1 at each genome position by 10bp bins.

## data
-counts: Raw counts (number of reads) values obtained for each locus (evREP, proviral segments and random loci) at each stage (St1, St3) and at each condition GFP ou U16), obtained with FeatureCounts
-coverage: ratio of coverage between Stage 3 and Stage 3 in bigwig format
-flagstat: various metrics of reads alignments
-regions: GTF file summarizing the position of each locus (and corresponding groups if relevant)
