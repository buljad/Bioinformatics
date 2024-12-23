cwlVersion: v1.0
class: CommandLineTool
baseCommand: samtools
arguments:
  - flagstat
inputs:
  input_bam:
    type: File
    inputBinding:
      position: 1
outputs:
  output_flagstat:
    type: stdout
stdout: output.txt

