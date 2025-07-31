# 🚨 DANGEROUS APP - PENTESTER'S PLAYGROUND 🚨

## ⚠️ CRITICAL WARNING ⚠️

**This application contains functions that can permanently damage your system!**

- 🚨 **CRITICAL DANGER**: Functions that can crash or destroy your system
- ⚠️ **HIGH DANGER**: Functions that can cause temporary issues
- 💡 **MEDIUM DANGER**: Functions that require careful handling
- ✅ **SAFE**: Utility functions for monitoring and testing

**USE ONLY FOR EDUCATIONAL PURPOSES ON SYSTEMS YOU OWN!**

## 🎯 Purpose

This application is designed for:
- **Penetration Testing Education**
- **Security Research**
- **System Administration Training**
- **Understanding System Vulnerabilities**

## 🔒 Security Features

### Multi-Level Warning System
- **🔴 RED ZONE**: Critical danger functions
- **🟠 ORANGE ZONE**: High danger functions
- **🟡 YELLOW ZONE**: Medium danger functions
- **🟢 GREEN ZONE**: Safe utility functions

### Access Control
- Admin privileges required for dangerous functions
- User consent confirmation dialogs
- Audit logging of all dangerous operations
- Session timeout for dangerous functions

### Safeguards
- Automatic backup before dangerous operations
- Rollback mechanisms where possible
- Rate limiting for destructive operations
- Environment detection (prevents running in production)

## 📋 Features

### System Crash Tools (🔴 CRITICAL)
- **BSOD Trigger**: Triggers Windows Blue Screen of Death
- **Fork Bomb**: Creates infinite process loop
- **Memory Exhaustion**: Fills RAM until system crashes
- **CPU Exhaustion**: Uses 100% CPU for specified duration
- **Disk Exhaustion**: Fills disk space with random data

### System Monitoring (🟢 SAFE)
- Real-time CPU usage monitoring
- Memory usage tracking
- Disk space monitoring
- Process count tracking

### Logging & Audit (🟢 SAFE)
- Comprehensive audit logging
- Operation history tracking
- Warning system logs
- Access control logs

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Windows/Linux/macOS
- Admin privileges (for dangerous functions)

### Installation Steps

1. **Clone or download the application**
   ```bash
   git clone <repository-url>
   cd dangerous_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### Running as Administrator (Windows)
For full functionality, run as administrator:
1. Right-click on Command Prompt or PowerShell
2. Select "Run as administrator"
3. Navigate to the application directory
4. Run `python main.py`

## 🚨 Safety Protocols

### Before Any Dangerous Operation
1. ✅ Check admin privileges
2. ✅ Validate target (if applicable)
3. ✅ Create backup (if applicable)
4. ✅ Show multiple warnings
5. ✅ Get explicit user consent
6. ✅ Log operation details
7. ✅ Set emergency stop timer

### During Dangerous Operation
1. ✅ Monitor system resources
2. ✅ Check for emergency stop
3. ✅ Log progress
4. ✅ Provide status updates

### After Dangerous Operation
1. ✅ Verify system stability
2. ✅ Log completion status
3. ✅ Offer rollback option
4. ✅ Update audit trail

## 📁 File Structure

```
dangerous_app/
├── core/
│   ├── security/
│   │   ├── access_control.py      # Admin privileges & permissions
│   │   └── warning_system.py      # Warning dialogs & confirmations
│   └── dangerous/
│       └── system_crash.py        # System crash tools
├── ui/
│   └── main_window.py             # Main application UI
├── config/
│   └── permissions.json           # User permissions
├── logs/
│   ├── access_control.log         # Access control logs
│   ├── warnings.log               # Warning system logs
│   └── system_crash.log           # System crash logs
├── main.py                        # Main application entry point
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## 🎮 Usage

### Starting the Application
```bash
python main.py
```

### Using Dangerous Functions
1. **Select a dangerous function** from the System Crash Tools tab
2. **Read the warning dialog** carefully
3. **Confirm your understanding** of the consequences
4. **Execute the function** (if you're sure)
5. **Monitor the results** in the System Monitor tab

### Emergency Stop
- Click the **🚨 EMERGENCY STOP 🚨** button to immediately stop all dangerous operations
- This will terminate all running dangerous processes

### Monitoring System Resources
- Use the **System Monitor** tab to track CPU, memory, and disk usage
- Monitor process count and system stability
- Check logs for any issues

## ⚠️ Disclaimers

### Legal Disclaimer
This software is provided "AS IS" without warranty of any kind. The authors are not responsible for any damage caused by the use of this software.

### Educational Purpose
This application is designed solely for educational purposes. Users are responsible for ensuring they have proper authorization before testing on any system.

### System Damage
The dangerous functions in this application can cause:
- System crashes
- Data loss
- Application failures
- Hardware stress
- Permanent system damage

### Responsibility
Users are fully responsible for:
- Understanding the consequences of each function
- Testing only on systems they own
- Obtaining proper authorization
- Following local laws and regulations

## 🔧 Configuration

### Permissions File
Edit `config/permissions.json` to customize:
- Which functions require admin privileges
- Which functions require backups
- Which functions require confirmations

### Logging
Logs are stored in the `logs/` directory:
- `access_control.log`: Admin privilege checks
- `warnings.log`: Warning dialog history
- `system_crash.log`: System crash operations

## 🐛 Troubleshooting

### Common Issues

**"Admin privileges required"**
- Run the application as administrator
- On Windows: Right-click → "Run as administrator"

**"Permission denied"**
- Check if you have proper permissions
- Ensure you're running on a system you own

**"Function not available"**
- Some functions are platform-specific
- Check the system requirements

**"Application crashes"**
- Check the logs for error messages
- Ensure all dependencies are installed
- Try running as administrator

### Getting Help
1. Check the logs in the `logs/` directory
2. Review the error messages in the application
3. Ensure all dependencies are installed
4. Verify you have proper permissions

## 📚 Educational Resources

### Understanding the Functions
- **BSOD Trigger**: Learn about Windows kernel vulnerabilities
- **Fork Bomb**: Understand process management and system limits
- **Memory Exhaustion**: Study memory management and system stability
- **CPU Exhaustion**: Learn about CPU scheduling and resource management
- **Disk Exhaustion**: Understand file system limits and storage management

### Security Concepts
- **Access Control**: Understanding privilege escalation
- **System Monitoring**: Learning about resource tracking
- **Audit Logging**: Understanding security event tracking
- **Warning Systems**: Implementing proper user notifications

## 🤝 Contributing

### Guidelines
1. **Safety First**: All dangerous functions must have proper warnings
2. **Documentation**: Document all functions and their risks
3. **Testing**: Test thoroughly in safe environments
4. **Logging**: Implement comprehensive logging for all operations

### Adding New Functions
1. Create the function in the appropriate module
2. Add proper warning dialogs
3. Implement access control checks
4. Add comprehensive logging
5. Update documentation

## 📄 License

This project is for educational purposes only. Use responsibly and only on systems you own or have explicit permission to test.

## ⚖️ Legal Notice

This software is provided for educational purposes only. Users are responsible for:
- Complying with local laws and regulations
- Obtaining proper authorization before testing
- Understanding the consequences of their actions
- Using the software responsibly

**By using this software, you acknowledge that you understand the risks and accept full responsibility for any consequences.**

---

**🚨 REMEMBER: This is for educational purposes only! Use responsibly! 🚨** 