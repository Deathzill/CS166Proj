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
      self.result_text_box.insert("0.0", "")

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
      self.result_text_box.insert("0.0", "")

      self.generate_button = ctk.CTkButton(self, text="Generate", command=self.generate)
      self.generate_button.grid(row=6, column=0, padx=10, pady=10, sticky="we")

   def generate(self):
      result = password_generator(num_chars=int(self.num_chars_entry.get()), capitalize=self.capitalize_check_box.get()
                                    , include_numbers=self.include_numbers_check_box.get(), include_specialchar=self.include_specialchar_check_box.get())
      self.result_text_box.delete("0.0", str(sys.maxsize) + ".0")
      self.result_text_box.insert("0.0", result)

class PasswordSaverFrame(ctk.CTkFrame):
    def __init__(self, master, password):
        super().__init__(master)

        self.__file_password = password

        self.label = ctk.CTkLabel(self, text="Password Saver")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        self.website_entry = ctk.CTkEntry(self, placeholder_text="Website")
        self.website_entry.grid(row=1, column=0, padx=10, pady=10, sticky="we")

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.grid(row=2, column=0, padx=10, pady=10, sticky="we")

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password")
        self.password_entry.grid(row=3, column=0, padx=10, pady=10, sticky="we")

        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_password)
        self.save_button.grid(row=4, column=0, padx=10, pady=10, sticky="we")

    def save_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showwarning("Missing Information", "Please fill in all fields before saving.")
            return

        # Check if credentials for the website already exist
        existing_credentials = get_all("Src/passwords.json.enc", self.__file_password)
        if website in existing_credentials:
            confirm_replace = messagebox.askyesno(
                "Replace Existing Credentials",
                f"Credentials for {website} already exist. Do you want to replace them?"
            )
            if not confirm_replace:
                return

        # Save the credentials
        save_password("Src/passwords.json.enc", website, username, password, self.__file_password)
        messagebox.showinfo("Success", "Credentials have been saved successfully!")

        # Clear the input fields after saving
        self.website_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")

class PasswordDeleterFrame(ctk.CTkFrame):
    def __init__(self, master, password):
        super().__init__(master)

        self.__file_password = password

        self.label = ctk.CTkLabel(self, text="Password Deleter")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        self.website_entry = ctk.CTkEntry(self, placeholder_text="Website")
        self.website_entry.grid(row=1, column=0, padx=10, pady=10, sticky="we")

        self.save_button = ctk.CTkButton(self, text="Delete", command=self.delete_password)
        self.save_button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

    def delete_password(self):
        website = self.website_entry.get()
        if not website:
            messagebox.showwarning("Missing Information", "Please enter a website to delete.")
            return

        # Check if credentials for the website exist
        try:
            existing_credentials = get_all("Src/passwords.json.enc", self.__file_password)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving credentials: {str(e)}")
            return

        if website not in existing_credentials:
            messagebox.showerror("Error", f"No credentials found for '{website}'.")
            return

        # Show confirmation dialog if credentials exist
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the password for '{website}'?")
        if confirm:
            try:
                delete_password("Src/passwords.json.enc", website, self.__file_password)
                messagebox.showinfo("Success", f"Password for '{website}' has been deleted.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showinfo("Cancelled", "Deletion cancelled.")

        # Clear the input field after the process
        self.website_entry.delete(0, "end")


class PasswordViewerFrame(ctk.CTkFrame):
    def __init__(self, master, password):
        super().__init__(master)

        self.__file_password = password

        self.label = ctk.CTkLabel(self, text="Password Viewer")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        # Entry to input the website to look up
        self.website_entry = ctk.CTkEntry(self, placeholder_text="Website")
        self.website_entry.grid(row=1, column=0, padx=10, pady=10, sticky="we")

        # Button to look up credentials
        self.lookup_button = ctk.CTkButton(self, text="Look Up", command=self.lookup_credentials)
        self.lookup_button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

        # Button to list all credentials
        self.list_all_button = ctk.CTkButton(self, text="List All", command=self.list_all_credentials)
        self.list_all_button.grid(row=3, column=0, padx=10, pady=10, sticky="we")

        # Text box to display credentials
        self.result_box = ctk.CTkTextbox(self, height=150, width=300)
        self.result_box.grid(row=4, column=0, padx=10, pady=10, sticky="we")

    def lookup_credentials(self):
        website = self.website_entry.get()
        if not website:
            messagebox.showwarning("Missing Information", "Please enter a website to look up.")
            return

        try:
            # Retrieve all credentials
            credentials = get_all("Src/passwords.json.enc", self.__file_password)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving credentials: {str(e)}")
            return

        # Search for the website in the credentials
        if website in credentials:
            result = credentials[website]
            self.result_box.delete("1.0", "end")  # Clear previous results
            self.result_box.insert(
                "1.0",
                f"Website: {website}\nUsername: {result['username']}\nPassword: {result['password']}",
            )
        else:
            messagebox.showinfo("Not Found", f"No credentials found for '{website}'.")
            self.result_box.delete("1.0", "end")

    def list_all_credentials(self):
        try:
            # Retrieve all credentials
            credentials = get_all("Src/passwords.json.enc", self.__file_password)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving credentials: {str(e)}")
            return

        # Display all credentials in the result box
        self.result_box.delete("1.0", "end")  # Clear previous results
        if credentials:
            for website, details in credentials.items():
                self.result_box.insert(
                    "end",
                    f"Website: {website}\nUsername: {details['username']}\nPassword: {details['password']}\n\n",
                )
        else:
            self.result_box.insert("1.0", "No credentials found.")

class PasswordStrengthCheckerFrame(ctk.CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.label = ctk.CTkLabel(self, text="Password Checker")
      self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

      self.manual_password_entry = ctk.CTkEntry(self, placeholder_text="Enter Password")
      self.manual_password_entry.grid(row=1, column=0, padx=10, pady=10, sticky="we")

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
   def __init__(self, password):
      super().__init__()

      self.title("Password Manager")
      self.geometry("820x752")

      self.passphrase_generator_frame = PassphraseGeneratorFrame(self)
      self.passphrase_generator_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

      self.password_generator_frame = PasswordGeneratorFrame(self)
      self.password_generator_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

      self.password_saver_frame = PasswordSaverFrame(self, password)
      self.password_saver_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")

      self.password_deleter_frame = PasswordDeleterFrame(self, password)
      self.password_deleter_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

      self.password_viewer_frame = PasswordViewerFrame(self, password)
      self.password_viewer_frame.grid(row=1, column=3, padx=10, pady=10, sticky="n")

      self.manual_password_checker_frame = PasswordStrengthCheckerFrame(self)
      self.manual_password_checker_frame.grid(row=0, column=3, padx=10, pady=10, sticky="n")
