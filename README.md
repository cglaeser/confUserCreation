# 🏗️ Conference User Management System

[![PowerShell](https://img.shields.io/badge/PowerShell-5.1+-blue.svg)](https://github.com/PowerShell/PowerShell)
[![Flask](https://img.shields.io/badge/Flask-2.3+-blue.svg)](https://flask.palletsprojects.com/)
[![Azure](https://img.shields.io/badge/Azure-Entra%20ID-0078d4.svg)](https://azure.microsoft.com/en-us/services/active-directory/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/tsimiz/confUserCreation.svg)](https://github.com/tsimiz/confUserCreation/issues)

A comprehensive solution for creating and managing conference workshop user accounts in Azure/Entra ID environments. This system provides both PowerShell automation scripts and a user-friendly multilingual web interface for streamlined user management.

## 📁 Project Structure

```
confUserCreation/
├── 📁 powershell-scripts/          # PowerShell automation scripts
│   ├── New-ConferenceUsers.ps1     # Create conference users
│   ├── Remove-ConferenceUsers.ps1  # Remove conference users
│   └── Examples.ps1                # Usage examples
├── 📁 web-frontend/                # Flask web application (4 languages)
│   ├── app.py                      # Main Flask application
│   ├── requirements.txt            # Python dependencies
│   ├── � templates/               # HTML templates
│   └── � translations/            # EN/DE/ES/FI translations
├── � run.sh                       # Quick start script
└── � start-frontend.sh            # Detailed startup script
```

## � Quick Start

### Option 1: Web Interface (Recommended)

```bash
# Start the multilingual web frontend
./run.sh

# Open your browser to: http://localhost:5000
# Switch between English, German, Spanish, or Finnish
```

### Option 2: PowerShell Scripts (Advanced Users)

```bash
# Navigate to scripts folder
cd powershell-scripts

# Create users
./New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 10

# Remove users
./Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024"
```

## ✨ Features

### 🌐 Web Frontend

- **Multilingual Support**: English, German, Spanish, Finnish interfaces
- **Intuitive Interface**: User-friendly forms with real-time validation
- **System Diagnostics**: Built-in status checking and requirements validation
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Security**: Form validation, error handling, and safe parameter passing

### ⚡ PowerShell Scripts

- **Automated User Creation**: Bulk creation with standardized naming conventions
- **Azure Integration**: Full Azure AD and Azure Resource Groups support
- **Excel Export**: Detailed spreadsheet output with all user information
- **Dry-Run Mode**: Safe preview mode before making actual changes
- **Comprehensive Logging**: Detailed progress and error reporting

## 📋 System Requirements

### For Web Frontend

- **Python 3.6+** with pip
- **Web Browser** (Chrome, Firefox, Safari, Edge)
- **PowerShell Core (pwsh)** for backend script execution

### For PowerShell Scripts

- **PowerShell 5.1+** or **PowerShell Core 6+**
- **Azure CLI** or **PowerShell Az modules** (optional, for resource groups)
- **Microsoft Graph PowerShell modules**

### Azure Permissions Required

- `User.ReadWrite.All`
- `Directory.ReadWrite.All`
- `Group.ReadWrite.All`
- Azure Subscription Contributor (for resource groups)

## � Usage Examples

### Web Interface Usage

```bash
# Start the web server
./run.sh

# Navigate to http://localhost:5000
# 1. Select "Create Users" for bulk user creation
# 2. Select "Remove Users" for cleanup
# 3. Select "Status" for system diagnostics
# 4. Use language switcher for German/Spanish/Finnish
```

### PowerShell Script Usage

```bash
# Navigate to PowerShell scripts
cd powershell-scripts

# Basic user creation
./New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 10

# Advanced creation with resource groups
./New-ConferenceUsers.ps1 -ConferenceName "MyWorkshop" -UserCount 5 -CreateResourceGroups -Location "West Europe"

# Safe cleanup
./Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -DryRun
```

## 📖 Documentation

- **[Web Frontend Guide](README-WebFrontend.md)** - Complete web interface documentation
- **[Multilingual Setup](MULTILINGUAL_SETUP.md)** - Translation and i18n configuration
- **[Deployment Guide](DEPLOYMENT.md)** - Production deployment instructions

## 🎯 PowerShell Script Features

- �🔍 **Automatic Tenant Discovery**: Automatically detects and uses the current Azure tenant
- 📝 **Standardized Naming**: Creates users with pattern `<ConferenceName>-user1`, `<ConferenceName>-user2`, etc.
- 👥 **Entra ID Group Management**: Creates and manages Entra ID groups for conference users
- 🏗️ **Azure Resource Groups**: Optionally creates individual resource groups for each user
- ⚙️ **Flexible Configuration**: Customizable user count, domain, and password settings
- 🔑 **Unique Passwords**: Generates unique passwords for each user (or uses a shared password if specified)
- 📊 **Excel Export**: Exports detailed user information including individual passwords to Excel
- ⚡ **Dry Run Mode**: Preview changes before execution
- 🛡️ **Error Handling**: Robust error handling with detailed logging
- 🔐 **Security**: Uses Microsoft Graph API with proper authentication and permissions
- 🧹 **Cleanup Support**: Includes deletion script for removing created resources
- 📊 **Detailed Reporting**: Comprehensive output with progress tracking

## � Installation & Setup

1. **📦 Install required PowerShell modules:**

   ```powershell
   Install-Module Microsoft.Graph.Authentication -Force
   Install-Module Microsoft.Graph.Users -Force
   Install-Module Microsoft.Graph.Groups -Force
   Install-Module Microsoft.Graph.Identity.DirectoryManagement -Force
   Install-Module ImportExcel -Force
   Install-Module Az.Accounts
   ```

2. **🐍 Install Python dependencies (for web frontend):**

   ```bash
   pip install -r web-frontend/requirements.txt
   ```

3. **🎯 Test your setup:**

   ```powershell
   .\New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 10
   ```

4. **👀 Preview before creating (recommended):**

   ```powershell
   .\New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 10 -DryRun
   ```

5. **🧹 Clean up when done:**
   ```powershell
   .\Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024"
   ```

> **💡 Tip**: Always use `-DryRun` first to see what will be created!

## 📋 Prerequisites

### 🔧 PowerShell Modules

Install the required Microsoft Graph PowerShell modules:

```powershell
# Core modules for user and group management
Install-Module Microsoft.Graph.Authentication -Force
Install-Module Microsoft.Graph.Users -Force
Install-Module Microsoft.Graph.Groups -Force
Install-Module Microsoft.Graph.Identity.DirectoryManagement -Force
```

For Azure resource group functionality, also install:

```powershell
# Additional modules for Azure resource management
Install-Module Az.Accounts -Force
Install-Module Az.Resources -Force
```

For Excel output functionality, install:

```powershell
# Optional module for Excel output (highly recommended)
Install-Module ImportExcel -Force
```

### 🔑 Azure Permissions

The user running the script must have sufficient permissions in the Azure tenant:

| Permission            | Purpose                        |
| --------------------- | ------------------------------ |
| `User.ReadWrite.All`  | 👤 To create and manage users  |
| `Directory.Read.All`  | 📂 To read tenant information  |
| `Group.ReadWrite.All` | 👥 To create and manage groups |

**Minimum Required Permissions:**
The script executor must have adequate permissions to both Entra ID and Azure:

- **Entra ID**: The above Microsoft Graph permissions are the minimum required
- **Azure**: For resource group creation, **Contributor** or **Owner** role in the target subscription

For Azure resource group creation:

- 🏗️ **Contributor** or **Owner** role in the target subscription

### 🔐 Authentication

You must be authenticated to Azure with appropriate permissions. The script will prompt for authentication when run.

**⚠️ Important Limitations:**

- 🚫 **MSA Personal Accounts**: This script cannot be executed with Microsoft Account (MSA) personal accounts. You must use a work or school account with access to an Azure Active Directory/Entra ID tenant.
- 🏢 **Organizational Account Required**: The executing user must have an organizational account with the necessary permissions listed above.

## 💻 Usage

### 👥 Creating Users

#### 🎯 Basic Usage

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 15
```

#### 🔧 Advanced Usage

```powershell
# 🔑 Create users with custom password
.\New-ConferenceUsers.ps1 -ConferenceName "DevWorkshop" -UserCount 5 -Password "TempPass123!"

# 🌐 Create users with custom domain
.\New-ConferenceUsers.ps1 -ConferenceName "CloudSummit" -UserCount 20 -Domain "contoso.com"

# 🔓 Create users without forcing password change
.\New-ConferenceUsers.ps1 -ConferenceName "SecureConf" -UserCount 10 -ForcePasswordChange $false

# 🏗️ Create users with Azure resource groups
.\New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 10 -CreateResourceGroups $true -Location "East US"

# 📋 Preview changes with dry run
.\New-ConferenceUsers.ps1 -ConferenceName "DevWorkshop" -UserCount 5 -DryRun

# 🌍 Create users with Azure resource groups in specific subscription
.\New-ConferenceUsers.ps1 -ConferenceName "DevWorkshop" -UserCount 5 -CreateResourceGroups $true -SubscriptionId "12345678-1234-1234-1234-123456789012" -Location "West Europe"
```

### 🗑️ Removing Users

#### 🧹 Basic Removal

```powershell
.\Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024"
```

#### 🔧 Advanced Removal

```powershell
# 👥 Remove users and groups but not resource groups
.\Remove-ConferenceUsers.ps1 -ConferenceName "DevWorkshop" -RemoveResourceGroups $false

# 💥 Remove everything including resource groups without confirmation
.\Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -RemoveResourceGroups $true -Force

# 🌐 Remove users from specific domain
.\Remove-ConferenceUsers.ps1 -ConferenceName "CloudSummit" -Domain "contoso.com"

# 👀 Preview what would be removed (dry run)
.\Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -DryRun
```

## ⚙️ Parameters

### 🆕 New-ConferenceUsers.ps1

| Parameter              | Type    | Required | Default               | Description                                   |
| ---------------------- | ------- | -------- | --------------------- | --------------------------------------------- |
| `ConferenceName`       | String  | ✅       | -                     | 📛 Conference name used as username prefix    |
| `UserCount`            | Integer | ❌       | 10                    | 🔢 Number of users to create (1-1000)         |
| `Domain`               | String  | ❌       | Auto-detected         | 🌐 Domain for user principal names            |
| `Password`             | String  | ❌       | Auto-generated        | 🔑 Initial password for all users             |
| `ForcePasswordChange`  | Boolean | ❌       | $true                 | 🔄 Force password change on first login       |
| `CreateResourceGroups` | Boolean | ❌       | $false                | 🏗️ Create Azure resource groups for each user |
| `SubscriptionId`       | String  | ❌       | Current context       | 📋 Azure subscription ID for resource groups  |
| `Location`             | String  | ❌       | Interactive selection | 🌍 Azure location for resource groups         |
| `DryRun`               | Switch  | ❌       | $false                | 👀 Preview changes without executing          |
| `ExcelOutputPath`      | String  | ❌       | Current directory     | 📊 Path where Excel file should be saved      |

### 🗑️ Remove-ConferenceUsers.ps1

| Parameter              | Type    | Required | Default       | Description                                    |
| ---------------------- | ------- | -------- | ------------- | ---------------------------------------------- |
| `ConferenceName`       | String  | ✅       | -             | 📛 Conference name to identify users to remove |
| `Domain`               | String  | ❌       | Auto-detected | 🌐 Domain for user principal names             |
| `RemoveGroups`         | Boolean | ❌       | $true         | 👥 Remove associated Entra ID group            |
| `RemoveResourceGroups` | Boolean | ❌       | $false        | 🏗️ Remove associated Azure resource groups     |
| `Force`                | Switch  | ❌       | $false        | 💥 Skip confirmation prompts                   |
| `DryRun`               | Switch  | ❌       | $false        | 👀 Preview changes without executing           |

## 📖 Examples

### 📊 Example 1: Basic Conference Setup

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 25
```

**✨ Output**: Creates 25 users named TechConf2024-user1 through TechConf2024-user25 and an Entra ID group "TechConf2024-users"

### 🔐 Example 2: Custom Password

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "DevWorkshop" -UserCount 10 -Password "Workshop2024!"
```

**✨ Output**: Creates 10 users with the specified password and Entra ID group

### 🔑 Example 3: Unique Passwords for Each User

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "SecureConf" -UserCount 15
```

**✨ Output**: Creates 15 users, each with a unique randomly generated password. Individual passwords are saved to the Excel export file for secure distribution.

### 🏗️ Example 4: Large Conference with Resource Groups

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "GlobalSummit" -UserCount 100 -Domain "company.com" -CreateResourceGroups $true -Location "East US"
```

**✨ Output**: Creates 100 users using the specified domain, creates individual resource groups for each user in East US

### 🧹 Example 5: Complete Cleanup

```powershell
.\Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -RemoveResourceGroups $true
```

**✨ Output**: Removes all users, groups, and resource groups associated with TechConf2024

### 👀 Example 6: Dry Run Preview

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "TestConf" -UserCount 5 -DryRun
```

**✨ Output**: Shows what would be created without actually creating anything, then asks for confirmation

### 🌍 Example 7: Multi-Location Setup

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "GlobalEvent" -UserCount 50 -CreateResourceGroups $true -SubscriptionId "12345678-1234-1234-1234-123456789012" -Location "West Europe"
```

**✨ Output**: Creates users and resource groups in a specific subscription and Azure region

### 🔄 Example 8: No Password Change Required

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "TrainingLab" -UserCount 15 -ForcePasswordChange $false
```

**✨ Output**: Creates users who won't be forced to change password on first login - perfect for training environments

### 🚫 Example 9: Safe Removal Preview

```powershell
.\Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -DryRun
```

**✨ Output**: Shows exactly what would be removed without actually deleting anything - always safe to run first!

### 📊 Example 10: Excel Output to Custom Location

```powershell
.\New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 20 -ExcelOutputPath "C:\Conference\Reports"
```

**✨ Output**: Creates 20 users with unique passwords and saves detailed Excel report to specified folder with usernames, individual passwords, and resource groups

## 📊 Output

The script provides detailed, color-coded output including:

- 🔌 Connection status to Microsoft Graph
- 🏢 Tenant information (name and ID)
- 🌐 Domain being used for user creation
- ⏳ Progress of user creation with real-time updates
- 📈 Summary of successful and failed creations
- 📋 Complete list of created users
- 🔑 Login credentials for the users
- 📊 **Excel report** with comprehensive user details (usernames, passwords, resource groups)

### 💻 Sample Output

```
=== Conference User Creation Script ===
Conference Name: TechConf2024
User Count: 5

Checking for required PowerShell modules...
Importing module: Microsoft.Graph.Authentication
Importing module: Microsoft.Graph.Users
Connecting to Microsoft Graph...
Successfully connected to Microsoft Graph
Retrieving tenant information...
Connected to tenant: Contoso Corporation
Tenant ID: 12345678-1234-1234-1234-123456789012
Using domain: contoso.com
Unique passwords will be generated for each user
IMPORTANT: Individual passwords will be available in the Excel export file!

Creating 5 users...
Creating user 1 of 5: TechConf2024-user1@contoso.com
✓ Created user: TechConf2024-user1@contoso.com
Creating user 2 of 5: TechConf2024-user2@contoso.com
✓ Created user: TechConf2024-user2@contoso.com
...

=== Creation Summary ===
Successfully created: 5 out of 5 users
Failed: 0 users

Created Users:
==============
• TechConf2024 Workshop User 1 (TechConf2024-user1@contoso.com)
• TechConf2024 Workshop User 2 (TechConf2024-user2@contoso.com)
...

Login Information:
Username Format: TechConf2024-user[1-5]@contoso.com
Passwords: Unique password generated for each user
Individual passwords are available in the Excel export file
Force Password Change: True

Script completed successfully!
```

## 🔒 Security Considerations

- 🔑 **Password Management**: If no password is specified, unique random passwords are generated for each user. These passwords are available in the Excel export file. Make sure to save and distribute these passwords securely.
- 🛡️ **Permissions**: The script requires high-level permissions to create users. Ensure the running user has appropriate access.
- 📝 **Audit Trail**: User creation activities are logged in Azure AD audit logs.
- 🔐 **Password Policy**: Generated passwords comply with common complexity requirements, but ensure they meet your organization's password policy.
- ⚠️ **Access Control**: Created users inherit default tenant permissions - review and adjust as needed.
- 🗑️ **Cleanup**: Always remove test users and resources when no longer needed to maintain security hygiene.

## 🛠 Troubleshooting

### 🚨 Common Issues

#### 1️⃣ **Module Not Found**

```
❌ Error: Required module 'Microsoft.Graph.Authentication' is not installed
```

**💡 Solution**: Install the required modules using `Install-Module`

```powershell
Install-Module Microsoft.Graph.Authentication -Force
```

#### 2️⃣ **Insufficient Permissions**

```
❌ Error: Insufficient privileges to complete the operation
```

**💡 Solution**: Ensure the user has User.ReadWrite.All and Directory.Read.All permissions

#### 3️⃣ **Authentication Failed**

```
❌ Error: Failed to connect to Microsoft Graph
```

**💡 Solution**: Check your Azure credentials and network connectivity

#### 4️⃣ **Domain Not Found**

```
❌ Error: The domain 'example.com' is not verified in this tenant
```

**💡 Solution**: Use a verified domain or let the script auto-detect the default domain

#### 5️⃣ **Resource Group Creation Failed**

```
❌ Error: Failed to create resource group
```

**💡 Solution**: Ensure you have Contributor/Owner permissions in the Azure subscription

### 🆘 Getting Help

For additional help with the script parameters:

```powershell
Get-Help .\New-ConferenceUsers.ps1 -Full
Get-Help .\Remove-ConferenceUsers.ps1 -Full
```

For community support, check the [GitHub Issues](https://github.com/tsimiz/confUserCreation/issues) page.

### 💡 Pro Tips

- 🔄 **Always use dry run first**: Use `-DryRun` parameter to preview changes before execution
- 📝 **Save passwords securely**: Auto-generated passwords are complex and secure - store them in a password manager
- 🏷️ **Use descriptive conference names**: This helps identify resources later and makes cleanup easier
- 🧹 **Clean up regularly**: Remove test users and resources when no longer needed
- 📊 **Monitor resource usage**: Keep track of Azure resource group costs when using the resource group feature
- 🔍 **Check permissions**: Ensure adequate permissions before running large user creation batches

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### 💡 Ways to Contribute

- 🐛 Report bugs and issues
- 💻 Submit code improvements
- 📚 Improve documentation
- 🌟 Add new features
- 🧪 Add tests and examples

## 💬 Support

For issues and questions, please create an issue in the [GitHub repository](https://github.com/tsimiz/confUserCreation/issues).

### 📞 Getting Help

- 📋 Check the [troubleshooting guide](#-troubleshooting)
- 🔍 Search existing [GitHub Issues](https://github.com/tsimiz/confUserCreation/issues)
- 🆕 Create a new issue with detailed information
- 💬 Join community discussions

---

<div align="center">

**Made with ❤️ for the Azure community**

⭐ **Star this repository if you find it helpful!** ⭐

</div>
