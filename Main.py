
import random 
import tkinter as tk
import os 

topics = ["Artificial intelligence", "Climate change", "Cybersecurity", "Remote work", "Digital privacy", "Misinformation", "Social media", "Inflation", "Cryptocurrency", "Automation", "Mental health", "Burnout", "Sustainable fashion", "Fast fashion", "Digital nomads", "Influencer culture", "Algorithms", "Deepfakes", "Electric vehicles", "Renewable energy", "Space exploration", "Genetic engineering", "Virtual reality", "Augmented reality", "Online education", "Freelancing", "Gig economy", "E-commerce", "Web scraping", "Open-source software", "Data privacy", "Facial recognition", "Robotics", "3D printing", "Cybercrime", "Online communities", "Parasocial relationships", "Doomscrolling", "Digital minimalism", "Creator economy", "Meme culture", "Internet slang", "Cancel culture", "Political polarization", "Globalization", "Urbanization", "Overconsumption", "Minimalism", "Sustainable living", "Loneliness",]
question_prompt = [ "Your word is:    ", ]



 
def click(): 
  chosen_topic = random.choice(topics)
  chosen_prompt = random.choice(question_prompt)
  result.config(text=f"{chosen_prompt} {chosen_topic}")



root = tk.Tk()
root.geometry ("600x600")
root.title("Impromptu")
root.config(bg= "#6B8A8A")


result = tk.Label(
    root,
    text="Ready..",
    font=("Times New Roman", 45),
    bg="#6B8A8A",
    fg="white",
    wraplength=450
)

result.pack(pady=20 , padx= 30)


button = tk.Button(
 root, 
 text = "Spinner",
 command = click,
 font = ("Georgia", 30),
 justify = "left",
 
 )

button.place(x=200, y= 300)

  



 
  




root.mainloop()
