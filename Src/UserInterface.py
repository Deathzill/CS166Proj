from PassphraseGenerator import passphrase_generator
from PasswordGenerator import password_generator
from Password_Manager import save_password, get_all, delete_password
from PasswordStrengthChecker import check_password_strength
import sys
import tkinter.messagebox as messagebox

# https://customtkinter.tomschimansky.com/
import customtkinter as ctk

ctk.set_appearance_mode("dark")

class PassphraseGeneratorFrame(ctk.CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.label = ctk.CTkLabel(self, text="Passphrase Generator")
      self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

      self.num_words_entry = ctk.CTkEntry(self, placeholder_text="Num. Words")
      self.num_words_entry.grid(row=1, column=0, padx=10, pady=10, sticky="we")

      self.capitalize_check_box = ctk.CTkCheckBox(self, text="Capitalize")
      self.capitalize_check_box.grid(row=2, column=0, padx=10, pady=10, sticky="w")

      self.include_numbers_check_box = ctk.CTkCheckBox(self, text="Incl. Numbers")
      self.include_numbers_check_box.grid(row=3, column=0, padx=10, pady=10, sticky="w")

      self.separator_entry = ctk.CTkEntry(self, placeholder_text="Separator")
      self.separator_entry.grid(row=4, column=0, padx=10, pady=10, sticky="we")

      self.result_text_box = ctk.CTkTextbox(self, height=50)
      self.result_text_box.grid(row=5, column=0, padx=10, pady=10)
      self.result_text_box.insert("0.0", "Phrase3 Placeholder1")

      self.generate_button = ctk.CTkButton(self, text="Generate", command=self.generate)
      self.generate_button.grid(row=6, column=0, padx=10, pady=10, sticky="we")

   def generate(self):
      result = passphrase_generator(num_words=int(self.num_words_entry.get()), capitalize=self.capitalize_check_box.get()
                                    , include_numbers=self.include_numbers_check_box.get(), separator=self.separator_entry.get())
      self.result_text_box.delete("0.0", str(sys.maxsize) + ".0")
      self.result_text_box.insert("0.0", result)

class PasswordGeneratorFrame(ctk.CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.label = ctk.CTkLabel(self, text="Password Generator")
      self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

      self.num_chars_entry = ctk.CTkEntry(self, placeholder_text="Num. Characters (8-24)")
      self.num_chars_entry.grid(row=1, column=0, padx=10, pady=10, sticky="we")

      self.capitalize_check_box = ctk.CTkCheckBox(self, text="Incl. Capitals")
      self.capitalize_check_box.grid(row=2, column=0, padx=10, pady=10, sticky="w")

      self.include_numbers_check_box = ctk.CTkCheckBox(self, text="Incl. Numbers")
      self.include_numbers_check_box.grid(row=3, column=0, padx=10, pady=10, sticky="w")

      self.include_specialchar_check_box = ctk.CTkCheckBox(self, text="Incl. Special Characters")
      self.include_specialchar_check_box.grid(row=4, column=0, padx=10, pady=10, sticky="we")

      self.result_text_box = ctk.CTkTextbox(self, height=50)
      self.result_text_box.grid(row=5, column=0, padx=10, pady=10)
      self.result_text_box.insert("0.0", "Password3 Placeholder1")

      self.generate_button = ctk.CTkButton(self, text="Generate", command=self.generate)
      self.generate_button.grid(row=6, column=0, padx=10, pady=10, sticky="we")

   def generate(self):
      result = password_generator(num_chars=int(self.num_chars_entry.get()), capitalize=self.capitalize_check_box.get()
                                    , include_numbers=self.include_numbers_check_box.get(), include_specialchar=self.include_specialchar_check_box.get())
      self.result_text_box.delete("0.0", str(sys.maxsize) + ".0")
      self.result_text_box.insert("0.0", result)

class PasswordSaverFrame(ctk.CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.label = ctk.CTkLabel(self, text="Password Saver")
      self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

      self.website_entry = ctk.CTkEntry(self, placeholder_text="Website", height=50)
      self.website_entry.grid(row=1, column=0, padx=10, pady=10)

      self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", height=50)
      self.username_entry.grid(row=2, column=0, padx=10, pady=10)

      self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", height=50)
      self.password_entry.grid(row=3, column=0, padx=10, pady=10)

      self.save_button = ctk.CTkButton(self, text="Save", command=self.save_password)
      self.save_button.grid(row=4, column=0, padx=10, pady=10, sticky="we")

   def save_password(self):
      save_password("Src/passwords.json.enc", self.website_entry.get(), self.username_entry.get(), self.password_entry.get(), "your_password")


class PasswordDeleterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text="Password Deleter")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        self.website_entry = ctk.CTkEntry(self, placeholder_text="Website", height=50)
        self.website_entry.grid(row=1, column=0, padx=10, pady=10)

        self.save_button = ctk.CTkButton(self, text="Delete", command=self.delete_password)
        self.save_button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

    def delete_password(self):
        website = self.website_entry.get()
        if not website:
            messagebox.showwarning("Missing Information", "Please enter a website to delete.")
            return

        # Show confirmation dialog
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the password for '{website}'?")
        if confirm:
            try:
                delete_password("Src/passwords.json.enc", website, "your_password")
                messagebox.showinfo("Success", f"Password for '{website}' has been deleted.")
                
            except KeyError:
                messagebox.showerror("Error", f"No credentials found for '{website}'.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showinfo("Cancelled", "Deletion cancelled.")


class PasswordViewerFrame(ctk.CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.label = ctk.CTkLabel(self, text="Password Viewer")
      self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

      self.save_button = ctk.CTkButton(self, text="View", command=self.view_passwords)
      self.save_button.grid(row=1, column=0, padx=10, pady=10, sticky="we")

      self.passwords_text_box = ctk.CTkTextbox(self, height=200)
      self.passwords_text_box.grid(row=2, column=0, padx=10, pady=10)
      self.passwords_text_box.insert("0.0", "Press view to update")

   def view_passwords(self):
      self.passwords_text_box.delete("0.0", str(sys.maxsize) + ".0")
      data = get_all("Src/passwords.json.enc", "your_password")
      formatted_string = ""

      for website, credentials in data.items():
         formatted_string += f"website: {website}\nusername: {credentials['username']}\npassword: {credentials['password']}\n\n"
      
      self.passwords_text_box.insert("0.0", formatted_string)

class PasswordStrengthCheckerFrame(ctk.CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.label = ctk.CTkLabel(self, text="Password Checker")
      self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

      self.manual_password_entry = ctk.CTkEntry(self, placeholder_text="Enter Password", height=50)
      self.manual_password_entry.grid(row=1, column=0, padx=10, pady=10)

      self.check_button = ctk.CTkButton(self, text="Check Strength", command=self.check_strength)
      self.check_button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

        # Label to display the strength of the password
      self.strength_label = ctk.CTkLabel(self, text="Password Strength: ")
      self.strength_label.grid(row=3, column=0, padx=10, pady=10, sticky="we")

        # Label to display suggestions for improvement
      self.suggestions_label = ctk.CTkTextbox(self, height=100, font=("Arial", 12), wrap="word", state="disabled")
      self.suggestions_label.grid(row=4, column=0, padx=10, pady=10, sticky="we")

   def check_strength(self):
      password = self.manual_password_entry.get()
      
      if not password:
            self.strength_label.configure(text="Password Strength: Please enter a password.", text_color="gray")

            # Display a default placeholder in the suggestions label
            self.suggestions_label.configure(state="normal")
            self.suggestions_label.delete("0.0", "end")  # Clear previous suggestions
            self.suggestions_label.insert("0.0", "Password strength suggestions will appear here.")  # Default text
            self.suggestions_label.configure(state="disabled")

            return  
      strength, suggestions = check_password_strength(password)
      
      strength_color = {
            "Strong": "green",
            "Medium": "orange",
            "Weak": "red"
        }
        
      # Display strength
      self.strength_label.configure(text=f"Password Strength: {strength}", text_color=strength_color.get(strength, "black"))

      # Display suggestions for improvement
      suggestions_text = "\n".join(f"• {s}" for s in suggestions) if suggestions else "Password is strong!"
      self.suggestions_label.configure(state="normal")  # Enable the textbox for updating text
      self.suggestions_label.delete("0.0", "end")  # Clear the previous text
      self.suggestions_label.insert("0.0", suggestions_text)  # Insert new suggestions
      self.suggestions_label.configure(state="disabled")  # Disable the textbox for editing



class App(ctk.CTk):
   def __init__(self):
      super().__init__()

      self.title("Password Manager")
      self.geometry("720x710")

      self.passphrase_generator_frame = PassphraseGeneratorFrame(self)
      self.passphrase_generator_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

      self.password_generator_frame = PasswordGeneratorFrame(self)
      self.password_generator_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

      self.password_saver_frame = PasswordSaverFrame(self)
      self.password_saver_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

      self.password_deleter_frame = PasswordDeleterFrame(self)
      self.password_deleter_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

      self.password_viewer_frame = PasswordViewerFrame(self)
      self.password_viewer_frame.grid(row=1, column=3, padx=10, pady=10, sticky="n")

      self.manual_password_checker_frame = PasswordStrengthCheckerFrame(self)
      self.manual_password_checker_frame.grid(row=0, column=3, padx=10, pady=10, sticky="n")
      

      