import numpy as np
import unittest

from Selection import Selection

class TestSelection(unittest.TestCase):
    def setUp(self):
        # Generate random population for 100 instances
        np.random.seed(42)
        self.population = np.random.randint(1, 10, size=(100, 3)).tolist()

        # Generate fitness scores such that the last two instances have the lowest scores
        self.fitness_scores = [0.5] * 98 + [0.1, 0.2]

        # Create a Selection object
        num_parents = 2
        target_class = 0
        population_size = 100
        predict_fn = lambda instance: 0  # Mock predict_fn for testing
        self.selection = Selection(num_parents, target_class, population_size, predict_fn)

    def test_select_elites(self):
        # Set parallel to False to test serial execution
        self.selection.parallel = False
        
        # Run the selection
        elites = self.selection.select_elites(self.population, self.fitness_scores)
        
        # Assert that the elites were selected correctly
        self.assertEqual(len(elites), 10)  # Since population size is 100, we expect 10 elites

    def test_select_parallel(self):
        # Set parallel to True to test parallel execution
        self.selection.parallel = True
        
        # Run the selection
        elites = self.selection.select_elites(self.population, self.fitness_scores)
        
        # Assert that the elites were selected correctly
        self.assertEqual(len(elites), 10)  # Since population size is 100, we expect 10 elites

    def test_select_parents(self):
        # Set parallel to False to test serial execution
        self.selection.parallel = False
        
        # Run the selection
        parents = self.selection.select_parents(self.population, self.fitness_scores)
        
        # Assert that the parents were selected correctly
        self.assertEqual(len(parents), 2)  # Since num_parents is 2, we expect 2 parents
        self.assertEqual(parents, self.population[-2:])  # The last two instances should be selected as parents

    def test_select_parents_parallel(self):
        # Set parallel to True to test parallel execution
        self.selection.parallel = True
        
        # Run the selection
        parents = self.selection.select_parents(self.population, self.fitness_scores)
        
        # Assert that the parents were selected correctly
        self.assertEqual(len(parents), 2)  # Since num_parents is 2, we expect 2 parents
        self.assertEqual(parents, self.population[-2:])  # The last two instances should be selected as parents

if __name__ == "__main__":
    unittest.main()
