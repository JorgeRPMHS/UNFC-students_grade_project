import pandas as pd

def calculate_stats(file_name):
    
    data = pd.read_csv(file_name)
    data["Pass/Fail"] = data["Grade"].apply(lambda x: "Pass" if x > 50 else "Fail")
    avg = data["Grade"].mean()
    count = len(data)
    print(data[["First Name", "Last Name", "Grade", "Pass/Fail"]])
    return avg, count

if __name__ == "__main__":
    avg, count = calculate_stats("grades.csv")
    print(f"The average grade is {avg}")
    print(f"Total students {count}")