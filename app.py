import matplotlib.pyplot as plt
import numpy as np
import random

# Define the activities
activities = [
    "Meditasi", "Solat Dhuha", "Baca Buku", "Nonton Film", "Main Game", 
    "Olahraga", "Belajar Skill Baru", "Makan Siang", 
    "Buat Feed Sosmed", "Ngemil", "Jalan-jalan Santai", 
    "Bersih-bersih Rumah", "Mendengarkan Musik", 
    "Bersantai", "Membaca Artikel", "Mengikuti Kursus Online"
]

# Prayers with fixed times
prayers = {
    "04:00": "Solat Subuh",
    "07:00": "Sarapan",
    "12:00": "Solat Dzuhur",
    "13:00": "Makan Siang",
    "15:00": "Solat Ashar",
    "18:00": "Solat Maghrib",
    "19:00": "Makan Malam",
    "20:00": "Solat Isya"
}

# Convert prayer times to hours for easier plotting
prayer_times = [
    (4, 4.5, "Solat Subuh"),
    (7, 7.5, "Sarapan"),
    (12, 12.5, "Solat Dzuhur"),
    (13, 13.5, "Makan Siang"),
    (15, 15.5, "Solat Ashar"),
    (18, 18.5, "Solat Maghrib"),
    (19, 19.5, "Makan Malam"),
    (20, 20.5, "Solat Isya")
]

# Fixed sleep time from 22:00 to 04:00
sleep_block = (22, 4, "Tidur")

# Generate random start times in 2-hour increments excluding the sleep block
available_times = list(range(4, 22, 2))  # Times start at 4 AM and go up to 10 PM (exclude 10 PM to 4 AM)
random.shuffle(available_times)

# Assign activities to each 2-hour time slot
activity_blocks = []
for i in range(min(len(activities), len(available_times))):
    start_time = available_times[i]
    end_time = start_time + 2  # Each block is 2 hours
    activity_blocks.append((start_time, end_time, activities[i]))

# Create a polar plot to mimic the circular schedule
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7,7))

# Hours of the day (in radians for a 24-hour clock)
hours = np.linspace(0, 2 * np.pi, 25)

# Labels for each hour of the day
labels = [
     '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', 
    '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM','12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', 
    '9 AM', '10 AM', '11 AM', '12 AM'
]

# Combine activities, prayer times, and sleep into a single list for plotting
all_blocks = activity_blocks + prayer_times + [sleep_block]

# Define colors for each activity/prayer (distinct for each)
colors = ['#F4E1D2', '#FFC1C1', '#FFDEAD', '#90EE90', '#ADD8E6', '#FFB6C1', '#DDA0DD', 
          '#FFFACD', '#E6E6FA', '#FAFAD2', '#FFE4E1', '#E0FFFF', '#FFD700', '#C0C0C0',
          '#FA8072', '#98FB98', '#FF6347', '#AFEEEE', '#DA70D6', '#BA55D3']

# Plot each block (both activities, prayers, and sleep) with corresponding colors
for i, (start, end, label) in enumerate(all_blocks):
    if start < end:
        ax.fill_between(hours[int(start):int(end)+1], 0, 1, label=label, color=colors[i % len(colors)], alpha=0.6)
    else:  # For sleep which spans over midnight
        ax.fill_between(hours[int(start):], 0, 1, label=label, color=colors[i % len(colors)], alpha=0.6)
        ax.fill_between(hours[:int(end)+1], 0, 1, label=None, color=colors[i % len(colors)], alpha=0.6)

    # Calculate mid_angle and rotation angle
    mid_angle = (start + (end if end > start else end + 24)) / 2 % 24
    rotation_angle = np.degrees(hours[int(mid_angle)])  # Convert to degrees for text rotation
    alignment = 'center'
    
    # Adjust rotation so that text follows the direction of the wedge
    if rotation_angle > 180:
        rotation_angle += 180
        alignment = 'center'

    # Position text further out to avoid crowding
    ax.text(hours[int(mid_angle)], 0.75, label, color="black", fontsize=8, ha=alignment, va='center', 
            rotation=rotation_angle, rotation_mode='anchor')

# Add the labels around the outer circle
ax.set_xticks(hours)
ax.set_xticklabels(labels, fontsize=8)

# Title and remove radial gridlines for a cleaner look
ax.set_title('Daily Schedule Penggangguran', va='bottom', fontsize=14)
ax.grid(False)
 
# Show the plot
plt.show()
