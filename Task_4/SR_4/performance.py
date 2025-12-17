from abc import ABC, abstractmethod

class Performance(ABC):
    def __init__(self, subjects, scores):
        self.subjects = subjects
        self.scores = scores

    @abstractmethod
    def calculate_average_score(self):
        pass

class DesiredPerformance(Performance):
    def __init__(self, subjects, scores, desired_avg):
        super().__init__(subjects, scores)
        self.desired_avg = desired_avg

    def calculate_average_score(self):
        # Повертає бажаний середній бал
        return self.desired_avg