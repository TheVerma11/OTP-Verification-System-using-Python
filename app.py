import time
import secrets
import hashlib
import tkinter as tk
from tkinter import messagebox


OTP_EXPIRY = 600          # 10 minutes
MAX_ATTEMPTS = 3
RESEND_COOLDOWN = 30      # 30 seconds


class OTPVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification System")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        self.otp_hash = None
        self.otp_created_at = None
        self.attempts = 0
        self.resend_available_at = 0

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="OTP Verification",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=(30, 10))

        subtitle = tk.Label(
            self.root,
            text="Secure Email Verification - Demo Mode",
            font=("Arial", 11)
        )
        subtitle.pack(pady=(0, 25))

        tk.Label(
            self.root,
            text="Email Address",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=50)

        self.email_entry = tk.Entry(
            self.root,
            width=38,
            font=("Arial", 11)
        )
        self.email_entry.pack(pady=(5, 15), ipady=6)

        self.send_button = tk.Button(
            self.root,
            text="Generate OTP",
            command=self.send_otp,
            width=20,
            font=("Arial", 11, "bold")
        )
        self.send_button.pack(pady=5)

        self.demo_otp_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold")
        )
        self.demo_otp_label.pack(pady=10)

        tk.Label(
            self.root,
            text="Enter OTP",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=50, pady=(10, 0))

        self.otp_entry = tk.Entry(
            self.root,
            width=20,
            font=("Arial", 14),
            justify="center"
        )
        self.otp_entry.pack(pady=8, ipady=6)

        self.verify_button = tk.Button(
            self.root,
            text="Verify OTP",
            command=self.verify_otp,
            width=20,
            font=("Arial", 11, "bold")
        )
        self.verify_button.pack(pady=5)

        self.resend_button = tk.Button(
            self.root,
            text="Resend OTP",
            command=self.resend_otp,
            width=20,
            state="disabled"
        )
        self.resend_button.pack(pady=10)

        self.status_label = tk.Label(
            self.root,
            text="Enter your email and generate an OTP.",
            font=("Arial", 10)
        )
        self.status_label.pack(pady=10)

        self.timer_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10)
        )
        self.timer_label.pack(pady=5)

    def generate_otp(self):
        return f"{secrets.randbelow(1_000_000):06d}"

    def hash_otp(self, otp):
        return hashlib.sha256(otp.encode()).hexdigest()

    def send_otp(self):

        email = self.email_entry.get().strip()

        if not email or "@" not in email:
            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email address."
            )
            return

        otp = self.generate_otp()

        self.otp_hash = self.hash_otp(otp)
        self.otp_created_at = time.time()
        self.attempts = 0
        self.resend_available_at = time.time() + RESEND_COOLDOWN

        # Demo mode: display OTP inside application
        self.demo_otp_label.config(
            text=f"Demo OTP: {otp}"
        )

        self.status_label.config(
            text="OTP generated successfully."
        )

        self.send_button.config(state="disabled")
        self.resend_button.config(state="disabled")

        self.update_timer()

        messagebox.showinfo(
            "OTP Generated",
            "OTP generated successfully.\n\n"
            "Use the Demo OTP shown in the application."
        )

    def verify_otp(self):

        entered_otp = self.otp_entry.get().strip()

        if not self.otp_hash:
            messagebox.showwarning(
                "No OTP",
                "Please generate an OTP first."
            )
            return

        if time.time() - self.otp_created_at > OTP_EXPIRY:

            self.otp_hash = None

            self.status_label.config(
                text="OTP expired. Generate a new OTP."
            )

            self.demo_otp_label.config(text="")

            messagebox.showwarning(
                "OTP Expired",
                "Your OTP has expired."
            )

            self.send_button.config(state="normal")
            return

        if self.attempts >= MAX_ATTEMPTS:

            self.otp_hash = None

            messagebox.showerror(
                "Attempts Exceeded",
                "Maximum verification attempts reached."
            )

            return

        self.attempts += 1

        if self.hash_otp(entered_otp) == self.otp_hash:

            self.otp_hash = None

            self.status_label.config(
                text="Email verified successfully!"
            )

            self.demo_otp_label.config(
                text="Verification Successful"
            )

            messagebox.showinfo(
                "Success",
                "OTP verified successfully!"
            )

            self.verify_button.config(state="disabled")
            self.send_button.config(state="normal")

        else:

            remaining = MAX_ATTEMPTS - self.attempts

            if remaining > 0:

                self.status_label.config(
                    text=f"Invalid OTP. {remaining} attempts remaining."
                )

                messagebox.showerror(
                    "Invalid OTP",
                    f"Incorrect OTP.\n\n"
                    f"Attempts remaining: {remaining}"
                )

            else:

                self.otp_hash = None
                self.demo_otp_label.config(text="")

                messagebox.showerror(
                    "Verification Failed",
                    "Maximum attempts exceeded."
                )

    def resend_otp(self):

        if time.time() < self.resend_available_at:

            remaining = int(
                self.resend_available_at - time.time()
            )

            messagebox.showinfo(
                "Please Wait",
                f"Please wait {remaining} seconds."
            )

            return

        self.send_otp()

    def update_timer(self):

        if not self.otp_created_at:
            return

        elapsed = time.time() - self.otp_created_at
        remaining = max(
            0,
            OTP_EXPIRY - int(elapsed)
        )

        if remaining > 0:

            minutes = remaining // 60
            seconds = remaining % 60

            self.timer_label.config(
                text=f"OTP expires in: {minutes:02d}:{seconds:02d}"
            )

            # Enable resend after cooldown
            if time.time() >= self.resend_available_at:
                self.resend_button.config(state="normal")

            self.root.after(
                1000,
                self.update_timer
            )

        else:

            self.timer_label.config(
                text="OTP expired."
            )

            self.status_label.config(
                text="OTP expired. Generate a new OTP."
            )

            self.otp_hash = None
            self.demo_otp_label.config(text="")

            self.send_button.config(
                state="normal"
            )


if __name__ == "__main__":

    root = tk.Tk()

    app = OTPVerificationApp(root)

    root.mainloop()