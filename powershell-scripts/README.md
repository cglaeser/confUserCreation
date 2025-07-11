# PowerShell Scripts for Conference User Management

This folder contains the core PowerShell automation scripts for managing conference users in Azure AD.

## 📁 Scripts Overview

### 🆕 New-ConferenceUsers.ps1
**Purpose**: Create conference users in bulk with standardized naming and optional Azure resources.

**Key Features**:
- Bulk user creation with automatic naming (`ConferenceName-user1`, `ConferenceName-user2`, etc.)
- Automatic Azure AD group creation and assignment
- Optional Azure Resource Groups for each user
- Excel export with all user details including passwords
- Dry-run mode for safe testing
- Comprehensive error handling and logging

### 🗑️ Remove-ConferenceUsers.ps1
**Purpose**: Clean up conference users and associated resources after events.

**Key Features**:
- Safe removal of conference users by pattern matching
- Optional removal of Azure AD groups
- Optional removal of Azure Resource Groups
- Confirmation prompts for safety
- Dry-run mode for preview
- Detailed removal reporting

### 📖 Examples.ps1
**Purpose**: Comprehensive usage examples and common scenarios.

**Contents**:
- Basic user creation examples
- Advanced scenarios with resource groups
- Cleanup and removal examples
- Best practices and tips

## 🚀 Quick Start

### Prerequisites
```powershell
# Install required modules
Install-Module Microsoft.Graph.Authentication -Scope CurrentUser
Install-Module Microsoft.Graph.Users -Scope CurrentUser
Install-Module Microsoft.Graph.Groups -Scope CurrentUser

# Optional for Resource Groups
Install-Module Az.Accounts -Scope CurrentUser
Install-Module Az.Resources -Scope CurrentUser

# Optional for Excel export
Install-Module ImportExcel -Scope CurrentUser
```

### Authentication
```powershell
# Connect to Microsoft Graph
Connect-MgGraph -Scopes "User.ReadWrite.All,Directory.ReadWrite.All,Group.ReadWrite.All"

# For Resource Groups (optional)
Connect-AzAccount
```

## 💻 Usage Examples

### Basic User Creation
```powershell
# Create 10 users for TechConf2024
./New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 10

# Preview before creating (dry-run)
./New-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -UserCount 10 -DryRun
```

### Advanced Creation with Resource Groups
```powershell
# Create users with individual Azure Resource Groups
./New-ConferenceUsers.ps1 -ConferenceName "Workshop2024" -UserCount 5 -CreateResourceGroups -Location "West Europe"

# With custom domain and Excel export
./New-ConferenceUsers.ps1 -ConferenceName "DevConf" -UserCount 20 -Domain "mycompany.onmicrosoft.com" -ExcelPath "./users.xlsx"
```

### User Cleanup
```powershell
# Preview what will be removed (recommended first step)
./Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -DryRun

# Remove users only
./Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024"

# Remove users, groups, and resource groups
./Remove-ConferenceUsers.ps1 -ConferenceName "TechConf2024" -RemoveGroups -RemoveResourceGroups
```

## ⚙️ Common Parameters

### New-ConferenceUsers.ps1 Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ConferenceName` | String | Yes | Prefix for all usernames |
| `UserCount` | Int | No | Number of users to create (default: 10) |
| `Domain` | String | No | Azure AD domain (auto-detected if not specified) |
| `Password` | String | No | Shared password (random if not specified) |
| `CreateResourceGroups` | Switch | No | Create Azure Resource Groups |
| `SubscriptionId` | String | No | Azure subscription for resource groups |
| `Location` | String | No | Azure region (default: West Europe) |
| `ExcelPath` | String | No | Path for Excel export |
| `DryRun` | Switch | No | Preview mode without actual creation |

### Remove-ConferenceUsers.ps1 Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ConferenceName` | String | Yes | Conference name to remove |
| `Domain` | String | No | Azure AD domain (auto-detected if not specified) |
| `RemoveGroups` | Switch | No | Remove associated Azure AD groups |
| `RemoveResourceGroups` | Switch | No | Remove associated resource groups |
| `Force` | Switch | No | Skip confirmation prompts |
| `DryRun` | Switch | No | Preview mode without actual removal |

## 🛡️ Security Best Practices

1. **Always test with `-DryRun` first** before making actual changes
2. **Use least-privilege permissions** - only grant necessary Azure AD roles
3. **Review output carefully** before proceeding with bulk operations
4. **Keep Excel exports secure** - they contain user passwords
5. **Use strong passwords** when specifying custom passwords
6. **Regularly clean up** unused conference accounts

## 🔧 Troubleshooting

### Common Issues

#### "Connect-MgGraph: Authentication needed"
```powershell
# Solution: Re-authenticate with proper scopes
Disconnect-MgGraph
Connect-MgGraph -Scopes "User.ReadWrite.All,Directory.ReadWrite.All,Group.ReadWrite.All"
```

#### "Insufficient privileges to complete the operation"
```powershell
# Solution: Check your Azure AD role assignments
# Required roles: User Administrator, Groups Administrator
Get-MgContext | Select-Object Account, Scopes
```

#### "Resource group creation failed"
```powershell
# Solution: Ensure Azure authentication and permissions
Connect-AzAccount
Get-AzContext
# Ensure you have Contributor role on the subscription
```

#### PowerShell execution policy errors
```powershell
# Solution: Set execution policy (run as administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📊 Output and Logging

### Console Output
- Real-time progress indicators
- Detailed operation logs
- Error messages with recommendations
- Summary statistics

### Excel Export
When using `-ExcelPath`, the script creates a detailed Excel file containing:
- Username and UPN for each user
- Individual passwords (if generated)
- Group memberships
- Resource group information (if created)
- Creation timestamps

### Log Files
Scripts create detailed log files in the current directory:
- `ConferenceUserCreation-YYYYMMDD-HHMMSS.log`
- `ConferenceUserRemoval-YYYYMMDD-HHMMSS.log`

## 🔗 Integration with Web Frontend

These PowerShell scripts are designed to work seamlessly with the web frontend located in `../web-frontend/`. The Flask application calls these scripts with appropriate parameters based on user input from the web interface.

### Web Frontend Integration Points
- **Parameter Validation**: Web interface validates inputs before calling scripts
- **Progress Monitoring**: Real-time feedback through PowerShell output parsing
- **Error Handling**: Web interface captures and displays script errors
- **File Paths**: All file paths are properly resolved between web frontend and scripts

## 📄 More Information

For detailed usage examples and advanced scenarios, see:
- `Examples.ps1` - Comprehensive usage examples
- `../README.md` - Main project documentation
- `../web-frontend/README-WebFrontend.md` - Web interface documentation

---

**Note**: These scripts require appropriate Azure AD permissions and should be tested in a development environment before use in production.
