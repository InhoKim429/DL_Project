import numpy as np


class GraphList(object):
    def __init__(self, matrix_path, train_path, test_path, validation = 0.1):
        self.matrix_path = matrix_path
        self.train_path  = train_path
        self.test_path   = test_path
        self.validation  = validation
        self.graph       = np.load(matrix_path)
        self.train_index = self.read_datasheet(train_path)
        self.test_index  = self.read_datasheet(test_path)

    def read_datasheet(self, file_path):
        path = file_path.split("/")
        file = open(file_path, "r")
        line_index = 1
        line = file.readline()

        if path[2] == "train.txt":
            train_index = []
            while line:
                item = line.split(" ")
                train_index.append((int(item[0]), int(item[1].split('\n')[0])))
                line = file.readline()
                line_index += 1

            return train_index

        elif path[2] == "test.txt":
            test_index = []
            while line:
                item = line.split(" ")
                test_index.append(int(item[0].split('\n')[0]))
                line = file.readline()
                line_index += 1

            return test_index

    def make_dataset(self):
        dataset       = []
        test_dataset  = []
        for index, label in self.train_index:
            dataset.append((self.graph[index], label))

        for index in self.test_index:
            test_dataset.append(self.graph[index])
            
        np.random.shuffle(dataset)
        train_dataset = dataset[:int((1-self.validation)*len(dataset))]
        valid_dataset = dataset[int((1-self.validation)*len(dataset)):]
        
        return train_dataset, valid_dataset, test_dataset