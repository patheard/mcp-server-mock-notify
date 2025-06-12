# 🎷 MockNotifyService MCP Server 🚀

> **The coolest notification orchestra conductor in town!** 🎵

Transform your AI assistant into a **notification maestro** with this blazing-fast Model Context Protocol (MCP) server! 🔥 Seamlessly orchestrate emails, SMS, templates, and user management like a true digital virtuoso.

## ✨ Features That'll Blow Your Mind

### 🛠️ Your Notification Toolkit Arsenal

🔐 **1. User Management** - *Your VIP Access Pass*
   - 🎫 `signup_user` - Roll out the red carpet for new users & get that golden API key!

🏗️ **2. Service Management** - *Build Your Empire*
   - 🚀 `create_service` - Launch your notification rocket ship
   - 📋 `get_services` - Survey your notification kingdom

🎨 **3. Template Management** - *Craft Masterpieces*
   - ✨ `create_template` - Design stunning, reusable message art
   - 🎭 `get_templates` - Browse your template gallery

📨 **4. Notification Delivery** - *Send Like a Boss*
   - 💌 `send_email_notification` - Deliver beautiful emails with style
   - 📱 `send_sms_notification` - Fire off SMS messages at lightspeed

📊 **5. Message Tracking** - *Stay in the Loop*
   - 🔍 `get_message_status` - Track your messages like a digital detective
   - 📈 `get_messages` - View your entire message empire

💓 **6. System Health** - *Keep the Beat Going*
   - 🏥 `health_check` - Monitor your service's vital signs

🎯 **7. Workflow Automation** - *The Grand Finale*
   - 🎪 `complete_notification_workflow` - One-click magic from signup to delivery!

## 🚀 Installation - *Get This Party Started!*

**Ready to rock?** Let's get you up and running in no time! 🎸

1. **Grab the dependencies** (like collecting your band members):
```bash
pip install -r requirements.txt
```

2. **Fire up the MCP server** (let the music begin!):
```bash
python server.py
```

*Boom! 💥 You're now conducting the notification symphony!*

## ⚙️ Configuration - *Fine-Tune Your Instrument*

🌟 **Default Setup**: We're jamming with the remote MockNotifyService at `https://notify.ai-jam.cdssandbox.xyz` 

🎛️ **Want to change the beat?** Just override with a different `base_url` parameter in any tool call!

## 🎵 Usage Examples - *Let's Make Some Magic!*

### 🎭 The Classic 5-Step Dance

**Follow these killer moves to notification stardom:**

**🎬 Step 1: Roll Out the Red Carpet**
```python
# Welcome your new superstar user!
signup_user("rockstar@example.com", "secret123")
```

**🏗️ Step 2: Build Your Empire**
```python
create_service("🚀 My Awesome App", "your-golden-api-key", "Mind-blowing notifications")
```

**🎨 Step 3: Craft Your Masterpiece**
```python
create_template(
    "🌟 Epic Welcome Email", 
    "Welcome to the revolution!", 
    "Hey superstar! 🎉 Ready to change the world?", 
    "your-service-id", 
    "your-golden-api-key"
)
```

**📨 Step 4: Launch That Message!**
```python
send_email_notification("template-id", "lucky-recipient@example.com", "your-golden-api-key")
```

**🕵️ Step 5: Track Like a Pro**
```python
get_message_status("message-id", "your-golden-api-key")
```

### 🎪 The One-Click Wonder - *For When You're Feeling Lazy*

**Why do 5 steps when you can do 1?** Use our magical workflow tool:

```python
complete_notification_workflow(
    user_email="future-legend@example.com",
    user_password="topsecret456", 
    service_name="🌈 Dream Service",
    service_description="Making dreams come true, one notification at a time",
    template_name="✨ Magical Welcome",
    template_subject="🎊 You're In!",
    template_body="Welcome to the most amazing experience of your life! 🚀",
    recipient_email="about-to-be-amazed@example.com"
)
```

*Bam! 💥 Everything done in one epic swoop!*

## 🔑 API Key Management - *Your Golden Tickets*

🎫 **The VIP Pass System:**
- 🌟 API keys are your **golden tickets** - handed out when users join the party
- 🔒 **Guard them with your life!** Store securely for all your future API adventures
- 👑 Each user gets their own **unique key** - their personal backstage pass to services, templates, and messages

## 🛡️ Error Handling - *We've Got Your Back*

**No worries, we handle the drama!** 🎭

✅ **Success Stories**: Beautiful JSON responses with all the data you crave  
❌ **Plot Twists**: Clear error messages and HTTP status codes when things go sideways  
🌐 **Network Hiccups**: We catch those pesky connection issues and serve them up as friendly error messages

*Because nobody likes mysterious crashes!* 💪

## 🌍 Remote Hosting - *Living in the Cloud*

**Our MCP server is a cloud native superstar!** ☁️ 

Dancing with the remotely hosted MockNotifyService, providing:
- 🔐 **VIP Authentication** & API key magic
- 🏗️ **Service & Template Wizardry**
- 📧 **Email & SMS Lightning Delivery**
- 📊 **Message Detective Tracking**
- 💓 **24/7 Health Monitoring**

## 🤖 AI Assistant Integration - *The Ultimate Partnership*

**Transform your AI assistant into a notification superhero!** 🦸‍♂️

**Superpowers Unlocked:**
- 🏗️ **Build complete notification empires** from scratch
- 📨 **Send personalized messages** to thousands like a boss
- 🔍 **Track delivery & engagement** like a digital detective
- 🎨 **Manage multiple services & templates** like a content curator
- 🎫 **Handle user registration & authentication** seamlessly

🎼 **The Symphony of Simplicity**: Our tools are like LEGO blocks - simple pieces that build incredible notification masterpieces!