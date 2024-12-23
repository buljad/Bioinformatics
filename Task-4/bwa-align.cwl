cwlVersion: v1.0
class: CommandLineTool
baseCommand: bwa
arguments:
  - mem
inputs:
  ref_genome:
    type: File
    inputBinding:
      position: 1
  read1:
    type: File
    inputBinding:
      position: 2
  read2:
    type: File
    inputBinding:
      position: 3
outputs:
  output_sam:
    type: File
    outputBinding:
      glob: output.sam
stdout: output.sam
