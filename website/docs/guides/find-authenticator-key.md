---
title: Find your 2FA setup key
sidebar_label: Find your 2FA setup key
description: Find the TOTP secret or otpauth link for a browser agent in common password managers and authenticator apps, or enter a one-time code instead.
---

# Find your 2FA setup key

If Hermes asks for an **Authenticator key** or an `otpauth://totp/...` link, it wants the saved setup secret that generates your verification codes. It does **not** want the changing six-digit code shown on your phone.

You can skip saving a key. For a single sign-in, open your authenticator, find the matching website and account, and enter its current code in Hermes' masked verification-code prompt. Never paste it into chat.

## Choose what you want to do

| What Hermes asks for | What to provide | Where to put it |
| --- | --- | --- |
| Verification code | The current code from your app, usually six digits | The masked verification-code prompt |
| Authenticator key | A setup key, also called a TOTP secret or seed, or a full `otpauth://totp/...` link | The masked Authenticator key field in Passwords & Logins |
| Approval, passkey or security key | Approve the request or use your device | Complete the action yourself on your device |

**Saving a setup key lets Hermes generate future codes without asking you.** Keep it private like a password. Saving the password and the second-factor secret together removes the separation provided by keeping the authenticator on a separate device. Only do this for accounts you want to automate and where your organization's policy allows it.

Do not paste setup keys, QR codes, vault exports or verification codes into chat. Do not upload them to an online QR decoder. A QR code containing a setup key grants the same access as the key itself.

## Find your app

Menu labels can differ by platform and app version. Look for the saved entry for the **website you are signing into**, not your password manager's own account.

### 1Password

Prefer the existing integration. If the 1Password CLI is installed and signed in, Hermes can use a website Login item's saved one-time password without you copying its secret. See [Passwords & Logins](../user-guide/features/credential-vault.md#already-using-1password-or-bitwarden).

To find the setup value manually:

1. Unlock 1Password and search for the website.
2. Open the matching **Login** item. Check the username if you have several accounts.
3. Select **Edit** and find the existing **One-Time Password** field.
4. Copy its stored value if your version exposes it. This is a setup secret or an `otpauth://totp/...` link, not the rotating code in the normal item view.
5. Paste it only into Hermes' masked **Authenticator key** field. Cancel the edit in 1Password so you do not accidentally change the item.

If there is no One-Time Password field, that item does not have the authenticator secret. Check your authenticator app or use the website setup process below. Do not export your whole vault to retrieve one key.

