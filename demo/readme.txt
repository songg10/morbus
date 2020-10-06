The KB is basically an expert system trying to automatically diagnose the illness/disease/condition of the patient according to the patient's symptoms. As the description may have suggested, this KB will be useful for medical implementation of expert system. The rules were created based on the symptoms listed on Centers for Disease Control and Prevention (CDC).


Here are some commands that you can use to run my interpreter:
- load someKB.txt: This loads into memory the KB stored in the file someKB.txt
- tell atom_1 atom_2 ... atom_n: This adds the atoms atom_1 to atom_n to the current KB
- infer_all: Prints all the atoms that can currently be inferred by the rules in the KB. Note that no atoms can be inferred until at least one tell command is called

Example run:

kb> load a4_q2_kb.txt
21 new rule(s) added

kb> tell fever
" fever " added to KB

kb> infer_all
Newly inferred items:
<None>
Atoms already known to be true:
fever 

kb> tell coughing hard_to_breath pneumonia fatigue
" coughing " added to KB
" hard_to_breath " added to KB
" pneumonia " added to KB
" fatigue " added to KB

kb> tell coughing
atom " coughing " already known to be true

kb> infer_all
Newly inferred items:
asthma corona_virus lower_respiratory_infection 
Atoms already known to be true:
coughing fatigue fever hard_to_breath pneumonia 

kb> exit

