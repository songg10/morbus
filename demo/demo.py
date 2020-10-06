def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"
#________________________________________________________________________________________
def print_list(list, size):
	for i in range(size):
		print(list[i], end =' ')
	print()

def check_atom(command):
	for i in range(1, len(command)):
			if not is_atom(command[i]):
				print("\"", command[i], "\" is not a valid atom")
				return i
	return 0

def read_atom(command, atoms):
	for i in range(1, len(command)):
		if command[i] in atoms:
			print("atom \"", command[i], "\" already known to be true")
		else:
			atoms.add(command[i])
			print("\"", command[i], "\" added to KB")
	return

def read_kb(command, rules):
	try:
		with open(command[1], 'r') as f:
			count = 0
			for read_data in f:
				data_module = read_data.split()
				if len(data_module) <= 1:
					return False
				for even in range(0, len(data_module), 2):
					if not is_atom(data_module[even]):
						return False
				for odd in range(1, len(data_module), 2):
					if odd == 1:
						if data_module[odd] != "<--":
							return False
					else:
						if data_module[odd] != "&":
							return False

				rules[data_module[0]] = set()
				for i in range(1, len(data_module)):
					if is_atom(data_module[i]):
						rules[data_module[0]].add(data_module[i])
				print(read_data, end='')
				count += 1
			print(count, "new rule(s) added")
	except FileNotFoundError:
		return False
	return True

def infer_all(atoms, rules):
	inference = set()
	count = 0
	while count < len(list(rules)):
		i = list(rules)[count]
		if i not in inference and i not in atoms:
			if (rules[i] & (inference | atoms)) == rules[i]:
				inference.add(i)
				count = -1
		count += 1
	return inference

def print_options():
	print("This is a python interpreter of a knowledge based system.")
	print("Here are the options:")
	print("1.load \"filename.txt\": Import the rules for the knowledge based system from the \"filename.txt\".")
	print("2.tell atom_1 atom_2 ... atom_n: Add atoms to the current knowledge based system.")
	print("3.infer_all: Prints all the atoms that can currently be inferred by the rules in the KB.\n*Note that no atoms can be inferred until at least one tell command is called.")
	print("4.clear_atoms: Clear all the atoms of the current KB.")
	print("5.exit: Exit the interpreter.")
	print("________________________________________________________________________________\n")

def init_interpreter():
	atoms = set()
	rules = dict()
	#print_options()
	while True:
		command = input("kb> ").split()
		if len(command) < 1:
			print("Please specify a command\n")
			continue

		if command[0] == "load":
			if len(command) == 1:
				print("Error: \"load\" needs at least one file. Please specify the KB file to read\n")
				continue
			if not read_kb(command, rules):
				print("Error: ", "\"", command[1], "\" is not a valid knowledge base\n")
			print()

		elif command[0] == "tell":
			if len(command) == 1:
				print("Error: \"tell\" needs at least one atom\n")
				continue
			if check_atom(command) != 0:
				continue
			read_atom(command, atoms)
			print()
				
		elif command[0] =="infer_all":
			if len(atoms) == 0:
				print("Can't infer any atom since there are no atoms in the KB(no valid \"tell\" calls have been made\n")
				continue
			inference = infer_all(atoms, rules)
			print("Newly inferred items:")
			if (len(inference) > 0):
				print_list(sorted(inference), len(sorted(inference)))
			else:
				print("<None>")
			print("Atoms already known to be true:")
			print_list(sorted(atoms), len(sorted(atoms)))
			atoms = atoms | inference
			print()

		elif command[0] =="exit":
			break

		elif command[0] == "clear_atoms":
			atoms.clear()
			print("All atoms are cleared from the KB\n")

		else:
			print("Error: unknown command \"", command[0], "\"\n")
			print()
			continue


if __name__ == "__main__":
	init_interpreter()