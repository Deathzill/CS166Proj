from PassphraseGenerator import passphrase_generator
import sys

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

      self.capitalize_check_box = ctk.CTkCheckBox(self, text="Capitlize")
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

class PasswordManagementFrame(ctk.CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      self.label = ctk.CTkLabel(self, text="Passwords")
      self.label.grid(row=0, column=0, padx=10, pady=10, sticky="we")

      self.add_button = ctk.CTkButton(self, text="Add")
      self.add_button.grid(row=1, column=0, padx=10, pady=10, sticky="we")

      self.delete_button = ctk.CTkButton(self, text="Delete")
      self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

      self.view_button = ctk.CTkButton(self, text="View")
      self.view_button.grid(row=3, column=0, padx=10, pady=10, sticky="we")

class App(ctk.CTk):
   def __init__(self):
      super().__init__()

      self.title("Password Manager")
      self.geometry("420x370")

      self.passphrase_generator_frame = PassphraseGeneratorFrame(self)
      self.passphrase_generator_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

      self.password_management_frame = PasswordManagementFrame(self)
      self.password_management_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")