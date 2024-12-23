cwlVersion: v1.0
class: Workflow
inputs:
  ref_genome: File
  read1: File
  read2: File
outputs:
  flagstat_output:
    type: File
    outputSource: flagstat/output_flagstat
steps:
  align:
    run: bwa-align.cwl
    in:
      ref_genome: ref_genome
      read1: read1
      read2: read2
    out: [output_sam]
  flagstat:
    run: samtools-flagstat.cwl
    in:
      input_bam: align/output_sam
    out: [output_flagstat]
