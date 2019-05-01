# GENOME-SEQUENCING
 This project is developed mainly using Python and MySQL.
 It is a Gene Sequence Detector.
 
 First of all, a python GUI is created using Tkinter which provides facility to the user to upload a Fasta File(contains a large no. of gene sequences) named as EcoliGeneSequences.txt here in this project. If it is not a Fasta File,it will display an error showing the message "Not a fasta file!!"
 
# FOLLOWING CODITIONS WERE CHECKED FOR THE FILE TO BE A VALID FASTA FILE
 </br> 1.The information line starts with a ‘>’ symbol only.
 </br> 2.The information is contained in one single line and is not continued to the next line.
 </br> 3.There is no blank line between information line and gene sequence.
 </br> 4.The gene sequence contains only 4 characters ‘A’, ‘T’, ‘G’ and ‘C’.
 
 After the validation of the fasta file is done,We have stored informations in the database by comparing the file with another file named "GeneDetails.txt".
 
</br>The information that should be contained in the database are:
        Sl_No, Gene Information, Gene sequence, Count_A, Count_T, Count_G, Count_C, length, (G+C)%.
where, (G+C)% is calculated as:
  </br>(G+C)% = (Count_G +  Count_C) / (Count_A + Count_T+ Count_G+ Count_C)*100
  
  # SCREENSHOTS OF THE OUTPUT
  
  1.TKINTER GUI
  
  ![Screenshot (2708)](https://user-images.githubusercontent.com/40006730/57037117-f50fc100-6c73-11e9-8564-d8bcfb673a04.png)
  2.CONTENT OF THE DATABASE

![records](https://user-images.githubusercontent.com/40006730/57037119-f6d98480-6c73-11e9-9800-ebb2dbe26c30.png)
