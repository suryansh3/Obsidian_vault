---
tags:
  - meta
  - log
---
# Cleanup log - 2026-11-09

Pre-cleanup snapshot: git commit `a183f88` (`git show a183f88:<old path>` restores anything).

Highlights
- Deleted boilerplate daily notes (31 in `01 - Daily`, 30 in `01 Daily` - default values, many with broken `undefined` links, one with merge-conflict markers); kept the 3 customised ones and regenerated today's.
- Restored 41 corrupted Time Garden templates from commit `7a0b2a1` and hardened them against the plugin-load race.
- Removed empty/duplicate folders: `01 - Daily`, `02 - Weekly`, `03 - Monthly`, `06 - Templates`, `07 - Pursuits & Goals`, `00 - AI and ML`, root `Clippings`, root `gemini-scribe`, duplicate dashboards.
- 102 unreferenced images moved to `07 - Archives/Unlinked Attachments` (nothing deleted).

Full operation list
```
MOVE 01 Daily/2026/05-May/2026-05-06-Wednesday.md -> 01 - Journal/Daily/2026/05-May/2026-05-06-Wednesday.md
MOVE 01 Daily/2026/05-May/2026-05-07-Thursday.md -> 01 - Journal/Daily/2026/05-May/2026-05-07-Thursday.md
MOVE 01 Daily/2026/08-August/2026-08-13-Thursday.md -> 01 - Journal/Daily/2026/08-August/2026-08-13-Thursday.md
DELETE 01 Daily
DELETE 01 - Daily
DELETE 02 - Weekly
DELETE 03 - Monthly
DELETE 00 - Dashboard/RPG_Dashboard.md
DELETE 99 - Meta/RPG_Dashboard.md
DELETE 00 - Dashboard/Welcome.md
MOVE 05 - Second Brain & Knowledge/MOC.md -> 00 - Dashboard/MOC.md
MOVE 99 - Meta/Pursuits/Career.md -> 02 - Quests/Pursuits/Career.md
MOVE 99 - Meta/Pursuits/YouTube.md -> 02 - Quests/Pursuits/YouTube.md
MOVE 99 - Meta/Pursuits/Income.md -> 02 - Quests/Pursuits/Income.md
MOVE 99 - Meta/Pursuits/Content_creation.md -> 02 - Quests/Pursuits/Content Creation.md
MOVE 99 - Meta/Areas/Core.md -> 02 - Quests/Areas/Core.md
MOVE 99 - Meta/Areas/Craft.md -> 02 - Quests/Areas/Craft.md
MOVE 99 - Meta/Areas/Intel.md -> 02 - Quests/Areas/Intel.md
MOVE 99 - Meta/Areas/Physical.md -> 02 - Quests/Areas/Physical.md
MOVE 99 - Meta/Areas/Psyche.md -> 02 - Quests/Areas/Psyche.md
MOVE 99 - Meta/Areas/Spiritual.md -> 02 - Quests/Areas/Spiritual.md
MOVE 99 - Meta/Character.md -> 02 - Quests/Character.md
MOVE 99 - Meta/Rewards.md -> 02 - Quests/Rewards.md
DELETE 07 - Pursuits & Goals
MOVE 00 - AI and ML/Python/Untitled.md -> 03 - AI & ML/AI & ML Roadmap.md
DELETE 00 - AI and ML
MOVE 04 - Academics & CS/03. Semester 3rd -> 04 - Academics & CS/Semester 3
MOVE 04 - Academics & CS/Semester 3/02 - Data Structure -> 04 - Academics & CS/Semester 3/Data Structures
MOVE 04 - Academics & CS/Semester 3/03 - IOT -> 04 - Academics & CS/Semester 3/IoT
MOVE 04 - Academics & CS/Semester 3/04 - Probability -> 04 - Academics & CS/Semester 3/Probability & Statistics
MOVE 04 - Academics & CS/Semester 3/06- Digital System Design -> 04 - Academics & CS/Semester 3/Digital System Design
MOVE 04 - Academics & CS/04. Semester 4 -> 04 - Academics & CS/Semester 4
MOVE 04 - Academics & CS/Semester 4/1. COA (Computer Organization and Architecture) -> 04 - Academics & CS/Semester 4/COA
MOVE 04 - Academics & CS/Semester 4/2. DM (Discrete Mathematics ) -> 04 - Academics & CS/Semester 4/Discrete Mathematics
MOVE 04 - Academics & CS/Semester 4/3. OOPJ (Java) -> 04 - Academics & CS/Semester 4/OOPJ (Java)
MOVE 04 - Academics & CS/Semester 4/4. Operating System (OS) -> 04 - Academics & CS/Semester 4/Operating Systems
MOVE 04 - Academics & CS/Semester 4/MID-SEMESTER -> 04 - Academics & CS/Semester 4/Mid-Semester
MOVE 04 - Academics & CS/Semester 4/OOPJ (Java)/LAB -> 04 - Academics & CS/Semester 4/OOPJ (Java)/Lab
MOVE 04 - Academics & CS/Semester 4/OOPJ (Java)/THEORY -> 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory
MOVE 04 - Academics & CS/Semester 4/Operating Systems/LAB -> 04 - Academics & CS/Semester 4/Operating Systems/Lab
MOVE 04 - Academics & CS/05. Semester 5 -> 04 - Academics & CS/Semester 5
MOVE 04 - Academics & CS\Semester 5\CN(L)\DAY-7.md -> 04 - Academics & CS\Semester 5\CN\Lab\DAY-7.md
DELETE 04 - Academics & CS/Semester 5/CN(L)
MOVE 04 - Academics & CS\Semester 5\DAA-lab\24155060-day10-DAA.md -> 04 - Academics & CS\Semester 5\DAA\Lab\24155060-day10-DAA.md
MOVE 04 - Academics & CS\Semester 5\DAA-lab\DAY-5.md -> 04 - Academics & CS\Semester 5\DAA\Lab\DAY-5.md
MOVE 04 - Academics & CS\Semester 5\DAA-lab\DAY-6.md -> 04 - Academics & CS\Semester 5\DAA\Lab\DAY-6.md
MOVE 04 - Academics & CS\Semester 5\DAA-lab\Day1.md -> 04 - Academics & CS\Semester 5\DAA\Lab\Day1.md
MOVE 04 - Academics & CS\Semester 5\DAA-lab\Day2.md -> 04 - Academics & CS\Semester 5\DAA\Lab\Day2.md
MOVE 04 - Academics & CS\Semester 5\DAA-lab\Day3.md -> 04 - Academics & CS\Semester 5\DAA\Lab\Day3.md
MOVE 04 - Academics & CS\Semester 5\DAA-lab\Day4.md -> 04 - Academics & CS\Semester 5\DAA\Lab\Day4.md
MOVE 04 - Academics & CS\Semester 5\DAA-lab\day8.md -> 04 - Academics & CS\Semester 5\DAA\Lab\day8.md
DELETE 04 - Academics & CS/Semester 5/DAA-lab
MOVE 04 - Academics & CS/Projects-Python -> 04 - Academics & CS/Projects
MOVE 04 - Academics & CS/DSA 16 question co-pilot.md -> 04 - Academics & CS/Semester 3/Data Structures/DSA 16 Question Co-Pilot.md
MOVE 05 - Second Brain & Knowledge/SIH.md -> 04 - Academics & CS/Projects/SIH.md
MOVE 99 - Meta/attachments/Assignment3-svp.tex -> 04 - Academics & CS/Semester 5/SVP/Assignment3-svp.tex
MOVE 04 - Academics & CS/Semester 4/OOPJ (Java)/Untitled.md -> 04 - Academics & CS/Semester 4/OOPJ (Java)/Utkarsh - Inheritance Programs.md
MOVE 04 - Academics & CS/Semester 4/Mid-Semester/Untitled.md -> 04 - Academics & CS/Semester 4/Mid-Semester/OOPJ Important Topics & Weightage.md
MOVE 04 - Academics & CS/Semester 4/DBMS/Untitled.md -> 04 - Academics & CS/Semester 4/DBMS/DBMS - SQL Views.md
MOVE 04 - Academics & CS/Semester 4/Operating Systems/Lab/Untitled 2.md -> 04 - Academics & CS/Semester 4/Operating Systems/Lab/OS Lab - Bash Practice Solutions.md
MOVE 04 - Academics & CS/Semester 4/Operating Systems/Assignment-9.md -> 04 - Academics & CS/Semester 4/Operating Systems/OS Assignment-9.md
MOVE 04 - Academics & CS/Semester 4/Operating Systems/Lab/Assignment-5.md -> 04 - Academics & CS/Semester 4/Operating Systems/Lab/OS Assignment-5.md
MOVE 04 - Academics & CS/Semester 4/Operating Systems/Lab/Assignment-6.md -> 04 - Academics & CS/Semester 4/Operating Systems/Lab/OS Assignment-6.md
MOVE 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/Assignment-7.md -> 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/OOPJ Theory Assignment-7.md
MOVE 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/Assignment-9.md -> 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/OOPJ Theory Assignment-9.md
MOVE 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/Assignment.md -> 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/OOPJ Theory - Join, Daemon, Priority.md
MOVE 04 - Academics & CS/Semester 4/COA/ASSIGNMENT.md -> 04 - Academics & CS/Semester 4/COA/COA Assignment.md
MOVE 04 - Academics & CS/Semester 4/DAWR/DAY 1.md -> 04 - Academics & CS/Semester 4/DAWR/DAWR Day 1.md
MOVE 04 - Academics & CS/Semester 5/DAA/Lab/DAY-5.md -> 04 - Academics & CS/Semester 5/DAA/Lab/DAA Lab Day-5.md
MOVE 04 - Academics & CS/Semester 4/Discrete Mathematics/INTRODUCTION.md -> 04 - Academics & CS/Semester 4/Discrete Mathematics/Discrete Mathematics - Introduction.md
MOVE 04 - Academics & CS/Semester 3/IoT/Introduction.md -> 04 - Academics & CS/Semester 3/IoT/IoT - Introduction.md
MOVE 04 - Academics & CS/Semester 4/MLSA CHALLENGE.md -> 04 - Academics & CS/Semester 4/MLSA Challenge.md
DELETE 04 - Academics & CS/Semester 3/Probability & Statistics/Untitled.md
DELETE 04 - Academics & CS/Semester 3/Digital System Design/Untitled 1.md
DELETE 04 - Academics & CS/Semester 4/Discrete Mathematics/Untitled.md
DELETE 04 - Academics & CS/Semester 4/OOPJ (Java)/Theory/Untitled.md
DELETE 04 - Academics & CS/Semester 4/OOPJ (Java)/Untitled 1.md
DELETE 04 - Academics & CS/Semester 4/Operating Systems/Lab/Untitled.md
DELETE 04 - Academics & CS/Semester 4/Operating Systems/Untitled.md
DELETE 04 - Academics & CS/Semester 4/OOPJ (Java)/Lab/Main.java.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 1 - Introduction.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 1 - Introduction.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 10 - Image Segmentation.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 10 - Image Segmentation.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 11 - Color Image Processing.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 11 - Color Image Processing.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 12 - Introduction to Image Compression and Watermarking.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 12 - Introduction to Image Compression and Watermarking.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 2 - Basic Mathematical Operations and Intensity Transformations.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 2 - Basic Mathematical Operations and Intensity Transformations.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 3 - Histogram Processing and Fundamentals of Spatial Filtering.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 3 - Histogram Processing and Fundamentals of Spatial Filtering.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 4 - Spatial Filtering.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 4 - Spatial Filtering.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 5 - Introduction to Fourier Transform.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 5 - Introduction to Fourier Transform.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 6 - Discrete Fourier Transform (DFT).md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 6 - Discrete Fourier Transform (DFT).md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 7 - Image Filtering in Frequency Domain.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 7 - Image Filtering in Frequency Domain.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 8 - Image Restoration In Spatial Domain.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 8 - Image Restoration In Spatial Domain.md
MOVE 05 - Second Brain & Knowledge/Clippings/Digital Image Processing - Part 9 - Image Restoration In Frequency Domain.md -> 05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 9 - Image Restoration In Frequency Domain.md
MOVE 05 - Second Brain & Knowledge/Clippings/New chat.md -> 05 - Second Brain & Knowledge/Clippings/AI Chats/Engineering Economics - Gemini Chat.md
MOVE Clippings/10 Brutal Historical Series Like Game of Thrones You NEED to Watch  Netflix  Top 10 Shows.md -> 05 - Second Brain & Knowledge/Clippings/Misc/10 Brutal Historical Series Like Game of Thrones You NEED to Watch  Netflix  Top 10 Shows.md
MOVE Clippings/10 Websites That Will Make You Smarter Than 99% of People.md -> 05 - Second Brain & Knowledge/Clippings/Self Improvement/10 Websites That Will Make You Smarter Than 99% of People.md
MOVE Clippings/18 Hobbies That Quietly Make Your Life Better.md -> 05 - Second Brain & Knowledge/Clippings/Self Improvement/18 Hobbies That Quietly Make Your Life Better.md
MOVE Clippings/30 Uncomfortable Things to Do Alone (Build Confidence).md -> 05 - Second Brain & Knowledge/Clippings/Self Improvement/30 Uncomfortable Things to Do Alone (Build Confidence).md
MOVE Clippings/500 Cambridge C1 and C2 Advanced vocabulary (Full Course).md -> 05 - Second Brain & Knowledge/Clippings/Self Improvement/500 Cambridge C1 and C2 Advanced vocabulary (Full Course).md
MOVE Clippings/Find The Perfect Hairstyle For Your Face  Best Haircuts For Men.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/Find The Perfect Hairstyle For Your Face  Best Haircuts For Men.md
MOVE Clippings/How I fixed my recessed face using physics (& how you can too...).md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/How I fixed my recessed face using physics (& how you can too...).md
MOVE Clippings/How I Forced My Shoulders To Grow.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/How I Forced My Shoulders To Grow.md
MOVE Clippings/How To Build An Insane V-Taper Body.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/How To Build An Insane V-Taper Body.md
MOVE Clippings/How To Force Your Chest To Grow.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/How To Force Your Chest To Grow.md
MOVE Clippings/How To Force Your Forearms To Grow.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/How To Force Your Forearms To Grow.md
MOVE Clippings/How To Force Your Skinny Arms To Grow.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/How To Force Your Skinny Arms To Grow.md
MOVE Clippings/How to Speak Better Than 99% of People (Complete Framework).md -> 05 - Second Brain & Knowledge/Clippings/Self Improvement/How to Speak Better Than 99% of People (Complete Framework).md
MOVE Clippings/Note Taking & Research Assistant Powered by AI.md -> 05 - Second Brain & Knowledge/Clippings/AI & Tech/Note Taking & Research Assistant Powered by AI.md
MOVE Clippings/The Legal Metrology (Packaged Commodities) Rules, 2011.md -> 05 - Second Brain & Knowledge/Clippings/Misc/The Legal Metrology (Packaged Commodities) Rules, 2011.md
MOVE Clippings/this NOT that mensfashion mensclothes fallfashion fashionadvice mensbrands.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/this NOT that mensfashion mensclothes fallfashion fashionadvice mensbrands.md
MOVE Clippings/Unfair Body Upgrades That Take Less Than 30 Days.md -> 05 - Second Brain & Knowledge/Clippings/Fitness & Looks/Unfair Body Upgrades That Take Less Than 30 Days.md
MOVE Clippings/Why Data, ML and AI Projects Are Completely Useless.md -> 05 - Second Brain & Knowledge/Clippings/AI & Tech/Why Data, ML and AI Projects Are Completely Useless.md
RMDIR Clippings
RMDIR 05 - Second Brain & Knowledge/05 - Handwritten Notes
RMDIR 05 - Second Brain & Knowledge/handwritten-notes
MOVE 05 - Second Brain & Knowledge/WIKI.md -> 05 - Second Brain & Knowledge/LLM Wiki Schema.md
MOVE README.md -> 08 - Resources/Obsidian Git Sync Guide.md
MOVE 99 - Meta/attachments/Devore Solutions Ed9.pdf -> 08 - Resources/Devore Solutions Ed9.pdf
DELETE 07 - Archives/Placeholder.md
DELETE 08 - Resources/Placeholder.md
MOVE 99 - Meta/attachments/Pasted image 20251111230831.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111230831.png
MOVE 99 - Meta/attachments/Pasted image 20251111230838.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111230838.png
MOVE 99 - Meta/attachments/Pasted image 20251111230904.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111230904.png
MOVE 99 - Meta/attachments/Pasted image 20251111230949.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111230949.png
MOVE 99 - Meta/attachments/Pasted image 20251111231006.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111231006.png
MOVE 99 - Meta/attachments/Pasted image 20251111231024.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111231024.png
MOVE 99 - Meta/attachments/Pasted image 20251111231039.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111231039.png
MOVE 99 - Meta/attachments/Pasted image 20251111231218.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111231218.png
MOVE 99 - Meta/attachments/Pasted image 20251111231536.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111231536.png
MOVE 99 - Meta/attachments/Pasted image 20251111232750.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251111232750.png
MOVE 99 - Meta/attachments/Pasted image 20251202080850.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202080850.png
MOVE 99 - Meta/attachments/Pasted image 20251202081035.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081035.png
MOVE 99 - Meta/attachments/Pasted image 20251202081219.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081219.png
MOVE 99 - Meta/attachments/Pasted image 20251202081351.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081351.png
MOVE 99 - Meta/attachments/Pasted image 20251202081442.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081442.png
MOVE 99 - Meta/attachments/Pasted image 20251202081544.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081544.png
MOVE 99 - Meta/attachments/Pasted image 20251202081651.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081651.png
MOVE 99 - Meta/attachments/Pasted image 20251202081737.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081737.png
MOVE 99 - Meta/attachments/Pasted image 20251202081816.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081816.png
MOVE 99 - Meta/attachments/Pasted image 20251202081853.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081853.png
MOVE 99 - Meta/attachments/Pasted image 20251202081925.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202081925.png
MOVE 99 - Meta/attachments/Pasted image 20251202082026.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082026.png
MOVE 99 - Meta/attachments/Pasted image 20251202082044.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082044.png
MOVE 99 - Meta/attachments/Pasted image 20251202082051.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082051.png
MOVE 99 - Meta/attachments/Pasted image 20251202082130.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082130.png
MOVE 99 - Meta/attachments/Pasted image 20251202082224.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082224.png
MOVE 99 - Meta/attachments/Pasted image 20251202082254.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082254.png
MOVE 99 - Meta/attachments/Pasted image 20251202082430.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082430.png
MOVE 99 - Meta/attachments/Pasted image 20251202082608.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082608.png
MOVE 99 - Meta/attachments/Pasted image 20251202082712.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082712.png
MOVE 99 - Meta/attachments/Pasted image 20251202082729.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082729.png
MOVE 99 - Meta/attachments/Pasted image 20251202082745.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202082745.png
MOVE 99 - Meta/attachments/Pasted image 20251202092815.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202092815.png
MOVE 99 - Meta/attachments/Pasted image 20251202092917.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202092917.png
MOVE 99 - Meta/attachments/Pasted image 20251202092954.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202092954.png
MOVE 99 - Meta/attachments/Pasted image 20251202092959.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202092959.png
MOVE 99 - Meta/attachments/Pasted image 20251202093104.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251202093104.png
MOVE 99 - Meta/attachments/Pasted image 20251205211428.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251205211428.png
MOVE 99 - Meta/attachments/Pasted image 20251205225508.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251205225508.png
MOVE 99 - Meta/attachments/Pasted image 20251208175023.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251208175023.png
MOVE 99 - Meta/attachments/Pasted image 20251208175051.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251208175051.png
MOVE 99 - Meta/attachments/Pasted image 20251208175111.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251208175111.png
MOVE 99 - Meta/attachments/Pasted image 20251208180101.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251208180101.png
MOVE 99 - Meta/attachments/Pasted image 20251208184056.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251208184056.png
MOVE 99 - Meta/attachments/Pasted image 20251209131003.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251209131003.png
MOVE 99 - Meta/attachments/Pasted image 20251209134825.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251209134825.png
MOVE 99 - Meta/attachments/Pasted image 20251211151449.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211151449.png
MOVE 99 - Meta/attachments/Pasted image 20251211151554.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211151554.png
MOVE 99 - Meta/attachments/Pasted image 20251211151756.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211151756.png
MOVE 99 - Meta/attachments/Pasted image 20251211151908.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211151908.png
MOVE 99 - Meta/attachments/Pasted image 20251211152025.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211152025.png
MOVE 99 - Meta/attachments/Pasted image 20251211152132.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211152132.png
MOVE 99 - Meta/attachments/Pasted image 20251211152230.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211152230.png
MOVE 99 - Meta/attachments/Pasted image 20251211152327.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211152327.png
MOVE 99 - Meta/attachments/Pasted image 20251211152444.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211152444.png
MOVE 99 - Meta/attachments/Pasted image 20251211152542.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211152542.png
MOVE 99 - Meta/attachments/Pasted image 20251211152800.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211152800.png
MOVE 99 - Meta/attachments/Pasted image 20251211153330.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211153330.png
MOVE 99 - Meta/attachments/Pasted image 20251211153439.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211153439.png
MOVE 99 - Meta/attachments/Pasted image 20251211153944.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211153944.png
MOVE 99 - Meta/attachments/Pasted image 20251211154048.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211154048.png
MOVE 99 - Meta/attachments/Pasted image 20251211154146.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251211154146.png
MOVE 99 - Meta/attachments/Pasted image 20251212141845.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251212141845.png
MOVE 99 - Meta/attachments/Pasted image 20251212145118.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251212145118.png
MOVE 99 - Meta/attachments/Pasted image 20251216232907.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251216232907.png
MOVE 99 - Meta/attachments/Pasted image 20251216233015.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251216233015.png
MOVE 99 - Meta/attachments/Pasted image 20251216233144.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251216233144.png
MOVE 99 - Meta/attachments/Pasted image 20251218224956.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251218224956.png
MOVE 99 - Meta/attachments/Pasted image 20251218225319.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251218225319.png
MOVE 99 - Meta/attachments/Pasted image 20251218234035.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251218234035.png
MOVE 99 - Meta/attachments/Pasted image 20251218234053.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251218234053.png
MOVE 99 - Meta/attachments/Pasted image 20251218234109.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251218234109.png
MOVE 99 - Meta/attachments/Pasted image 20251218234123.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251218234123.png
MOVE 99 - Meta/attachments/Pasted image 20251218234134.png -> 07 - Archives/Unlinked Attachments/Pasted image 20251218234134.png
MOVE 99 - Meta/attachments/Pasted image 20260106215702.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260106215702.png
MOVE 99 - Meta/attachments/Pasted image 20260106215956.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260106215956.png
MOVE 99 - Meta/attachments/Pasted image 20260109134501.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260109134501.png
MOVE 99 - Meta/attachments/Pasted image 20260112202619.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260112202619.png
MOVE 99 - Meta/attachments/Pasted image 20260112211020.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260112211020.png
MOVE 99 - Meta/attachments/Pasted image 20260112211233.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260112211233.png
MOVE 99 - Meta/attachments/Pasted image 20260112211929.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260112211929.png
MOVE 99 - Meta/attachments/Pasted image 20260218233253.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260218233253.png
MOVE 99 - Meta/attachments/Pasted image 20260225212804.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225212804.png
MOVE 99 - Meta/attachments/Pasted image 20260225213125.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225213125.png
MOVE 99 - Meta/attachments/Pasted image 20260225213640.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225213640.png
MOVE 99 - Meta/attachments/Pasted image 20260225223445.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225223445.png
MOVE 99 - Meta/attachments/Pasted image 20260225223451.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225223451.png
MOVE 99 - Meta/attachments/Pasted image 20260225223457.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225223457.png
MOVE 99 - Meta/attachments/Pasted image 20260225223505.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225223505.png
MOVE 99 - Meta/attachments/Pasted image 20260225223512.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225223512.png
MOVE 99 - Meta/attachments/Pasted image 20260225223529.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225223529.png
MOVE 99 - Meta/attachments/Pasted image 20260225223540.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225223540.png
MOVE 99 - Meta/attachments/Pasted image 20260225231557.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225231557.png
MOVE 99 - Meta/attachments/Pasted image 20260225231608.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225231608.png
MOVE 99 - Meta/attachments/Pasted image 20260225231616.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225231616.png
MOVE 99 - Meta/attachments/Pasted image 20260225231625.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225231625.png
MOVE 99 - Meta/attachments/Pasted image 20260225231632.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260225231632.png
MOVE 99 - Meta/attachments/Pasted image 20260322222816.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260322222816.png
MOVE 99 - Meta/attachments/Pasted image 20260823225331.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260823225331.png
MOVE 99 - Meta/attachments/Pasted image 20260823225344.png -> 07 - Archives/Unlinked Attachments/Pasted image 20260823225344.png
MOVE 99 - Meta/attachments/Screenshot 2025-12-11 160138.png -> 07 - Archives/Unlinked Attachments/Screenshot 2025-12-11 160138.png
MOVE 99 - Meta/attachments/ED-202511130109.excalidraw.md -> 07 - Archives/Unlinked Attachments/ED-202511130109.excalidraw.md
Orphans archived: 101
DELETE 06 - Templates
MOVE 99 - Meta/00 - Templates/(TEMPLATE) Unique.md -> 06 Templates/Notes/Unique Note.md
DELETE 99 - Meta/00 - Templates
MOVE 99 - Meta/Agent-Sessions -> 99 - Meta/Gemini Scribe/Agent-Sessions
MOVE 99 - Meta/Prompts -> 99 - Meta/Gemini Scribe/Prompts
MOVE gemini-scribe/rag-index-cache.json -> 99 - Meta/Gemini Scribe/rag-index-cache.json
MOVE 99 - Meta/Scheduled-Tasks -> 99 - Meta/Gemini Scribe/Scheduled-Tasks
DELETE gemini-scribe
DELETE 99 - Meta/Skills
DELETE 99 - Meta/Background-Tasks
DELETE 99 - Meta/Areas
DELETE 99 - Meta/Pursuits
DELETE desktop.ini
```
