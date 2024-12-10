import os

file_path="C:\Users\USER\OneDrive\Desktop\TRIAL"

def load_performance(file_path):
    #Load performance data from file, return None if file doesn't exist/invalid
    if not os.path.exists(file_path):
        return None
        
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    
    if len(lines) < 3:
        return None
    
    data = {}
    for line in lines:
        parts = line.strip().split(":")
        if len(parts) != 2:
            return None
        key = parts[0].strip()
        value = int(parts[1])
        data[key] = value
    
    required_keys = ["success_count", "failure_count", "total_guesses"]
    for key in required_keys:
        if key not in data:
            return None
            
    return data

def save_performance(file_path, performance_data):
    """Save performance data, return True if successful, False otherwise"""
    if not performance_data:
        return False
        
    file = open(file_path, 'w')
    file.write(f"success_count: {performance_data['success_count']}\n")
    file.write(f"failure_count: {performance_data['failure_count']}\n")
    file.write(f"total_guesses: {performance_data['total_guesses']}\n")
    file.close()
    return True
