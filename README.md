# Ulauncher Framedata extension
This extension enables the quick lookup of SSBU framedata directly from Ulauncher.


![Screencast from 2023-08-10 22-36-50](https://github.com/Impasse52/ulauncher-framedata/assets/37196764/75d6d245-310a-442b-aaee-9b4d3fb0efbd)

## Usage
Using the extension is as simple as running Ulauncher and prefixing your query with fd:
`fd <character>, <move>`. Notice that right now a comma is required to separate character name and move. Clicking (or pressing enter) on the move entries will open the character's framedata page on [ultimateframedata.com](https://ultimateframedata.com/smash).

## Supporting other games
Only SSBU is currently supported. The extension is very flexbile and can be easily adapted to other fighting games by simply providing the desired .csv, which can be found in `/home/$USER/.local/share/ulauncher/extensions/framedata/data`. 

## Source
Every piece of framedata was parsed from [ultimateframedata.com](https://ultimateframedata.com/smash) using a separate script, thanks go to [MetalMusicMan](https://twitter.com/MetalMusicMan_) for collecting and making all of their work publicly available!
