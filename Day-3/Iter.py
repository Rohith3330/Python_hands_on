class PassingScoreIterator:
    def __init__(self, scores, passing_threshold):
        self.scores = scores
        self.passing_threshold = passing_threshold
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.scores):
            score = self.scores[self.index]
            self.index += 1
            if score >= self.passing_threshold:
                return score 
        raise StopIteration

# Example usage:
scores = [85, 60, 75, 90, 55, 65]
passing_threshold = 70

passing_scores_iterator = PassingScoreIterator(scores, passing_threshold)

for score in passing_scores_iterator:
    print(score)
