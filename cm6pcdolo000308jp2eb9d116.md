---
title: "Simplify Authentication with Microsoft Identity: Azure AD Device Code Flow for Python Apps"
seoTitle: "Azure AD Device Code Flow for Python Apps"
seoDescription: "Learn how to authenticate Python apps using Azure AD Device Code Flow for secure access to Microsoft resources with Microsoft Graph API"
datePublished: Mon Feb 03 2025 17:45:52 GMT+0000 (Coordinated Universal Time)
cuid: cm6pcdolo000308jp2eb9d116
slug: simplify-authentication-with-microsoft-identity-azure-ad-device-code-flow-for-python-apps
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1737075398012/1ef4700b-1f3e-42ee-ad6b-2ed77098d3a7.png
ogImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737075900371/03558df7-54e5-406d-8439-2edb363b667b.png
tags: cloud, authentication, docker, python, azure, learning

---

Modern applications depend on secure user authentication and data access. [Azure Active Directory (Azure AD)](https://azure.microsoft.com/services/active-directory/) delivers enterprise-grade authentication for apps targeting Microsoft resources. In this blog, we’ll explore how to leverage Azure AD **Device Code flow** and the **Microsoft Graph API** to securely authenticate users and manage calendar data from a containerized Python app.

---

## 🌐 Authentication in Azure: An Overview

Azure AD supports multiple OAuth 2.0 flows:

* **Authorization Code Flow**:  
    Ideal for web apps that require interactive user sign-in from a browser. The user logs in via a front-end application, and the app exchanges an authorization code for an access token. This flow is highly secure since the code is sent server-side, away from client vulnerabilities. Best suited for applications with a backend capable of securely managing tokens.
    
* **Client Credentials Flow**:  
    Perfect for background services or daemons that don’t involve direct user interaction. The app authenticates using its own credentials (e.g., client ID and secret) and gets an access token for calling APIs. This is ideal for system-to-system communication, such as a server-side script managing Microsoft 365 data without needing user consent.
    
* **Device Code Flow**:  
    Tailored to scenarios with limited or no direct user input—e.g., IoT devices or CLI tools. The app generates a device code and URL for the user to authenticate on another device with a full browser. After login, the app receives an access token, making it a great choice for headless environments or containerized apps.
    

In this article, we focus on **Device Code flow ✅**, enabling secure sign-in using a second device with a browser. This approach also fits containerized applications perfectly—just display a device code and ask users to authenticate elsewhere.

### A Note on Azure AD vs. Azure AD B2C

There are two primary identity management solutions within Microsoft’s ecosystem:

* **Azure AD**:  
    Manages organizational (enterprise) identities within a principal directory. Commonly used for internal applications and systems that require integration with Microsoft 365 resources.
    
* **Azure AD B2C**:  
    Designed for external or consumer-facing apps and scenarios where you need a separate directory. It supports custom branding, multi-tenant setups, and social logins (e.g., Google or Facebook). B2C is ideal for apps that serve external users while maintaining separation from the primary organization.
    

For this learning journey, we’re using the standard **Azure AD** in a single, principal directory. This keeps our demonstration simpler and more focused on how to implement the Device Code flow. However, if you need to handle external identities or advanced user journeys, you can explore **Azure AD B2C** to build a dedicated, branded identity solution.

---

## 🏗️ Azure AD Architecture Overview

At the heart of our setup are **Azure AD** for authentication and **Microsoft Graph** for data access. Below is how these pieces fit together:

1. **Azure AD App Registration**
    
    * You register your app in Azure AD, defining permission scopes like `User.Read` and `Calendars.ReadWrite`.
        
2. **Device Code Flow**
    
    * Generates a device code and URL for the user to authenticate on a second device.
        
    * Returns an **access token** upon successful authentication.
        
3. **Microsoft Graph API**
    
    * Consumes the access token to interact with Microsoft 365 endpoints such as `/me` and `/me/events`.
        

![Diagram showing a device with a browser and a containerized app connecting to Azure Public Cloud's Principal Directory. It includes Microsoft Entra ID (Azure AD), App Registration with API permissions (User.Read, Calendar.Read, Calendar.Write), and Microsoft Graph API.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737084557651/0bac99fd-1e18-4136-8d52-d1fc117fc9fe.png align="center")

The diagram shows how Azure AD exchanges tokens and how the application then calls Microsoft Graph using those tokens.

---

## 🚀 Let’s Start by Cloning the Project Repo

To demonstrate how easy it is to set up authentication in Azure AD, clone the following repository:

```bash
git clone https://github.com/xmedinavei/az-deviceflow-auth-app
cd az-deviceflow-auth-app
```

This repo contains all the necessary setup for a containerized Python app that authenticates with Azure AD using the Device Code flow and interacts with Microsoft Graph.

---

## 📚 Setting Up Azure AD

### 1\. Register the App

1. Go to the [Azure Portal](https://portal.azure.com) and select **Microsoft Entra ID**.
    
2. Under **App registrations**, choose **New registration**.
    
3. Provide:
    
    * **Name**: A descriptive name for your app.
        
    * **Supported account types**: For this demo, pick "Accounts in this organizational directory only."
        
4. Click **Register** to complete the registration.
    

### 2\. Configure API Permissions

1. Under **API Permissions**, add permissions for **Microsoft Graph**:
    
    * `User.Read` for basic user profile data.
        
    * `Calendars.ReadWrite` for reading and writing calendar events.
        
2. Click **Grant admin consent** to approve the permissions on behalf of your organization.
    

> **Delegated Permissions vs. Application Permissions**  
> We’re adding **delegated** permissions, meaning the app will act as the signed-in user. The user must grant explicit consent to these permissions during login.

### 3\. Enable Public Client Flow

1. Under **Authentication**, expand **Advanced settings**.
    
2. Toggle **Allow public client flows** to **Yes**.
    
3. Save your settings.
    

### 4\. Collect Credentials

1. Return to the **Overview** page of your App Registration.
    
2. Copy the:
    
    * **Application (client) ID**
        
    * **Directory (tenant) ID**
        
3. Store these in a `.env` file for your app:
    

```plaintext
CLIENT_ID="your-application-id"
TENANT_ID="your-directory-id"
```

---

## 🏃 Let’s Run the App and Authenticate in Azure

With Azure AD configured and the app cloned, it’s time to run the containerized app.

### Build the Docker Image

```bash
docker build -t az-deviceflow-auth-app .
```

This command packages the code into a containerized environment.

### Run the Container

```bash
docker run --rm -it --env-file .env az-deviceflow-auth-app
```

Once the container starts, you’ll see a message like this in the console:

```plaintext
To sign in, use a web browser to open the page https://microsoft.com/devicelogin 
and enter the code ABCD-EFGH to authenticate.
```

Grab your 📱 **phone or another device**, open the provided link (`https://microsoft.com/devicelogin`), and paste the code (`ABCD-EFGH`). After authenticating, you’re granting the app permission to access your Microsoft 365 account.

This process is called **Device Flow Authentication** because the app is running on one device (e.g., the Docker container simulating an IoT device) while you authenticate on another device (like your phone). This flow is perfect for scenarios where the primary device lacks input capabilities, such as a TV or kiosk.

After successfully signing in via the browser, the app will retrieve and display your user information and calendar events. Here’s an example output:

```plaintext
Welcome, John Doe!

Your upcoming calendar events:
1. Subject: Weekly Team Meeting
   Organizer: Jane Smith
   Start: 2023-12-01T10:00:00
   End:   2023-12-01T11:00:00

2. Subject: Project Review
   Organizer: Bob Johnson
   Start: 2023-12-02T14:00:00
   End:   2023-12-02T15:00:00

Your meeting was created with the following details:
Subject: Study for the AZ-204 exam
Location: Wherever you are
Start: 2023-12-01T15:05:00
End: 2023-12-01T15:35:00
```

---

## 🧑‍💻 How It Works: Breaking Down the Code

Let’s dive into the code and understand how everything works step by step. I’ll walk you through the key parts so you can see how this app uses Azure AD and Microsoft Graph to make magic happen. 😊

### Device Code Flow Authentication

First, the app starts the **Device Code flow**. It generates a special code and a URL for you to authenticate. This is the step where you grab your 📱 or another device, open the URL, and enter the code to log in. Once you do, the app gets an access token that it can use to access your Microsoft 365 account. If something goes wrong (like you don’t authenticate in time), it raises an error.

```python
from msal import PublicClientApplication

# Configurations
tenant_id = "your-tenant-id"  # Replace with your tenant ID
client_id = "your-client-id"  # Replace with your app's client ID
scopes = ["User.Read", "Calendars.ReadWrite"]

# Initialize the MSAL app with tenant-specific authority
app = PublicClientApplication(client_id=client_id, authority=f"https://login.microsoftonline.com/{tenant_id}")

# Start the Device Code flow
flow = app.initiate_device_flow(scopes=scopes)
if "user_code" not in flow:
    raise Exception("Failed to start the Device Code flow.")

# Wait for user authentication and get the token
result = app.acquire_token_by_device_flow(flow)
if "access_token" in result:
    print("Authentication successful!")
else:
    print(f"Authentication failed: {result.get('error_description', 'Unknown error')}")
```

### Fetching Microsoft Graph Data

After you log in, the app can start talking to Microsoft Graph. First, it fetches your profile information, so it knows who you are. Then, it grabs your upcoming calendar events—just a couple of them to keep things simple. The app sends requests to Microsoft Graph using the token you provided during authentication, and voilà, your data is ready to use!

```python
# Use the token to get your profile data
headers = {"Authorization": f"Bearer {self.access_token}"}

# Fetch user profile
user_response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
if user_response.ok:
    user = user_response.json()
    print(f"Welcome, {user['displayName']}!")
else:
    print(f"Failed to fetch user info: {user_response.status_code}")

# Fetch the next two calendar events
events_response = requests.get("https://graph.microsoft.com/v1.0/me/events", headers=headers)
if events_response.ok:
    events = events_response.json().get("value", [])[:2]
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event['subject']} ({event['start']['dateTime']} - {event['end']['dateTime']})")
else:
    print(f"Failed to fetch calendar events: {events_response.status_code}")
```

### Creating a Calendar Event

That’s easy too! This snippet shows how the app creates a new event for you. Imagine you want to block some time to study for the AZ-204 exam. The app sends the event details to Microsoft Graph, and boom—it’s added to your calendar. If the request succeeds, the app will show the event details back to you. Now you’re all set to focus on what matters!

```python
# Use the token to get access to Microsoft Graph API
headers = {"Authorization": f"Bearer {self.access_token}"}

# Create a new calendar event
event_data = {
    "subject": "Study for the AZ-204 exam",
    "start": {"dateTime": "2023-12-01T15:05:00", "timeZone": "UTC"},
    "end": {"dateTime": "2023-12-01T15:35:00", "timeZone": "UTC"},
    "location": "Wherever you are"},
}

create_event_response = requests.post(
    "https://graph.microsoft.com/v1.0/me/events",
    headers=headers,
    json=event_data,
)

if create_event_response.status_code == 201:
    created_event = create_event_response.json()
    print("Your meeting was created with the following details:")
    print(f"Subject: {created_event['subject']}")
    print(f"Location: {created_event['location']['displayName']}")
    print(f"Start: {created_event['start']['dateTime']}")
    print(f"End: {created_event['end']['dateTime']}")
else:
    print("Failed to create calendar event.")  # Something went wrong with the request
```

**In Summary:**  
This app starts with authentication using the Device Code flow. Once logged in, it fetches your data (like profile info and events) and even helps you create new events on your calendar. It’s like having a mini assistant that works securely with your Microsoft 365 account!

---

## 💡 How to Use This Solution in Your Projects

The Device Code flow is incredibly versatile and can be adapted for various use cases. Here are some examples to spark ideas for your projects:

* **Employee Lounge Dashboard**  
    Inside a company, a wall-mounted digital dashboard in the employee lounge shows daily team schedules, upcoming meetings, and shared events. The Device Code flow allows IT admins to authenticate the device once, enabling it to securely access and display the company’s shared Microsoft 365 calendars.
    
* **Internal Tools**  
    Use this flow for command-line tools that automate Microsoft 365 tasks, such as scheduling team meetings or syncing task lists.
    
* **Custom Integrations**  
    Build webhooks or automation scripts that monitor changes in a user’s calendar and automatically notify relevant stakeholders.
    
* **Third-Party Integrations**  
    Incorporate this authentication method into partner applications that need controlled access to Microsoft 365 data, like shared project planning tools.
    

If you want to explore alternative solutions, consider integrating the same Azure resources with different flows. For example:

* **Use Authorization Code flow** for web applications with a backend server.
    
* **Leverage Client Credentials flow** for background services that need to operate without user interaction.
    

---

## 🔑 Key Takeaways

1. **Device Code Flow** is ideal for secure authentication in environments with limited user input.
    
2. **Microsoft Graph** provides seamless integration with Microsoft 365 resources.
    
3. Azure AD enables flexible authentication strategies to suit various scenarios, from IoT devices to enterprise apps.
    
4. **Azure AD B2C** offers a specialized identity solution for consumer-facing or multi-tenant apps with custom branding.
    

---

## 💻 Let’s Build Together

Thanks for reading! I’d love to connect and see how you use Azure AD + Microsoft Graph in your projects.  
  
Check out the repo: [https://github.com/xmedinavei/az-deviceflow-auth-app](https://github.com/xmedinavei/az-deviceflow-auth-app)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white align="left")](https://linkedin.com/in/xmedinavei)

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white align="left")](https://github.com/xmedinavei)

---

## 📚 Further Reading

* [Azure AD Device Code Flow Documentation](https://learn.microsoft.com/azure/active-directory/develop/v2-oauth2-device-code)
    
* [Microsoft Graph API Overview](https://learn.microsoft.com/graph/api/overview)
    
* [Python MSAL Library](https://github.com/AzureAD/microsoft-authentication-library-for-python)
    
* [App Registration Quickstart](https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app)
    
* [Azure AD B2C Overview](https://learn.microsoft.com/azure/active-directory-b2c/overview)
    

Thanks for reading and happy coding!