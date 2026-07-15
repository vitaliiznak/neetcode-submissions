class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations.
        
        Core Idea (very simple):
        - To create a permutation, we pick ANY number to put in FRONT.
        - Then we recursively find all permutations of the remaining numbers.
        - We do this for EVERY number (so we try all possibilities).
        """
        
        def get_all_possible_arrangements(numbers_we_can_still_use: List[int]) -> List[List[int]]:
            """
            Recursively generates every possible ordering of the given numbers.
            """
            
            # Base case: No numbers left → only one empty arrangement exists
            if not numbers_we_can_still_use:
                return [[]]
            
     
            
            # ============================================================
            # KEY PART: We try EVERY number as the one to put in front
            # ============================================================
            all_perm = []
            for i, num_to_put in enumerate(numbers_we_can_still_use):
                rest = ( 
                    numbers_we_can_still_use[:i] + numbers_we_can_still_use[i+1:]
                )
                perm_rest = get_all_possible_arrangements(rest)
               
                for perm in perm_rest:
                    all_perm.append( [num_to_put] + perm)

            return all_perm

                
            
        
        return get_all_possible_arrangements(nums)