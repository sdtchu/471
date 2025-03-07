from constraint import MinConflictsSolver


class CustomMinConflictsSolver(MinConflictsSolver):
    '''
    This is a subclass of the MinConflictsSolver that implements the getSolutions method.
    It does not need to be modified
    '''
    def getSolutions(self, domains, constraints, vconstraints)->list:
        s=super().getSolution(domains, constraints, vconstraints)
        if s is None:
            return []
        return [s]