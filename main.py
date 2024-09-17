class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression
    
    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    def print_result(self):
        result = self.solve()
        print(f"The result of the expression '{self.expression}' is: {result}")

# Example usage
if __name__ == "__main__":
    expr = input("Enter a mathematical expression: ")
    solver = ExpressionSolver(expr)
    solver.print_result()