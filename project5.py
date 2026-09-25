import tkinter as tk
from tkinter import messagebox
import pyttsx3


# ---------------- VOICE ----------------

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("AI Resume & Job Management System")
root.geometry("900x600")
root.config(bg="#eef4f7")


# ---------------- INTRODUCTION ----------------

def show_introduction():

    intro = tk.Toplevel(root)
    intro.title("Introduction")
    intro.geometry("600x450")
    intro.config(bg="lightblue")

    tk.Label(
        intro,
        text="AI Resume & Job Management System",
        font=("Arial", 22, "bold"),
        bg="lightblue"
    ).pack(pady=30)

    tk.Label(
        intro,
        text="Your Personal AI Career Assistant",
        font=("Arial", 14),
        bg="lightblue"
    ).pack()

    tk.Label(
        intro,
        text="Resume Management • Job Management • AI Analysis",
        font=("Arial", 11),
        bg="lightblue"
    ).pack(pady=15)

    tk.Label(
        intro,
        text="Project By: Fareeha",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).pack(pady=10)

    animation = tk.Label(
        intro,
        text="AI Assistant",
        font=("Arial", 18, "bold"),
        bg="lightblue"
    )
    animation.pack(pady=20)

    words = ["AI Assistant", "Resume Assistant", "Job Assistant"]

    def animate(i=0):
        animation.config(text=words[i])
        intro.after(700, animate, (i + 1) % len(words))

    animate()

    def introduction_voice():
        speak(
            "Welcome to AI Resume and Job Management System. "
            "This system helps users manage resumes and jobs."
        )

    tk.Button(
        intro,
        text="VOICE INTRODUCTION",
        command=introduction_voice,
        width=22
    ).pack(pady=10)

    tk.Button(
        intro,
        text="START PROJECT",
        command=intro.destroy,
        width=22
    ).pack(pady=10)


# ---------------- RESUME PAGE ----------------

def resume_page():

    resume = tk.Toplevel(root)
    resume.title("Resume Management")
    resume.geometry("600x600")
    resume.config(bg="white")

    tk.Label(
        resume,
        text="Resume Management",
        font=("Arial", 20, "bold"),
        bg="white"
    ).pack(pady=20)

    tk.Label(resume, text="Full Name", bg="white").pack()
    name_entry = tk.Entry(resume, width=50)
    name_entry.pack(pady=5)

    tk.Label(resume, text="Email", bg="white").pack()
    email_entry = tk.Entry(resume, width=50)
    email_entry.pack(pady=5)

    tk.Label(resume, text="Phone", bg="white").pack()
    phone_entry = tk.Entry(resume, width=50)
    phone_entry.pack(pady=5)

    tk.Label(resume, text="Education", bg="white").pack()
    education_entry = tk.Entry(resume, width=50)
    education_entry.pack(pady=5)

    tk.Label(resume, text="Skills", bg="white").pack()
    skills_entry = tk.Entry(resume, width=50)
    skills_entry.pack(pady=5)

    tk.Label(resume, text="Experience", bg="white").pack()
    experience_entry = tk.Entry(resume, width=50)
    experience_entry.pack(pady=5)

    def save_resume():

        if name_entry.get() == "":
            messagebox.showwarning("Warning", "Please enter your name.")
            return

        file = open("resume.txt", "w")

        file.write("AI RESUME\n\n")
        file.write("Name: " + name_entry.get() + "\n")
        file.write("Email: " + email_entry.get() + "\n")
        file.write("Phone: " + phone_entry.get() + "\n")
        file.write("Education: " + education_entry.get() + "\n")
        file.write("Skills: " + skills_entry.get() + "\n")
        file.write("Experience: " + experience_entry.get() + "\n")

        file.close()

        messagebox.showinfo(
            "Success",
            "Resume saved in resume.txt"
        )

    def clear_resume():

        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        education_entry.delete(0, tk.END)
        skills_entry.delete(0, tk.END)
        experience_entry.delete(0, tk.END)

    tk.Button(
        resume,
        text="SAVE RESUME",
        command=save_resume,
        width=20
    ).pack(pady=15)

    tk.Button(
        resume,
        text="CLEAR",
        command=clear_resume,
        width=20
    ).pack()


# ---------------- JOB PAGE ----------------

def job_page():

    job = tk.Toplevel(root)
    job.title("Job Management")
    job.geometry("650x600")
    job.config(bg="white")

    tk.Label(
        job,
        text="Job Management",
        font=("Arial", 20, "bold"),
        bg="white"
    ).pack(pady=20)

    tk.Label(job, text="Job Title", bg="white").pack()
    job_entry = tk.Entry(job, width=50)
    job_entry.pack(pady=5)

    tk.Label(job, text="Company", bg="white").pack()
    company_entry = tk.Entry(job, width=50)
    company_entry.pack(pady=5)

    tk.Label(job, text="Location", bg="white").pack()
    location_entry = tk.Entry(job, width=50)
    location_entry.pack(pady=5)

    job_list = tk.Listbox(job, width=70, height=10)
    job_list.pack(pady=15)

    jobs = []

    def add_job():

        if job_entry.get() == "":
            messagebox.showwarning(
                "Warning",
                "Please enter job title."
            )
            return

        job_data = {
            "title": job_entry.get(),
            "company": company_entry.get(),
            "location": location_entry.get()
        }

        jobs.append(job_data)

        file = open("jobs.txt", "a")

        file.write("Job Title: " + job_entry.get() + "\n")
        file.write("Company: " + company_entry.get() + "\n")
        file.write("Location: " + location_entry.get() + "\n")
        file.write("--------------------\n")

        file.close()

        job_list.insert(
            tk.END,
            job_data["title"] + " | " +
            job_data["company"] + " | " +
            job_data["location"]
        )

        job_entry.delete(0, tk.END)
        company_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            "Job added successfully."
        )

    tk.Button(
        job,
        text="ADD JOB",
        command=add_job,
        width=20
    ).pack()


