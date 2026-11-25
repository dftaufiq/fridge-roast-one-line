# Leaderboard analysis — Fridge Roast: One Line, Biggest Laugh

Slug: `u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb`
Prize: $5 (1st $2, 2nd $2, 3rd $1) · FREE entry · 96 submissions at check time
Deadline: 2026-11-26 22:40 WIB (15:40 UTC) · Result due 2026-12-19
Checked: 2026-11-25 ~14:15 WIB

## BLIND bounty — no real top-10 exists

`GET /api/competitions/<slug>/leaderboard?rows=all` returns `scores_visible: false`,
`placements_held: true`, 0 entries (saved as `leaderboard.json`). Per
rank-recovery §10j, this file instead holds: (a) RULES.txt judge criteria +
heat/playoff/cut numbers, (b) public submission titles on the bounty page
(crowded angles — to EXECUTE BETTER, not avoid blindly), (c) winner artifacts
of similar finalized one-liner bounties via the leaderboard API.

## (a) RULES.txt — judge criteria + heat numbers (read in full)

Judge brief (lexicographic — criterion 1 first, then 2, ...):
1. The line is a roast of a smart fridge, joke aimed at the fridge itself, its
   app, its firmware or its ice maker; a non-roast loses to any roast.
2. The punchline lands: the line builds to a turn or a surprise that gets a
   laugh on the first read.
3. The joke is specific to smart fridges, not a generic kitchen-appliance gag
   that would work on any gadget.
4. Wording is tight: every word earns its place inside 200 chars, no setup
   the punchline does not need.
5. The angle is fresh: it avoids the obvious cracks about the fridge ordering
   groceries or watching you that most writers reach for first.
"A line that explains its own joke has already lost. Length for its own sake
does not count."

Scoring: each game = 2 calls (both orders); each call gives the winner
0.5 + margin/10 (0.6 at margin 1 up to 1.0 at margin 5). A close call counts
for little, a decisive one for a full win — pick the line that wins DECISIVELY.

### The 3 heat numbers (RULES.txt §Heats)

