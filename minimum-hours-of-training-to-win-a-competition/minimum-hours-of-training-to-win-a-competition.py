from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]):
        # iterate through energy
        energyTrainingHours = 0
        experienceTrainingHours = 0
        for enemyEnergy in energy:
            if initialEnergy <= enemyEnergy:
                # increase energyTrainingHours
                # add just enough so that initialEnergy can work enxt round
                energyTrainingHours += (enemyEnergy - initialEnergy + 1)
                initialEnergy = 1
            else:
                initialEnergy -= enemyEnergy
        for enemyExperience in experience: 
            if initialExperience <= enemyExperience: 
                if enemyExperience - initialExperience + 1 > experienceTrainingHours: 
                    experienceTrainingHours = enemyExperience - initialExperience + 1
                initialExperience += enemyExperience
            else: 
                initialExperience += enemyExperience
        return energyTrainingHours + (experienceTrainingHours)


driver = Solution()
print(driver.minNumberOfHours(1, 1, [1, 1, 1, 1], [1, 1, 1, 50]))
