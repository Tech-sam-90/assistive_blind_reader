import matplotlib.pyplot as plt

# Example data
word_counts = [67, 136, 200, 342]
ocr_times = [3.21, 10.42, 4.16, 4.31]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(word_counts, ocr_times, color='blue')

# Add titles and labels
plt.title('OCR Time Across Various Word Counts')
plt.xlabel('Word Count')
plt.ylabel('OCR Time (seconds)')

# Display the plot
plt.show()
