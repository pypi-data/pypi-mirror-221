class frequenciesOfItems:
    def __init__(self, transactional_db, separator='\t'):
        self.transactional_db = transactional_db
        self.separator = separator

    def getFrequencies(self):
        item_freq_dict = {}

        # Read the transactional database and calculate item frequencies
        with open(self.transactional_db, 'r') as f:
            for line in f:
                items = line.strip().split(self.separator)
                for item in items:
                    if item in item_freq_dict:
                        item_freq_dict[item] += 1
                    else:
                        item_freq_dict[item] = 1

        return item_freq_dict