#!/usr/bin/env python3
"""
🚨 DANGEROUS APP LAUNCHER 🚨
Safe launcher script that checks dependencies and provides startup warnings.
"""

import sys
import os
import subprocess
import importlib.util
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ ERROR: Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = {
        'psutil': 'psutil',
        'tkinter': 'tkinter'
    }
    
    missing_packages = []
    
    for package_name, import_name in required_packages.items():
        try:
            importlib.import_module(import_name)
            print(f"✅ {package_name} is installed")
        except ImportError:
            missing_packages.append(package_name)
            print(f"❌ {package_name} is missing")
    
    if missing_packages:
        print("\n📦 Installing missing packages...")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ {package} installed successfully")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                return False
    
    return True

def check_admin_privileges():
    """Check if running with admin privileges"""
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            print("✅ Running with admin privileges")
        else:
            print("⚠️  Not running with admin privileges")
            print("   Some dangerous functions may not work properly")
        return True
    except:
        print("⚠️  Could not check admin privileges")
        return True

def show_startup_warning():
    """Show startup warning and get user consent"""
    print("\n" + "="*60)
    print("🚨 DANGEROUS APP - PENTESTER'S PLAYGROUND 🚨")
    print("="*60)
    print()
    print("⚠️  CRITICAL WARNING ⚠️")
    print("This application contains functions that can:")
    print("• Crash your system")
    print("• Delete or corrupt data")
    print("• Cause permanent damage")
    print("• Make your system unusable")
    print()
    print("USE ONLY FOR EDUCATIONAL PURPOSES ON SYSTEMS YOU OWN!")
    print()
    
    while True:
        response = input("Do you understand the risks and want to continue? (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            print("✅ Proceeding with caution...")
            return True
        elif response in ['no', 'n']:
            print("❌ Application cancelled by user")
            return False
        else:
            print("Please answer 'yes' or 'no'")

def check_safe_environment():
    """Check if running in a safe environment"""
    # Check if running in a virtual machine or test environment
    vm_indicators = [
        "/proc/version",  # Linux
        "Microsoft",      # Windows
        "VirtualBox",
        "VMware",
        "QEMU"
    ]
    
    safe_environment = False
    for indicator in vm_indicators:
        if indicator in os.environ.get("OS", "") or os.path.exists(indicator):
            safe_environment = True
            break
    
    if safe_environment:
        print("✅ Running in a safe environment")
    else:
        print("⚠️  Warning: Unknown environment")
        print("   Consider running in a virtual machine for safety")
    
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['logs', 'config']
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def main():
    """Main launcher function"""
    print("🚨 DANGEROUS APP LAUNCHER 🚨")
    print("Checking system requirements...")
    print()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Failed to install required dependencies")
        sys.exit(1)
    
    # Check admin privileges
    check_admin_privileges()
    
    # Check safe environment
    check_safe_environment()
    
    # Create directories
    create_directories()
    
    # Show startup warning
    if not show_startup_warning():
        sys.exit(0)
    
    # Launch the main application
    print("\n🚀 Launching Dangerous App...")
    print("="*60)
    
    try:
        # Import and run the main application
        from main import main as run_app
        run_app()
    except ImportError as e:
        print(f"❌ Error importing main application: {e}")
        print("Make sure you're running this from the correct directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error running application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 