[1Password's guide to one-time passwords](https://support.1password.com/one-time-passwords/)

### Bitwarden Password Manager

Hermes can also use saved TOTP keys through the Bitwarden CLI integration. Copying a key into Hermes is optional when that integration is available.

1. Unlock Bitwarden and open the matching website login.
2. Select **Edit**.
3. Find **Authenticator key**. On mobile, look for the authenticator setup/edit control in the Edit view.
4. Copy the existing setup value, revealing it if your app offers that control. Keep the entire URI if it starts with `otpauth://totp/`.
5. Paste it into Hermes' masked **Authenticator key** field. Cancel the Bitwarden edit without changing anything.

Bitwarden distinguishes storing a key from generating codes. A plan restriction on displaying codes does not necessarily mean the saved key is missing.

[Bitwarden's integrated authenticator guide](https://bitwarden.com/help/authenticator-keys)

### Bitwarden Authenticator

This is a separate app from Bitwarden Password Manager.

1. Open the app and find the matching website and username.
2. For a code stored locally, long-press the entry and select **Edit**.
3. Find its **Key**. Copy the existing value if the edit screen allows it.
4. If the entry uses non-default Algorithm, Refresh period or Number of digits, preserve those settings in a full TOTP URI rather than copying only the key.
5. For an entry synced from Password Manager, open and edit the login in Password Manager instead.

[Bitwarden Authenticator's edit instructions](https://bitwarden.com/help/bitwarden-authenticator)

### Proton Pass

1. Unlock Proton Pass and open the matching website login.
2. Select **Edit**.
3. Find **2FA secret (TOTP)**. Copy the existing setup value if your app exposes it, not the code shown in the normal login view.
4. Paste the value into Hermes' masked **Authenticator key** field.
5. Cancel the Proton Pass edit without modifying the saved login.

If your version only displays codes and does not expose the saved secret, use a one-time code or the website setup process below.

[Proton Pass's 2FA guide](https://proton.me/support/pass-2fa)

### Apple Passwords / iCloud Keychain

For a single sign-in:

1. Open **Passwords** and unlock it.
2. Find the website and matching account.
3. Copy the **Verification Code** and enter it in Hermes' masked verification-code prompt.

Apple documents adding setup keys and copying generated codes, but that does not guarantee your version exposes an existing setup secret. Do not assume **Edit → Set Up Code** reveals the old key. If you cannot find the original secret, use the website setup process below.

[Apple's verification-code guide for Mac](https://support.apple.com/guide/passwords/mchl873a6e72)

### Google Authenticator

For a single sign-in, open the app, find the website and account, and type the current code in the masked prompt.

Google offers **Menu → Transfer codes → Export codes**. Older versions may call these **Transfer accounts → Export accounts**. This generates transfer QR codes for moving entries between installations. Those QR codes use Google's migration format, not a normal per-account `otpauth://totp/...` link. **Do not paste a migration link into Hermes' Authenticator key field.**

For an easy setup without handling export files or decoding migration QR codes, use the website setup process below. Keep your existing Google Authenticator entry until you have verified the new setup.

[Google's Authenticator and transfer instructions](https://support.google.com/accounts/answer/1066447)

### Microsoft Authenticator

1. Open Authenticator and select the matching account.
2. If it shows a rotating verification code, enter that code in Hermes' masked prompt.
3. If it asks you to approve a sign-in or match a number, complete that action on your device instead.

Microsoft's documented backup/restore process restores accounts into Microsoft Authenticator. It is not a way to obtain an `otpauth://totp/...` link for Hermes. For a reusable TOTP setup, use the website's security settings below if the service and your organization allow it.

Work or school accounts may require Microsoft Authenticator push approvals or device registration. Do not replace those with TOTP unless your administrator permits it.

[Microsoft's backup guide](https://support.microsoft.com/en-us/authenticator/back-up-your-accounts-in-microsoft-authenticator)

### Authy

Authy does not support exporting account tokens to other apps.

For a single sign-in, open the account in Authy and enter its current code in Hermes' masked prompt. For automated TOTP sign-ins, obtain a new setup key from the website using the process below. Authy-specific authentication or push approvals may not have a transferable TOTP key.

[Twilio's explanation of Authy's export limitation](https://help.twilio.com/articles/19753420684059-Export-or-Import-Tokens-in-the-Authy-app-Not-Supported)

## If the app cannot show your key

The website that issued the authenticator can provide a setup key when you enroll or replace an authenticator. It usually does not show the existing key after enrollment.

1. Sign in to the website yourself using your working authenticator. Keep that session open.
2. Check that you have a working recovery method. Store any recovery codes privately, not in chat.
3. Open **Account settings → Security → Two-factor authentication**. The site may call it **Two-step verification** or **Multi-factor authentication**.
4. Look for **Add authenticator**, **Change authenticator**, **Replace app** or **Set up another device**. Prefer adding a method over disabling your only working method.
5. When the site shows a QR code, select **Can't scan?**, **Enter manually**, **Setup key** or a similar option to see the text secret.
6. Save that secret in your authenticator and, only if you want automated sign-ins, in Hermes' masked **Authenticator key** field. A standard enrollment QR contains the same secret plus its settings.
7. Complete the website's confirmation using a code from the newly configured authenticator.
8. Test a fresh sign-in before deleting the old entry. Replacing the authenticator may invalidate the old secret, so update every copy you intend to keep using.

If the site requires disabling 2FA first, stop until you have a tested recovery method and understand how to re-enable it. For managed accounts, ask your administrator. You do not need to change your 2FA setup just to let Hermes finish one sign-in.

## Save it in Hermes

1. Open **Settings → Passwords & Logins → Add** and choose a login. Save it for the actual login origin, including `https://` and the correct host.
2. Enter your login details in the masked form. Paste the setup secret or full TOTP link into **Authenticator key**.
3. Save. The item should show **2FA auto**.
4. Ask Hermes to sign into that site and verify it completes the code challenge. Do not delete your working authenticator or recovery methods.

The interactive CLI alternative is `hermes vault add`. Enter secrets only in its private prompts, never as command-line arguments.

You do not need to construct a URI when you already have a standard setup key. Hermes accepts a bare Base32 secret. If you have a full URI, keep it intact so non-default settings survive. Its shape is:

```text
otpauth://totp/SERVICE:ACCOUNT?secret=YOUR_BASE32_SETUP_KEY&issuer=SERVICE&algorithm=SHA1&digits=6&period=30
```

This is a template, not a usable credential. SHA1, six digits and a 30-second period are common defaults, not values to force onto every account. For an app that exposes only a key and separate settings, use those actual settings when creating a URI. An `otpauth://hotp/...` counter-based token is not a supported TOTP key.

## If it does not work

- **Only have six digits?** That is a one-time code. Enter it in the verification-code prompt, not the Authenticator key field. You cannot recover the secret from it.
- **Have a recovery code?** It is a separate emergency sign-in method, not a TOTP secret. Keep it out of the Authenticator key field.
- **Invalid link?** Use a bare setup key or a link starting with `otpauth://totp/`. Google migration links and encrypted backups are different formats.
- **The code is rejected?** Confirm the website and username, enable automatic date and time on both the authenticator device and the machine running Hermes, and preserve the original algorithm, digits and period. If you replaced the authenticator, the old key may no longer work.
- **Prompt asks for approval or a passkey?** Complete it on your device. There may be no TOTP secret to find.
- **Accidentally shared a secret?** Replace the authenticator in the website's security settings and update your private copies. Deleting the message alone does not revoke the secret.
