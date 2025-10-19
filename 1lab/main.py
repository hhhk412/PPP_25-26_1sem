

if __name__ == "__main__":
    pass # 
grades = [[5,4,3,5,4],[4,3,4,4,3],[5,5,5,4,5],[3,2,3,4,3],[4,4,4,4,4],[5,4,5,5,4],[3,3,2,3,4],[4,5,4,5,5],[2,3,2,3,2],[5,5,4,5,5]]

for i in range(10):
    print(f"Студент {i+1}: {sum(grades[i])/5}")

for j in range(5):
    subject = [grades[i][j] for i in range(10)]
    print(f"Предмет {j+1}: {max(subject)} {min(subject)}")

most = [sum(grades[i])/5 for i in range(10)]
print(f"Лучший: Студент {most.index(max(avgs))+1}")
print(f"Худший: Студент {most.index(min(avgs))+1}")