<p align="center">
    <a><img src="./images/icon.png" width=200 height="200"></a>
    <h1 align="center">Fizz</h1>
    <p align="center">
        <a><img src="https://img.shields.io/badge/version-0.1.5-blue.svg" alt="v0.1.5"></a>
        <a href="https://app.deepsource.com/gh/ax-i-om/fizz/" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://app.deepsource.com/gh/ax-i-om/fizz.svg/?label=active+issues&show_trend=true"/></a><br>
        Pop!_OS Configuration Wizard<br>
    </p>
</p>

## Table of Contents

- [Information](#information)
  - [About](#about)
  - [Disclaimer](#disclaimer)
  - [Config Checksums](#config-checksums)
  - [AI Disclosure](#ai-disclosure)
  - [TODO](#todo)

## Information

### About

Fizz is a simple utility for generating bash scripts that automate the provisioning and configuration of systems running Pop!_OS.

### Disclaimer

Fizz comes AS IS with NO WARRANTY and NO GUARANTEES. Per the software license and disclaimer, the developers are not liable for any damages that might result from the usage of Fizz.

> [!CAUTION] 
> Fizz executes commands found within `config.json` with elevated privileges. Ensure that the Fizz utility (`fizz.py`), configuration file (`config.json`) and any generated files (`.sh`) are trusted, as a tainted version may very well lead to system compromise

### Config Checksums

Ensure that the checksums of the configuration file you retrieved from this repository match those displayed below (MD5, SHA1, SHA256, & SHA512 respectively).
```
918c5019a45120052043fad27d4d42b8  config.json
59aca58a283955fb3805cfd91594c4d0c0996d18  config.json
8d76552c2a161dd056c643a661f84cb1810fd2271566bec3f01785e476a5deae  config.json
5a8d7b496c4fd32124cc328101b20bb6bb5e1fe26e4f905ff1d82862ccf06fabffee792b84b225d1330e804c3ade76f4a3089ddfc017fd74908ec27e52b9509f  config.json
```
These checksums will likely be archived in the future for permanent, secure referencing.

### AI Disclosure

The Fizz logo/symbol/mark was generated using OpenAI's DALL-E 2 AI system.

### TODO

+ Add configuration of system preferences (appearance, default applications, etc)
+ Add more modules (lutris, chrome, thorium, brave, gns3, docker-desktop, aliasing, preferences, etc)
+ Implement prerequisite modules?
+ Add progression indicator to generated scripts
+ General code cleanup