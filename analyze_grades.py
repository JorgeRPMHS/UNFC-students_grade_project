import pandas as pd

def calculate_stats(file_name):
    
    data = pd.read_csv(file_name)
    avg = data["Grade"].mean()
    count = len(data)
    return avg, count

if __name__ == "__main__":
    avg, count = calculate_stats("grades.csv")
    print(f"The average grade is {avg}")
    print(f"Total students {count}")