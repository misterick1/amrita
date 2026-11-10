# Discord Identity Verification & Privacy Guide
## Why Discord is Asking for Your Identity
Discord utilizes Stripe as a secure third-party identity verification provider. You are typically prompted to complete this verification for one of two major reasons: [1] 

   1. Age Assurance System: Starting in early 2026, Discord rolled out a global age assurance rollout to separate users into "Teen" (13–17) and "Adult" (18+) experiences to comply with child safety laws. While a machine-learning model automatically places over 90% of users into an age group based on account activity, you will be prompted to manually verify if the system lacks confidence in your age and you attempt to view age-restricted channels, toggle sensitive content filters, or adjust strict privacy settings. [2, 3, 4, 5] 
   2. Bot Developer Verification: If you develop a Discord bot that is added to more than 100 servers, Discord requires an ID scan through Stripe to verify a real person owns the bot and prevent malicious automated networks. [6, 7] 

For more context on how these requirements apply, you can consult [Discord's Age Group Support Page](https://support.discord.com/hc/en-us/articles/30326565624343-How-to-Confirm-Your-Age-Group-on-Discord).
## How Your Data and Privacy are Handled
Many users are understandably hesitant about uploading a government ID online, especially given historical data breaches affecting third-party support platforms in late 2025. Discord has structured its partnership with Stripe specifically to minimize data exposure: [1, 3, 8, 9] 

| Aspect | Data Handling & Retention Policy |
|---|---|
| What Discord Sees | Discord never receives your name, a copy of your ID, or your biometric photo data. They only receive an "age signal" (e.g., confirming you are "18+") or a verification token. |
| Stripe's Retention | Stripe processes the document images and removes biometric signatures from their system within one year. The text data is only processed to execute the verification requested by Discord. |
| Vendor Obligations | Under Discord's vendor terms, underlying raw ID data submitted via standard age verification is slated for immediate deletion once the transaction completes. |

Review the official [Discord Stripe FAQ](https://support-dev.discord.com/hc/en-us/articles/6226051178775-Stripe-Identity-Verification-FAQ) or the direct [Stripe Identity Privacy FAQ](https://support.stripe.com/questions/stripe-identity-faq) for further legal protections.
## Your Alternative Options
If you are uncomfortable sharing a photo ID, you do not necessarily have to do it, depending on what triggered the prompt: [5, 10] 

* Alternative Verification Methods: If this prompt appeared because of an age check, you can close the window and navigate to User Settings > Account Status on Discord. Depending on your region and device, you may have less invasive options available, including:
* App Store Verification: Share a simple "18+" age range confirmation token tied to your Apple App Store or Google Play Store account with a single tap.
   * Video Selfie: Uses local, on-device facial analysis software to estimate your age without transferring video or biometric files off your phone.
   * Credit Card Verification: Uses Stripe to verify you hold a valid adult credit card without storing card details. [4, 5, 10] 
* Decline & Accept Restrictions: You can click the Decline button at the bottom of your screen. If you choose not to verify, you will retain your friends list, servers, direct messages, and voice chat, but your account will remain restricted from joining NSFW/age-restricted spaces, and you will be unable to turn off certain teen-focused safety features.
[5] 


[1] [https://support-dev.discord.com](https://support-dev.discord.com/hc/en-us/articles/6226051178775-Stripe-Identity-Verification-FAQ)
[2] [https://www.bbc.com](https://www.bbc.com/news/articles/c1d67vdlk1ko)
[3] [https://www.pcmag.com](https://www.pcmag.com/news/discords-controversial-age-checks-are-back-heres-what-the-backlash-changed)
[4] [https://discord.com](https://discord.com/blog/safer-for-teens-same-discord-for-adults)
[5] [https://allaboutcookies.org](https://allaboutcookies.org/discord-age-verification)
[6] [https://www.change.org](https://www.change.org/p/discord-inc-change-the-bot-verification-process-for-discord)
[7] [https://news.ycombinator.com](https://news.ycombinator.com/item?id=27506175)
[8] [https://discord.com](https://discord.com/safety/age-assurance-on-discord-vendors-methods-and-your-data)
[9] [https://www.reddit.com](https://www.reddit.com/r/cybersecurity/comments/1r1oi54/how_concerned_should_we_be_about_discords_new_age/)
[10] [https://support.discord.com](https://support.discord.com/hc/en-us/articles/30326565624343-How-to-Confirm-Your-Age-Group-on-Discord)
