class MyManager:
    def __enter__(self):
        print("Enter method")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit method")

with MyManager():
    print('Something inside my context manager')