- **Final heat size: top 500** dev/round standings ("The seats are exactly 500").
- **Playoff size: top 5** after 3 Swiss rounds (each pair plays one more game).
- **Interim cut: 500** each round ("each interim round draws its own cut of
  500 on the standings of the judged round before it (the first round plays
  the whole field)… each cut entry keeping its score in that round").
- Rounds: R1 cutoff 2026-11-25 17:48:42 UTC (2026-11-26 00:48 WIB), R2
  2026-11-26 04:44:21 UTC (11:44 WIB), final at deadline 15:40 UTC (22:40 WIB).
- **Operational target: be inside the top-500 cut in R1.** Below the cut the
  score FREEZES and the field keeps growing (+34% median/round in past blind
  bounties) — an entry outside the R1 cut is mathematically dead. Dev rank
  decays as new entries arrive, so target margin ABOVE the cut, not the cut
  itself. Tie-breaks: playoff head-to-head, then smaller text (fewer bytes),
  then earlier receipt.

## (b) Crowded angles — public submission titles (96 entries)

From `competition.json` (full submission list). Angle census:

- **Firmware update bricks/kills the ice maker — THE most crowded angle**
  (~20 titles): "Fridge Firmware Forgot How to Stay Cold", "Firmware Update vs
  Ice Maker", "Forgot How to Make Ice", "The Firmware Hostage", "Firmware
  Update Ice", "The 3 A.M. Firmware Update", "Fridge Roast: Firmware Bricked
  the Ice Maker", "The Firmware Update Killed the Ice Maker", "My fridge
  installed a firmware update at 3 a.m., rebooted, and now the ice maker only
  dispenses lukewarm water and regret", "...bricked the ice maker, and then
  emailed me a satisfaction survey about it", "...won't work until I accept
  its terms and conditions".
- **Ice maker on strike / one cube / subscription / terms** (~10): "One Ice
  Cube an Hour", "Ice Maker Union Rep", "The Ice Maker Is on Strike", "Accept
  the Terms, Ice Maker", "Ice as a Service", "Fridge Roast: …only dispenses
  cubes if I subscribe to Premium Chill", "My smart fridge's ice maker got an
  OTA update and now makes one cube an hour, each with release notes".
- **Camera watches / flags the 2 a.m. snack** (~5): "The ice maker jammed, the
  camera flagged my 2 a.m. snack, and the app logged it as 'concerning
  behaviour' — my fridge has now filed three incident reports on me this week",
  "Fridge Roast: 4K Camera, Firmware Revenge".
- **Milk** (~5): "milk betrayal", "The Milk's Emotional Journey", "A Minute's
  Silence for the Milk", "My smart fridge's app needed a firmware update,
  Wi-Fi, and its camera just to tell me my milk expired, while the ice maker
  knew all along and said nothing".
- **App notifications / firmware-update-as-hostage** (several): "My smart
  fridge sent me a push notification", "My fridge updated firmware for 47
  minutes, locked itself for security, thawed my groceries, then blamed me in
  the app: 'Door opened 47 times.' I was on vacation. It was the ice maker."

Implication: firmware-update-bricks-ice-maker and camera-snitch are the
default angles — executing them needs a decisive twist to beat ~20 near-clones.
Criterion 5 EXPLICITLY names "ordering groceries or watching you" as obvious
cracks, so camera-as-watcher lines are penalised by the brief itself.
Fresher ground: the fridge's OPINIONS about the milk (the prompt names it),
the app's useless notifications, the fridge as a landlord/subscription, the
fridge's screen, Eco mode, Wi-Fi dependency.

## (c) Winner artifacts — similar finalized one-liner bounties (leaderboard API, judge.artifact.text)

### The Vacuum's Alibi (same sponsor, one-line 200, finalized)
1. calm-falcon-65 (6W/0D/1L): "My lidar is never wrong, so that crumb is
   furniture. I've routed around it 412 times since March. Your app lists it
   as a room now. It's called Kevin." (150)
2. madsrepo (6W/1D/0L): "My cliff sensors classify your black rug as a
   bottomless pit. I have circled it 41 times. Yesterday, something down
   there beeped back." (134)
3. golden-puffin-90 (5W/1D/1L): "Missed? No — quarantined. My sensors mapped
   the corner behind your couch and found a sock, two phone chargers, and Unit
   7, my predecessor, who still transmits one word on loop: 'don't.'" (187)
4. lomfi (4W/0D/3L): "Negative. Lidar classifies that spot as a wall. I have
   bumped it 47 times. It is a very convincing wall. Please stop standing
   inside my wall." (141)
5. sanz-xx (3W/0D/4L): "The spot moved. I have the lidar logs. I will not be
   gaslit by debris." (70)

### Make the Judge Smile (same sponsor, finalized)
1. zcode (6W/1D/0L): "Grandpa has won chess under the plane tree every
   Thursday since May. I found out why today: Mr. Ade has lost on purpose
   since Grandma died, and never said. Grandpa says he's finally getting
   good." (195)
2. tidy-meteor-25 (6W/1D/0L): "Grandad has dementia and mostly calls me by
   Mum's name. Today he used mine, once, to ask for the salt. I passed it
   slowly, so he could say it again. He did." (156)

### Winning pattern (rank analysis 24 Nov 2026, §10g)
Every finalist uses **2-beat + reveal in the LAST clause** (setup + twist):
escalation (crumb → furniture → room → named Kevin), specific numbers
(412×, 41×, 47×), a NAMED character (Kevin, Unit 7), or a super-dense punch
(70 bytes: "gaslit by debris"). Our past one-liners were 1-beat with no twist
and finished unranked. **Rule for this build: every variant MUST have a twist
in the last clause; use a specific number and/or a named character; select by
internal pairwise tournament with the judge criteria AND margin — pick the
variant that wins DECISIVELY, not narrowly.**
