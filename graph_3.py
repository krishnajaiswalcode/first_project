import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
study_scores = [50, 55, 65, 70, 75, 80, 85, 90, 95, 100]
plt.figure(figsize=(10, 5))
plt.scatter(study_hours, study_scores, color='blue', label='Scores')
plt.plot(study_hours, study_scores, color='red', label='Trend Line')
plt.plot(study_hours, study_scores)
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Score')
plt.grid()
plt.show()