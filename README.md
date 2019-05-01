# GENOME-SEQUENCING
 This project is developed mainly using Python and MySQL.
 It is a Gene Sequence Detector.
 
 First of all, a python GUI is created using Tkinter which provides facility to the user to upload a Fasta File(contains a large no. of gene sequences) named as EcoliGeneSequences.txt here in this project. If it is not a Fasta File,it will display an error showing the message "Not a fasta file!!"
 
# FOLLOWING CODITIONS WERE CHECKED FOR THE FILE TO BE A VALID FASTA FILE
 1.The information line starts with a ‘>’ symbol only.
 2.The information is contained in one single line and is not continued to the next line.
 3.There is no blank line between information line and gene sequence.
 4.The gene sequence contains only 4 characters ‘A’, ‘T’, ‘G’ and ‘C’.
 
 After the validation of the fasta file is done,We have stored informations in the database by comparing the file with another file named "GeneDetails.txt".
 
The information that should be contained in the database are:
        Sl_No, Gene Information, Gene sequence, Count_A, Count_T, Count_G, Count_C, length, (G+C)%.
where, (G+C)% is calculated as:
  (G+C)% = (Count_G +  Count_C) / (Count_A + Count_T+ Count_G+ Count_C)*100
  
  # SCREENSHOTS OF THE OUTPUT
  
  1.TKINTER GUI
  
  
  2.CONTENT OF THE DATABASE

