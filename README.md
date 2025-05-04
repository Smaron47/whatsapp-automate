**WhatsApp Bulk Message & Media Sender**

---

## Table of Contents

1. Project Overview
2. Key Features
3. Technology Stack & Module Explanations
4. File Structure
5. Environment Setup & Dependencies
6. Application Configuration
7. GUI Layout & Workflow
8. Functionality Breakdown

   * 8.1 `get_user_data_dir()`
   * 8.2 `send_messages()`
   * 8.3 `attach_and_send_files()`
   * 8.4 `send_images()`
   * 8.5 `update_preview_images()`
   * 8.6 `load_image()`
9. Error Handling & Logging
10. Customization & Extensibility
11. Best Practices
12. Testing & Debugging
13. Future Enhancements
14. Keywords
15. Licensing & Author Information

---

## 1. Project Overview

This desktop application, built with **Tkinter** and **Selenium**, automates sending bulk text messages and media (images/videos) via **WhatsApp Web**. Users input multiple phone numbers and a message, optionally attach files, and the script logs into an existing WhatsApp session in Chrome to dispatch messages programmatically.

**Use Case:** Customer outreach, event invites, notifications in regions where WhatsApp is prevalent.

---

## 2. Key Features

* Send personalized bulk text messages to a list of numbers.
* Attach and send multiple images or videos in one operation.
* Preview attached media within the GUI.
* Maintain an existing WhatsApp Web session via Chrome user data directory.
* Log failed deliveries for later review.

---

## 3. Technology Stack & Module Explanations

* **Tkinter**: GUI framework for input fields, buttons, and image previews.
* **Selenium WebDriver**: Browser automation to interact with WhatsApp Web elements.
* **Pillow (PIL)**: Image processing for thumbnails.
* **os, random, string, time**: Utilities for file paths, delays, and randomness.

---

## 4. File Structure

```plaintext
whatsapp_bulk_sender/
├── bulk_sender.py         # Main application script
├── requirements.txt       # List of dependencies
└── README.md              # (This) Documentation
```

---

## 5. Environment Setup & Dependencies

1. **Python 3.7+**
2. Install required libraries:

   ```bash
   pip install selenium pillow
   ```
3. **Chrome Browser** and matching **chromedriver** in PATH.
4. Ensure WhatsApp Web is logged in on Chrome profile.

---

## 6. Application Configuration

* **`BASE_URL`**: WhatsApp Web URL.
* **`CHAT_URL`**: Template to open chat for a given phone number.
* **`get_user_data_dir()`**: Returns path to Chrome’s Default profile to reuse session.
* **`sleep_duration`**: Random delay (4–7s) to mimic human interaction.

---

## 7. GUI Layout & Workflow

1. **Phone Numbers**: Multiline `Text` widget (one number per line, international format).
2. **Message**: Multiline `Text` widget for message body.
3. **Buttons**:

   * Attach Image/Video
   * Send Messages (text only)
   * Send Images (with optional message)
4. **Media Preview**: Thumbnails of selected files.
5. **Failed List**: `Text` widget logging numbers where sending failed.

---

## 8. Functionality Breakdown

### 8.1 `get_user_data_dir()`

Returns the OS-specific path to Chrome’s user data (`AppData/Local/Google/Chrome/User Data/Default`) for session persistence.

### 8.2 `send_messages()`

1. Reads phone numbers and message text.
2. Launches Chrome with Selenium, navigates to WhatsApp Web.
3. Iterates numbers: opens chat URL, waits for input box, sends keys, presses ENTER.
4. On exception, logs number to `failed_numbers_text`.

### 8.3 `attach_and_send_files()`

Opens file dialog, allows multi-selection. Appends chosen paths to `file_paths_to_send` and refreshes previews.

### 8.4 `send_images()`

1. Reads numbers and optional message.
2. For each number: opens chat URL, clicks Attach, uploads each file via hidden `<input>` element, adds message text (if provided), clicks Send.
3. Logs failures and clears attachments after completion.

### 8.5 `update_preview_images()`

Destroys old preview frame and recreates thumbnails from `file_paths_to_send` using `load_image()` and `ImageTk.PhotoImage`.

### 8.6 `load_image(file_path)`

Uses Pillow to open, resize to 100×100, and convert to `PhotoImage`

---

## 9. Error Handling & Logging

* Broad `try/except` around Selenium interactions to prevent crash on missing elements.
* Failed numbers appended to GUI text box for manual follow-up.
* Silent failures in image preview loading.

---

## 10. Customization & Extensibility

* **Delay Tuning**: Adjust `sleep_duration` or use explicit waits.
* **Group Messaging**: Extend to send via group links.
* **Attachment Types**: Add document or contact attachments.
* **Headless Mode**: Run Chrome headlessly for server-side deployments.

---

## 11. Best Practices

* Validate phone number formats before sending.
* Respect WhatsApp’s policies; avoid spamming.
* Use environment variables for paths and URLs.
* Modularize code into classes for testability.

---

## 12. Testing & Debugging

* **Unit tests**: Mock Selenium’s `WebDriver` and element locators.
* **Integration tests**: Run against a test WhatsApp account.
* **Logs**: Capture browser console logs for troubleshooting.

---

## 13. Future Enhancements

* OAuth login instead of local user data dir.
* Retry logic for transient network failures.
* GUI theme support and responsive resizing.
* Progress indicators for each recipient.

---

## 14. Keywords

```
WhatsApp bulk sender
Tkinter Selenium automation
WhatsApp Web bot
Python bulk messaging
automated media sending
gui whatsapp automation
selenium whatsapp script
pillow image preview
auto whatsapp messages
failed delivery log
bulk message python
```

---

## 15. Licensing & Author Information

**Author:** Smaron Biswas
**Created:** 2022
**License:** MIT License

Free to use, modify, and distribute under the terms of the MIT License.

---

*End of Documentation.*
