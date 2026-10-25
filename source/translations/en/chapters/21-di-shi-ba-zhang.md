---
id: di-shi-ba-zhang
num: 18
part: jin-jie-pian
nav: Chapter 18: Data Backup and Migration
toc: default
kind: chapter
---

### Chapter 18: Data Backup and Migration

{class="chapter-intro mb-4"}
Stored on app servers, available by re-logging in on a new phone

#### : WeChat friend list, Taobao orders, transaction records in banking apps. These are stored on the corresponding company's servers, not on your phone.

In a gray area, requiring special handling

- <strong>: WeChat chat history (although WeChat servers store it, you can't download it from the server yourself), device credentials bound to mobile banking, keys in two-step verification apps (like Google Authenticator).</strong> So what you need to focus on protecting is the first and third categories.
- <strong>2. Full Phone Backup: Get Everything in One Go</strong> A full phone backup is like taking a complete "snapshot" of your phone—current system settings, home screen layout, app data, photos, contacts, all packaged up.
- <strong>Option 1: Local Computer Backup (Most Reliable, Recommended for People with Computers)</strong> iPhone

: Connect your phone to the computer with a data cable, open iTunes (older Windows version) or Finder (Mac), and select "Back Up Now" on the device page. Note: check "Encrypt backup", otherwise passwords and health data won't be included.

#### Android

: Each brand has its own computer software, such as Huawei Phone Assistant, Xiaomi Assistant, Samsung Smart Switch. Connect to the computer and follow the instructions.

##### The benefit of computer backup is that you don't need to pay for cloud space, and the restore speed is much faster than cloud restore. The downside is that you need to remember to plug in and back up periodically—most people can't manage this.

- <strong>Android</strong>: Each brand's cloud has backup functionality. Huawei phones search "cloud backup" in Settings, Xiaomi goes to "Xiaomi Cloud Service", OPPO/vivo similarly. There's also a Google-built backup (Settings → System → Backup)—turn this on too.

##### The biggest benefit of cloud backup is "you don't have to worry about it"—it's automatic. The biggest downside is that restoring takes a long time to download, and the free space is usually not enough.

- <strong>iPhone</strong> Full phone backup is the safety net, but some things are too important and deserve a separate extra copy:
- <strong>Android</strong> Dual insurance plan
- : Enable iCloud Photos/Google Photos auto-sync, and every few months manually copy photos to your computer or external hard drive. This way, one copy in the cloud, one copy locally—mutual backup.

#### Free plan

: Google Photos gives 15GB for free, can be set to "compressed quality" to save space. Or every month, use a data cable to copy all photos to your computer.

##### Contacts (Easily Overlooked but Extremely Important)

- <strong>iPhone contacts sync with iCloud by default—as long as sync is on, no extra backup needed. But if you want to be safer, you can export a vCard file from iCloud.com and save it on your computer.</strong> Android contacts usually sync with Google or brand cloud. Go to the Contacts app settings to export a .vcf file—that's a complete backup.
- <strong>WeChat Chat History (Handle Separately, Top Priority)</strong> This must be discussed separately, because WeChat chat history is often incomplete in full phone backups, and phone migration tools simply can't handle it.

##### Method 1: Migrate to new phone

- . WeChat → Me → Settings → General → Chat History Migration &amp; Backup → Migrate → Migrate to Phone/Tablet. Connect both old and new phones to the same Wi-Fi, scan the QR code to transfer. Note: Don't log out of WeChat on the old phone until migration is complete.
- Method 2: Back up to computer

##### . Install WeChat PC version on your computer, three bars in the bottom left → Migration &amp; Backup → Backup &amp; Restore → Back up chat history to computer. Afterward, when you change phones, you can restore it to the new phone.

Method 3: Back up to cloud

- <strong>. WeChat also supports backing up to iCloud or phone cloud space, but note: this backup can only be restored on your current phone, not cross-device. To change phones, you still need to use the first two methods.</strong>4. Phone Replacement Guide: From Old Phone to New Phone
- <strong>Getting a new phone is a happy event, but if the data doesn't transfer over, it becomes a headache. Three scenarios, handled separately:</strong> Same Brand Upgrade (Simplest)
- <strong>iPhone → New iPhone</strong>: When turning on and activating, place the old phone nearby, and "Quick Start" will automatically pop up. Use the old phone to scan the pattern on the new phone. All data, settings, and app layout will be transferred intact, including Wi-Fi passwords. Takes about 20-30 minutes.

#### Android same brand

: Use the brand's built-in phone replacement tool. Huawei uses "Phone Clone", Xiaomi uses "Xiaomi Phone Transfer", OPPO uses "Phone Move", vivo uses "EasyShare". The steps are similar: install the same app on both old and new phones, scan to connect, check what to transfer, start.

##### Cross-Brand Phone Replacement (Android to Android, Different Brands)

- <strong>Use third-party phone replacement tools or the old brand's built-in replacement app (most brands' replacement apps also support transferring to other Android phones). What can be transferred: contacts, photos, text messages, call logs, some apps. What can't be transferred: in-app login status (you need to re-login), WeChat chat history (use WeChat's own migration feature).</strong> Cross-Platform Phone Replacement (Android to iPhone, or Vice Versa)
- <strong>Android → iPhone</strong>: Apple has a "Move to iOS" app. Download it on your Android phone, and when activating the new iPhone, select "Move Data from Android". Can transfer contacts, photos, text messages and other basic data, but app data can't be transferred. WeChat chat history still needs WeChat's own migration feature.

##### iPhone → Android

: Each Android brand has corresponding migration tools, but honestly, cross-platform migration experience isn't as good as same-platform. Do the most important things first: export contacts, back up photos, migrate WeChat chat history. Take your time with the rest.

##### 5. The Golden Rule of Backup: The 3-2-1 Principle

- <strong>This is a classic principle in the data security field, simple and easy to remember:</strong>3
- <strong>: Keep at least three copies of important data (one original, two backups).</strong>2

#### : Use two different storage media for backups (e.g., one in the cloud, one on an external hard drive).

1

- <strong>: At least one backup should be in a different physical location (to prevent fire, theft, etc. from destroying all data at once).</strong> For ordinary people, achieving "one in the cloud, one on the computer" is already quite good. Don't make it too complicated—the key is that you actually do it.
- <strong>Special Attention for WeChat Chat History</strong> WeChat chat history cannot be migrated by any phone replacement tool! It's not covered by full phone backup. You must use WeChat's built-in "Chat History Migration" feature, or back up to the computer version of WeChat. Many people discover after getting a new phone that all chat history is gone—and by then it's too late. The old phone may have already been factory reset.
- <strong>Practice: Do a Complete Backup Drill</strong> Check whether iCloud Backup or brand cloud backup is enabled, confirm the last backup time.

Manually back up photos: Use a data cable to connect to the computer, copy the DCIM and Pictures folders to the computer.

::: div .warning-box .rounded-lg .p-4 .mt-4
{class="font-semibold"}
<i class="fas fa-exclamation-triangle mr-2"></i>Back up contacts: iPhone users export vCard from iCloud.com; Android users export .vcf file in Contacts app settings.

{class="mt-1"}
Back up WeChat chat history: Open WeChat → Me → Settings → General → Chat History Migration &amp; Backup → Back up to computer.
:::

{class="mt-1"}
Copy the exported contacts vcf and photo folders to an external hard drive or USB drive, completing the "one offline copy elsewhere" of the 3-2-1 rule.