# ---------------- AI ANALYSIS ----------------

def ai_analysis():

    analysis = tk.Toplevel(root)
    analysis.title("AI Resume Analysis")
    analysis.geometry("650x550")
    analysis.config(bg="white")

    tk.Label(
        analysis,
        text="AI Resume Analysis",
        font=("Arial", 20, "bold"),
        bg="white"
    ).pack(pady=20)

    tk.Label(
        analysis,
        text="Enter your skills:",
        font=("Arial", 12),
        bg="white"
    ).pack()

    skills = tk.Entry(analysis, width=50)
    skills.pack(pady=10)

    result = tk.Text(
        analysis,
        width=65,
        height=15
    )
    result.pack(pady=10)

    def analyze():

        user_skills = skills.get()

        if user_skills == "":
            messagebox.showwarning(
                "Warning",
                "Please enter your skills."
            )
            return

        result.delete("1.0", tk.END)

        result.insert(
            tk.END,
            "AI Analysis Result\n\n"
        )

        result.insert(
            tk.END,
            "Your Skills: " + user_skills + "\n\n"
        )

        result.insert(
            tk.END,
            "Suggestions:\n"
        )

        result.insert(
            tk.END,
            "• Improve your technical skills.\n"
        )

        result.insert(
            tk.END,
            "• Add relevant projects to your resume.\n"
        )

        result.insert(
            tk.END,
            "• Highlight your important skills.\n"
        )

        result.insert(
            tk.END,
            "• Apply for jobs related to your skills.\n"
        )

    def speak_result():

        text = result.get("1.0", tk.END)

        if text.strip() != "":
            speak(text)

    tk.Button(
        analysis,
        text="ANALYZE RESUME",
        command=analyze,
        width=20
    ).pack(pady=5)

    tk.Button(
        analysis,
        text="SPEAK RESULT",
        command=speak_result,
        width=20
    ).pack(pady=5)


# ---------------- JOB MATCHING ----------------

def job_matching():

    match = tk.Toplevel(root)
    match.title("AI Job Matching")
    match.geometry("600x500")
    match.config(bg="white")

    tk.Label(
        match,
        text="AI Job Matching",
        font=("Arial", 20, "bold"),
        bg="white"
    ).pack(pady=20)

    tk.Label(
        match,
        text="Enter your skills:",
        font=("Arial", 12),
        bg="white"
    ).pack()

    skills_entry = tk.Entry(match, width=50)
    skills_entry.pack(pady=10)

    result = tk.Text(
        match,
        width=60,
        height=15
    )
    result.pack(pady=10)

    def find_jobs():

        skills = skills_entry.get().lower()

        result.delete("1.0", tk.END)

        if "python" in skills:

            result.insert(
                tk.END,
                "Suitable Job: Python Intern\n"
            )

            result.insert(
                tk.END,
                "Match: 100%\n\n"
            )

        elif "chemistry" in skills:

            result.insert(
                tk.END,
                "Suitable Job: Chemistry Teacher\n"
            )

            result.insert(
                tk.END,
                "Match: 100%\n\n"
            )

        elif "excel" in skills:

            result.insert(
                tk.END,
                "Suitable Job: Data Entry Assistant\n"
            )

            result.insert(
                tk.END,
                "Match: 100%\n\n"
            )

        else:

            result.insert(
                tk.END,
                "No matching job found."
            )

    tk.Button(
        match,
        text="FIND SUITABLE JOBS",
        command=find_jobs,
        width=25
    ).pack()


# ---------------- MAIN FRONTEND ----------------

tk.Label(
    root,
    text="AI RESUME & JOB MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#eef4f7"
).pack(pady=40)

tk.Label(
    root,
    text="Your Personal AI Career Assistant",
    font=("Arial", 14),
    bg="#eef4f7"
).pack(pady=5)

tk.Button(
    root,
    text="RESUME MANAGEMENT",
    command=resume_page,
    width=30
).pack(pady=10)

tk.Button(
    root,
    text="JOB MANAGEMENT",
    command=job_page,
    width=30
).pack(pady=10)

tk.Button(
    root,
    text="AI RESUME ANALYSIS",
    command=ai_analysis,
    width=30
).pack(pady=10)

tk.Button(
    root,
    text="AI JOB MATCHING",
    command=job_matching,
    width=30
).pack(pady=10)

tk.Button(
    root,
    text="INTRODUCTION & VOICE",
    command=show_introduction,
    width=30
).pack(pady=10)

tk.Button(
    root,
    text="EXIT",
    command=root.destroy,
    width=30
).pack(pady=10)


root.mainloop()