#!/usr/bin/env python3
"""
🧪 DANGEROUS APP - INSTALLATION TEST 🧪
Test script to verify that all components are working correctly.
"""

import sys
import os
import importlib
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    modules_to_test = [
        ('tkinter', 'GUI framework'),
        ('psutil', 'System monitoring'),
        ('json', 'Configuration handling'),
        ('logging', 'Logging system'),
        ('threading', 'Threading support'),
        ('datetime', 'Time handling'),
        ('ctypes', 'System calls'),
        ('platform', 'Platform detection'),
        ('subprocess', 'Process management')
    ]
    
    failed_imports = []
    
    for module_name, description in modules_to_test:
        try:
            importlib.import_module(module_name)
            print(f"✅ {module_name} - {description}")
        except ImportError as e:
            print(f"❌ {module_name} - {description} (Error: {e})")
            failed_imports.append(module_name)
    
    return len(failed_imports) == 0

def test_security_modules():
    """Test if security modules can be imported"""
    print("\n🔒 Testing security modules...")
    
    # Add core directory to path
    core_path = Path(__file__).parent / 'core'
    sys.path.insert(0, str(core_path))
    
    security_modules = [
        ('security.access_control', 'Access Control'),
        ('security.warning_system', 'Warning System')
    ]
    
    failed_imports = []
    
    for module_path, description in security_modules:
        try:
            importlib.import_module(module_path)
            print(f"✅ {description}")
        except ImportError as e:
            print(f"❌ {description} (Error: {e})")
            failed_imports.append(module_path)
    
    return len(failed_imports) == 0

def test_dangerous_modules():
    """Test if dangerous modules can be imported"""
    print("\n🚨 Testing dangerous modules...")
    
    dangerous_modules = [
        ('dangerous.system_crash', 'System Crash Tools')
    ]
    
    failed_imports = []
    
    for module_path, description in dangerous_modules:
        try:
            importlib.import_module(module_path)
            print(f"✅ {description}")
        except ImportError as e:
            print(f"❌ {description} (Error: {e})")
            failed_imports.append(module_path)
    
    return len(failed_imports) == 0

def test_directories():
    """Test if required directories exist or can be created"""
    print("\n📁 Testing directories...")
    
    directories = ['logs', 'config']
    
    for directory in directories:
        dir_path = Path(directory)
        if dir_path.exists():
            print(f"✅ {directory} directory exists")
        else:
            try:
                dir_path.mkdir(exist_ok=True)
                print(f"✅ {directory} directory created")
            except Exception as e:
                print(f"❌ Failed to create {directory} directory (Error: {e})")
                return False
    
    return True

def test_file_permissions():
    """Test if we can write to log files"""
    print("\n📝 Testing file permissions...")
    
    test_files = [
        'logs/test.log',
        'config/test.json'
    ]
    
    for file_path in test_files:
        try:
            with open(file_path, 'w') as f:
                f.write("test")
            print(f"✅ Can write to {file_path}")
            
            # Clean up test file
            os.remove(file_path)
        except Exception as e:
            print(f"❌ Cannot write to {file_path} (Error: {e})")
            return False
    
    return True

def test_admin_privileges():
    """Test admin privileges"""
    print("\n👑 Testing admin privileges...")
    
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            print("✅ Running with admin privileges")
        else:
            print("⚠️  Not running with admin privileges")
            print("   Some dangerous functions may not work properly")
        return True
    except Exception as e:
        print(f"⚠️  Could not check admin privileges (Error: {e})")
        return True

def test_system_info():
    """Test system information gathering"""
    print("\n💻 Testing system information...")
    
    try:
        import psutil
        
        # Test CPU info
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"✅ CPU Usage: {cpu_percent}%")
        
        # Test memory info
        memory = psutil.virtual_memory()
        print(f"✅ Memory Usage: {memory.percent}%")
        
        # Test disk info
        disk = psutil.disk_usage('/')
        print(f"✅ Disk Usage: {disk.percent}%")
        
        # Test process count
        process_count = len(psutil.pids())
        print(f"✅ Process Count: {process_count}")
        
        return True
    except Exception as e:
        print(f"❌ Failed to get system info (Error: {e})")
        return False

def test_gui_components():
    """Test GUI components"""
    print("\n🖥️  Testing GUI components...")
    
    try:
        import tkinter as tk
        
        # Test basic tkinter functionality
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Test creating a simple widget
        label = tk.Label(root, text="Test")
        print("✅ Tkinter widgets work")
        
        root.destroy()
        return True
    except Exception as e:
        print(f"❌ GUI test failed (Error: {e})")
        return False

def main():
    """Main test function"""
    print("🧪 DANGEROUS APP - INSTALLATION TEST 🧪")
    print("=" * 50)
    
    tests = [
        ("Import Tests", test_imports),
        ("Security Modules", test_security_modules),
        ("Dangerous Modules", test_dangerous_modules),
        ("Directory Tests", test_directories),
        ("File Permissions", test_file_permissions),
        ("Admin Privileges", test_admin_privileges),
        ("System Information", test_system_info),
        ("GUI Components", test_gui_components)
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test_name, test_function in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_function():
                passed_tests += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
    
    print("\n" + "="*50)
    print(f"📊 TEST RESULTS: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! Installation is complete.")
        print("🚀 You can now run the application with: python launch.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        print("🔧 Try installing missing dependencies or running as administrator.")
    
    print("="*50)

if __name__ == "__main__":
    main() 