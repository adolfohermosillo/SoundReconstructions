def get_cor_sets(file):
	file = open(file,'r')
	correspondance_sets = []
	for i in file:
		line = i.split()
		correspondance_sets.append(line)
	return correspondance_sets

def get_sounds(correspondance_sets):
	sound_inventory = []
	correspondance_sets = correspondance_sets[1:]
	for gloss_set in correspondance_sets:
		for word in gloss_set:
			for ch in word:
				if ch not in sound_inventory and ch != '-':
					sound_inventory.append(ch)
	return sorted(sound_inventory)


def group_by_sounds(correspondance_sets, sound_inventory):
	languages = correspondance_sets[0]
	correspondance_sets = correspondance_sets[1:]
	for sound in sound_inventory:
		print(sound)
		print(languages)
		for word_sets in correspondance_sets:
			sound_present = False
			for word in word_sets:
				if sound in word:
					sound_present = True
			if sound_present: 
				print(word_sets)
		print()

if __name__ == "__main__":
  correspondance_sets = get_cor_sets('words.txt')
  sound_inventory = get_sounds(correspondance_sets)
  group_by_sounds(correspondance_sets, sound_inventory)
