# Adjusting the issue with indexing when calculating mid_angle

import matplotlib.pyplot as plt
import numpy as np

# Create a polar plot to mimic the circular schedule
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6,6))

# Hours of the day
hours = np.linspace(0, 2 * np.pi, 25)  # 24 hours

# Corresponding labels for the hours
labels = [
    '12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', 
    '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', 
    '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM', '12 AM'
]

# Custom activity blocks (adjust to your needs)
activities = [
    (0, 6, 'Dreamland'),
    (6, 7, 'Morning'),
    (7, 10, 'Gaming'),
    (10, 12, 'Makan Siang'),
    (12, 14, 'Gaming'),
    (14, 16, 'Exercise'),
    (16, 18, 'Play'),
    (18, 19, 'Comics'),
    (19, 24, 'Chill Time')
]

# Define colors for each activity
colors = ['#F4E1D2', '#FFC1C1', '#FFDEAD', '#90EE90', '#ADD8E6', '#FFB6C1', '#DDA0DD', '#FFFACD', '#E6E6FA']

# Plot each activity as a wedge in the circle with corresponding colors
for i, (start, end, label) in enumerate(activities):
    ax.fill_between(hours[start:end+1], 0, 1, label=label, color=colors[i], alpha=0.6)
    
    # Add titles inside each wedge
    mid_angle = (start + end) / 2  # Position the text at the middle of each wedge
    ax.text((hours[int(mid_angle)]), 0.5, label, color="black", fontsize=10, ha='center', va='center')

# Add the labels around the outer circle
ax.set_xticks(hours)
ax.set_xticklabels(labels, fontsize=8)

# Title and remove radial gridlines for cleaner look
ax.set_title('Daily Schedule of Bae Seok-Ryu', va='bottom', fontsize=14)
ax.grid(False)

# Adding the legend inside the pie chart
# ax.legend(loc='center', title="Activities")

# Show plot
plt.show()
