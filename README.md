<p align="center">
    <a><img src="./images/icon.png" width=200 height="200"></a>
    <h1 align="center">Fizz</h1>
    <p align="center">
        <a><img src="https://img.shields.io/badge/version-0.1.1-blue.svg" alt="v0.1.1"></a>
        <a href="https://app.deepsource.com/gh/ax-i-om/fizz/" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://app.deepsource.com/gh/ax-i-om/fizz.svg/?label=active+issues&show_trend=true"/></a><br>
        Pop!_OS Configuration Wizard<br>
    </p>
</p>

## Table of Contents

- [Information](#information)
  - [About](#about)
  - [Disclaimer](#disclaimer)
  - [AI Disclosure](#ai-disclosure)
  - [TODO](#todo)

## Information

### About

Fizz is a simple utility for generating bash scripts that automate the provisioning and configuration of systems running Pop!_OS.

### Disclaimer

Fizz comes AS IS with NO WARRANTY and NO GUARANTEES. Per the software license and disclaimer, the developers are not liable for any damages that might result from the usage of Fizz.

> [!CAUTION] 
> Fizz executes commands found within `config.json` with elevated privileges. Ensure that the Fizz utility (`fizz.py`), configuration file (`config.json`) and any generated files (`.sh`) are trusted, as a tainted version may very well compromise your system. 

### AI Disclosure

The Fizz logo/symbol/mark was generated using OpenAI's DALL-E 2 AI system.

### TODO

+ Add configuration of system preferences (appearance, default applications, etc)
+ Add more modules (lutris, chrome, thorium, brave, gns3, docker-desktop, aliasing, preferences, etc)
+ Implement prerequisite modules?
+ Add progression indicator to generated scripts
+ General code cleanup