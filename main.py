"""
🚨 DANGEROUS APP - PENTESTER'S PLAYGROUND 🚨
Main application that integrates all dangerous modules with security features.
FOR EDUCATIONAL PURPOSES ONLY - USE RESPONSIBLY!
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import os
import threading
import time
from datetime import datetime

# Add the core modules to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

# Import security modules
from security.access_control import AccessControl
from security.warning_system import WarningSystem

# Import dangerous modules
from dangerous.system_crash import SystemCrashTools

class DangerousApp:
    """
    🚨 Main application for dangerous operations 🚨
    Provides a safe interface for dangerous functions with proper warnings.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🚨 DANGEROUS APP - PENTESTER'S PLAYGROUND 🚨")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a1a")

        # Initialize security systems
        self.access_control = AccessControl()
        self.warning_system = WarningSystem()

        # Initialize dangerous modules
        self.system_crash_tools = SystemCrashTools(self.access_control, self.warning_system)

        # Emergency stop flag
        self.emergency_stop = False

        # Setup UI
        self.setup_ui()

        # Check admin status
        self.check_admin_status()

    def setup_ui(self):
        """Setup the user interface"""

        # Main title
        title_frame = tk.Frame(self.root, bg="#1a1a1a")
        title_frame.pack(fill="x", padx=20, pady=20)

        title_label = tk.Label(
            title_frame,
            text="🚨 DANGEROUS APP - PENTESTER'S PLAYGROUND 🚨",
            font=("Arial", 18, "bold"),
            bg="#1a1a1a",
            fg="#FF0000"
        )
        title_label.pack()

        subtitle_label = tk.Label(
            title_frame,
            text="⚠️ FOR EDUCATIONAL PURPOSES ONLY - USE RESPONSIBLY ⚠️",
            font=("Arial", 10),
            bg="#1a1a1a",
            fg="#FFAA00"
        )
        subtitle_label.pack(pady=5)

        # Status frame
        status_frame = tk.Frame(self.root, bg="#1a1a1a")
        status_frame.pack(fill="x", padx=20, pady=10)

        # Admin status
        self.admin_status_label = tk.Label(
            status_frame,
            text="Admin Status: Checking...",
            font=("Arial", 10),
            bg="#1a1a1a",
            fg="#FFFFFF"
        )
        self.admin_status_label.pack(side="left")

        # Emergency stop button
        emergency_btn = tk.Button(
            status_frame,
            text="🚨 EMERGENCY STOP 🚨",
            command=self.emergency_stop_all,
            bg="#FF0000",
            fg="#FFFFFF",
            font=("Arial", 10, "bold"),
            relief="raised",
            borderwidth=2
        )
        emergency_btn.pack(side="right")

        # Main content frame
        content_frame = tk.Frame(self.root, bg="#1a1a1a")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Create notebook for different modules
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill="both", expand=True)

        # System Crash Tools Tab
        self.setup_system_crash_tab()

        # System Monitor Tab
        self.setup_system_monitor_tab()

        # Logs Tab
        self.setup_logs_tab()

        # Add Virus Builder tab to menu
        self.add_tools_menu()

        # Add a status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor="w")
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Set ttk theme for better appearance
        try:
            style = ttk.Style()
            style.theme_use("clam")
        except Exception:
            pass

    def add_tools_menu(self):
        """Add Tools menu with Virus Builder tab"""
        menubar = tk.Menu(self.root)
        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Virus Builder (EDU ONLY)", command=lambda: show_virus_builder_tab(self))
        menubar.add_cascade(label="Tools", menu=tools_menu)
        self.root.config(menu=menubar)

    def setup_system_crash_tab(self):
        """Setup the system crash tools tab"""
        crash_frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(crash_frame, text="🚨 System Crash Tools")

        # Title
        crash_title = tk.Label(
            crash_frame,
            text="🚨 CRITICAL DANGER: System Crash Tools 🚨",
            font=("Arial", 14, "bold"),
            bg="#1a1a1a",
            fg="#FF0000"
        )
        crash_title.pack(pady=10)

        # Warning
        warning_label = tk.Label(
            crash_frame,
            text="⚠️ These functions can permanently damage your system! ⚠️\n"
                 "⚠️ Use only for educational purposes on systems you own! ⚠️",
            font=("Arial", 10, "bold"),
            bg="#1a1a1a",
            fg="#FF0000",
            justify="center"
        )
        warning_label.pack(pady=10)

        # Buttons frame
        buttons_frame = tk.Frame(crash_frame, bg="#1a1a1a")
        buttons_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Button definitions
        buttons = [
            ("🚨 TRIGGER BLUE SCREEN OF DEATH 🚨", self.trigger_bsod, "#FF0000"),
            ("💣 CREATE FORK BOMB 💣", self.create_fork_bomb, "#FF6600"),
            ("💾 EXHAUST MEMORY 💾", self.exhaust_memory, "#FF6600"),
            ("🔥 EXHAUST CPU 🔥", self.exhaust_cpu, "#FFAA00"),
            ("💿 FILL DISK SPACE 💿", self.fill_disk, "#FFAA00"),
        ]
        for text, cmd, color in buttons:
            btn = tk.Button(
                buttons_frame,
                text=text,
                command=cmd,
                bg=color,
                fg="#FFFFFF",
                font=("Arial", 12, "bold"),
                relief="raised",
                borderwidth=3,
                padx=20,
                pady=10
            )
            btn.pack(fill="x", pady=5)

    def setup_system_monitor_tab(self):
        """Setup the system monitor tab"""
        monitor_frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(monitor_frame, text="📊 System Monitor")

        # Title
        monitor_title = tk.Label(
            monitor_frame,
            text="📊 System Resource Monitor",
            font=("Arial", 14, "bold"),
            bg="#1a1a1a",
            fg="#00FF00"
        )
        monitor_title.pack(pady=10)

        # System info frame
        info_frame = tk.Frame(monitor_frame, bg="#1a1a1a")
        info_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # System info labels
        self.cpu_label = tk.Label(
            info_frame,
            text="CPU Usage: --%",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#FFFFFF"
        )
        self.cpu_label.pack(anchor="w", pady=2)

        self.memory_label = tk.Label(
            info_frame,
            text="Memory Usage: --%",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#FFFFFF"
        )
        self.memory_label.pack(anchor="w", pady=2)

        self.disk_label = tk.Label(
            info_frame,
            text="Disk Usage: --%",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#FFFFFF"
        )
        self.disk_label.pack(anchor="w", pady=2)

        self.process_label = tk.Label(
            info_frame,
            text="Process Count: --",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#FFFFFF"
        )
        self.process_label.pack(anchor="w", pady=2)

        # Update button
        update_btn = tk.Button(
            info_frame,
            text="🔄 Update System Info",
            command=self.update_system_info,
            bg="#00AA00",
            fg="#FFFFFF",
            font=("Arial", 10, "bold")
        )
        update_btn.pack(pady=10)

        # Start monitoring
        self.start_monitoring()

    def setup_logs_tab(self):
        """Setup the logs tab"""
        logs_frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(logs_frame, text="📋 Logs & History")

        # Title
        logs_title = tk.Label(
            logs_frame,
            text="📋 Operation Logs and History",
            font=("Arial", 14, "bold"),
            bg="#1a1a1a",
            fg="#00FF00"
        )
        logs_title.pack(pady=10)

        # Logs text area
        self.logs_text = tk.Text(
            logs_frame,
            height=20,
            bg="#2a2a2a",
            fg="#FFFFFF",
            font=("Consolas", 10),
            wrap="word"
        )
        self.logs_text.pack(fill="both", expand=True, padx=20, pady=10)

        # Buttons frame
        logs_buttons_frame = tk.Frame(logs_frame, bg="#1a1a1a")
        logs_buttons_frame.pack(fill="x", padx=20, pady=10)

        refresh_btn = tk.Button(
            logs_buttons_frame,
            text="🔄 Refresh Logs",
            command=self.refresh_logs,
            bg="#00AA00",
            fg="#FFFFFF",
            font=("Arial", 10, "bold")
        )
        refresh_btn.pack(side="left", padx=5)

        clear_btn = tk.Button(
            logs_buttons_frame,
            text="🗑️ Clear Logs",
            command=self.clear_logs,
            bg="#FF6600",
            fg="#FFFFFF",
            font=("Arial", 10, "bold")
        )
        clear_btn.pack(side="left", padx=5)

        # Load initial logs
        self.refresh_logs()

    def check_admin_status(self):
        """Check and display admin status"""
        is_admin = self.access_control.is_admin()

        if is_admin:
            self.admin_status_label.config(
                text="Admin Status: ✅ ADMIN PRIVILEGES",
                fg="#00FF00"
            )
        else:
            self.admin_status_label.config(
                text="Admin Status: ❌ NO ADMIN PRIVILEGES",
                fg="#FF0000"
            )

            # Show warning for non-admin
            messagebox.showwarning(
                "Admin Privileges Required",
                "Some dangerous functions require admin privileges.\n"
                "Run this application as administrator for full functionality."
            )

    def trigger_bsod(self):
        """Trigger Blue Screen of Death"""
        result = self.system_crash_tools.bsod_trigger()
        if result:
            self.log_message("BSOD trigger executed successfully")
        else:
            self.log_message("BSOD trigger failed or was cancelled")

    def create_fork_bomb(self):
        """Create fork bomb"""
        result = self.system_crash_tools.fork_bomb()
        if result:
            self.log_message("Fork bomb executed successfully")
        else:
            self.log_message("Fork bomb failed or was cancelled")

    def exhaust_memory(self):
        """Exhaust system memory"""
        result = self.system_crash_tools.memory_exhaustion()
        if result:
            self.log_message("Memory exhaustion executed successfully")
        else:
            self.log_message("Memory exhaustion failed or was cancelled")

    def exhaust_cpu(self):
        """Exhaust CPU"""
        result = self.system_crash_tools.cpu_exhaustion()
        if result:
            self.log_message("CPU exhaustion executed successfully")
        else:
            self.log_message("CPU exhaustion failed or was cancelled")

    def fill_disk(self):
        """Fill disk space"""
        result = self.system_crash_tools.disk_exhaustion()
        if result:
            self.log_message("Disk exhaustion executed successfully")
        else:
            self.log_message("Disk exhaustion failed or was cancelled")

    def emergency_stop_all(self):
        """Emergency stop all dangerous operations"""
        self.emergency_stop = True
        self.system_crash_tools.emergency_stop_all()

        messagebox.showinfo(
            "Emergency Stop",
            "Emergency stop activated!\n"
            "All dangerous operations have been terminated."
        )

        self.log_message("EMERGENCY STOP ACTIVATED")

    def start_monitoring(self):
        """Start system monitoring"""
        def monitor_loop():
            while not self.emergency_stop:
                try:
                    self.update_system_info()
                    time.sleep(2)  # Update every 2 seconds
                except Exception as e:
                    print(f"Monitoring error: {e}")
                    break

        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()

    def update_system_info(self):
        """Update system information display"""
        try:
            info = self.system_crash_tools.get_system_info()
            if info:
                self.cpu_label.config(text=f"CPU Usage: {info.get('cpu_percent', '--')}%")
                self.memory_label.config(text=f"Memory Usage: {info.get('memory_percent', '--')}%")
                self.disk_label.config(text=f"Disk Usage: {info.get('disk_percent', '--')}%")
                self.process_label.config(text=f"Process Count: {info.get('process_count', '--')}")
        except Exception as e:
            print(f"Error updating system info: {e}")

    def log_message(self, message: str):
        """Log a message to the logs tab"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        if hasattr(self, "logs_text"):
            self.logs_text.insert(tk.END, log_entry)
            self.logs_text.see(tk.END)

    def refresh_logs(self):
        """Refresh the logs display"""
        self.logs_text.delete(1.0, tk.END)

        # Add recent logs
        self.log_message("=== DANGEROUS APP LOGS ===")
        self.log_message("Application started")
        self.log_message("Security systems initialized")

        # Add audit log entries
        audit_log = self.access_control.get_audit_log()
        if audit_log:
            self.log_message(f"Recent audit entries: {len(audit_log)}")
            for entry in audit_log[-5:]:  # Show last 5 entries
                func = entry.get('function', 'Unknown')
                danger = entry.get('danger_level', 'Unknown')
                self.log_message(f"  {func} - {danger}")

    def clear_logs(self):
        """Clear the logs"""
        self.logs_text.delete(1.0, tk.END)
        self.log_message("Logs cleared")

    def run(self):
        """Run the application"""
        try:
            self.log_message("Starting Dangerous App...")
            self.root.mainloop()
        except KeyboardInterrupt:
            self.emergency_stop_all()
        except Exception as e:
            self.log_message(f"Application error: {e}")
            self.emergency_stop_all()

def build_virus_script(payload_type, output_path):
    # Only for educational purposes!
    payloads = {
        "Message Box Spam": (
            'import ctypes\n'
            'for _ in range(100):\n'
            '    ctypes.windll.user32.MessageBoxW(0, "This is a test!", "Virus Builder Demo", 1)\n'
        ),
        "Fork Bomb (Linux)": (
            'import os\n'
            'while True:\n'
            '    os.fork()\n'
        ),
        "CPU Hog": (
            'while True:\n'
            '    pass\n'
        ),
    }
    code = payloads.get(payload_type, "# Invalid payload\n")
    with open(output_path, "w") as f:
        f.write("# VIRUS DEMO - FOR EDUCATIONAL PURPOSES ONLY\n")
        f.write(code)

def show_virus_builder_tab(app):
    # Remove any existing virus builder tab
    for i in range(app.notebook.index("end")):
        if app.notebook.tab(i, "text").startswith("🦠 Virus Builder"):
            app.notebook.forget(i)
            break

    virus_tab = ttk.Frame(app.notebook)
    app.notebook.add(virus_tab, text="🦠 Virus Builder (EDU ONLY)")

    info = tk.Label(
        virus_tab,
        text="Virus Builder (For Educational Purposes Only!)",
        font=("Arial", 14, "bold"),
        fg="red"
    )
    info.pack(pady=10)

    payload_label = tk.Label(virus_tab, text="Select Payload Type:")
    payload_label.pack(pady=(10, 0))

    payload_var = tk.StringVar(value="Message Box Spam")
    payloads = [
        "Message Box Spam",
        "Fork Bomb (Linux)",
        "CPU Hog"
    ]
    payload_menu = ttk.Combobox(virus_tab, textvariable=payload_var, values=payloads, state="readonly")
    payload_menu.pack(pady=5)

    output_label = tk.Label(virus_tab, text="Output File:")
    output_label.pack(pady=(10, 0))

    output_var = tk.StringVar()
    output_entry = tk.Entry(virus_tab, textvariable=output_var, width=40)
    output_entry.pack(pady=5)

    def browse_output():
        path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if path:
            output_var.set(path)

    browse_btn = tk.Button(virus_tab, text="Browse...", command=browse_output)
    browse_btn.pack(pady=2)

    def on_build():
        payload = payload_var.get()
        output = output_var.get()
        if not output:
            messagebox.showerror("Error", "Please specify an output file.")
            return
        try:
            build_virus_script(payload, output)
            messagebox.showinfo("Success", f"Virus script created at:\n{output}\n\nFOR EDUCATIONAL USE ONLY!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to build script: {e}")

    build_btn = tk.Button(
        virus_tab,
        text="Build Virus Script",
        fg="white",
        bg="#d9534f",
        font=("Arial", 12, "bold"),
        command=on_build
    )
    build_btn.pack(pady=15)

    warning = tk.Label(
        virus_tab,
        text="⚠️ These scripts are for EDUCATIONAL use ONLY. Do NOT run on production systems! ⚠️",
        fg="red",
        font=("Arial", 10, "bold"),
        wraplength=400,
        justify="center"
    )
    warning.pack(pady=10)

    app.notebook.select(virus_tab)

def main():
    """Main entry point"""
    print("🚨 DANGEROUS APP - PENTESTER'S PLAYGROUND 🚨")
    print("⚠️ FOR EDUCATIONAL PURPOSES ONLY - USE RESPONSIBLY ⚠️")
    print("=" * 60)

    # Check if running in a safe environment
    if os.path.exists("/proc/version") or "Microsoft" in os.environ.get("OS", ""):
        print("✅ Running in a safe environment")
    else:
        print("⚠️ Warning: Unknown environment")

    # Create and run the application
    app = DangerousApp()
    app.run()

if __name__ == "__main__":
    main()