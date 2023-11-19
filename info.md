# Haier hOn
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Andre0512/hon?color=green)](https://github.com/hrbek23/hoover)
[![GitHub](https://img.shields.io/github/license/Andre0512/hon?color=red)](https://github.com/Andre0512/hon/blob/main/LICENSE)
[![GitHub all releases](https://img.shields.io/github/downloads/Andre0512/hon/total?color=blue)](https://tooomm.github.io/github-release-stats/?username=Andre0512&repository=hon)  

---

Home Assistant integration for [Haier's mobile app hOn](https://hon-smarthome.com/) based on [pyhOn](https://github.com/Andre0512/pyhon).

---

[![Supported Languages](https://img.shields.io/badge/Languages-19-royalblue)](https://github.com/Andre0512/hon#supported-languages)
[![Supported Appliances](https://img.shields.io/badge/Appliances-11-forestgreen)](https://github.com/Andre0512/hon#supported-appliances)
[![Supported Models](https://img.shields.io/badge/Models-74-yellowgreen)](https://github.com/Andre0512/hon#supported-models)
[![Supported Entities](https://img.shields.io/badge/Entities-315-crimson)](https://github.com/Andre0512/hon#appliance-features)  

## Supported Appliances
- [Washing Machine](https://github.com/Andre0512/hon#washing-machine)
- [Tumble Dryer](https://github.com/Andre0512/hon#tumble-dryer)
- [Washer Dryer](https://github.com/Andre0512/hon#washer-dryer)
- [Oven](https://github.com/Andre0512/hon#oven)
- [Dish Washer](https://github.com/Andre0512/hon#dish-washer)
- [Air Conditioner](https://github.com/Andre0512/hon#air-conditioner)
- [Fridge](https://github.com/Andre0512/hon#fridge)
- [Induction Hob](https://github.com/Andre0512/hon#induction-hob) [BETA]
- [Hood](https://github.com/Andre0512/hon#hood) [BETA]
- [Wine Cellar](https://github.com/Andre0512/hon#wine-cellar) [BETA]
- [Air Purifier](https://github.com/Andre0512/hon#air-purifier) [BETA]

## Configuration

**Method A**: [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=hon)

**Method B**: Settings > Devices & Services > Add Integration > **Haier hOn**  
_If the integration is not in the list, you need to clear the browser cache._

## Examples
_Click to expand..._
<details>
  <summary>Washing Machine</summary>

![Washing Machine](assets/example_wm.png)
</details>
<details>
  <summary>Tumble Dryer</summary>

![Tumble Dryer](assets/example_td.png)
</details>
<details>
  <summary>Washer Dryer</summary>

![Washer Dryer](assets/example_wd.png)
</details>
<details>
  <summary>Oven</summary>

![Oven](assets/example_ov.png)
</details>
<details>
  <summary>Dish Washer</summary>

![Dish Washer](assets/example_dw.png)
</details>
<details>
  <summary>Air conditioner</summary>

![Air conditioner](assets/example_ac.png)
</details>
<details>
  <summary>Fridge</summary>

![Fridge](assets/example_ref.png)
</details>
<details>
  <summary>Wine Cellar</summary>

![Wine Cellar](assets/example_wc.png)
</details>
<details>
  <summary>Air Purifier</summary>

![Air Purifier](assets/example_ap.png)
</details>

## Supported Models
Support has been confirmed for these **74 models**, but many more will work. Please add already supported devices [with this form to complete the list](https://forms.gle/bTSD8qFotdZFytbf8).

|                     | **Haier**                                                                                                                                                                                                                          | **Hoover**                                                                                                                                     | **Candy**                                                                                                               |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Washing Machine** | HW80-B14959TU1DE <br/> HW80-B14959TU1IT <br/> HW80-B14979TU1 <br/> HW90-B14TEAM5 <br/> HW90-B14959S8U1 <br/> HW90G-BD14979UD <br/> HW100-B14959U1 <br/> HW110-14979                                                                | H7W4 48MBC-S <br/> HLWPS495TAMBE-11 <br/> HW 410AMBCB/1-80 <br/> HW 411AMBCB/1-80 <br/> HWE 49AMBS/1-S                                         | CO4 107T1/2-07 <br/> CBWO49TWME-S <br/> RO14126DWMST-S <br/> RO441286DWMC4-07 <br/> HW 68AMC/1-80 <br/> HWPD 69AMBC/1-S |
| **Tumble Dryer**    | HD80-A3959 <br/> HD90-A3TEAM5 <br/> HD90-A2959 <br/> HD90-A2959S                                                                                                                                                                   | H9A3TCBEXS-S <br/> HLE9A2TCE-80 <br/> HLE C10DCE-80 <br/> H5WPB447AMBC/1-S <br/> NDE H10A2TCE-80 <br/> NDE H9A2TSBEXS-S <br/> NDPHY10A2TCBEXSS | BCTDH7A1TE <br/> CSOE C10DE-80 <br/> ROE H9A3TCEX-S <br/> ROE H10A2TCE-07                                               |
| **Washer Dryer**    | HWD80-B14979U1 <br/> HWD100-B14979 <br/> HWD100-B14978                                                                                                                                                                             | HD 485AMBB/1-S <br/> HD 495AMC/1-S <br/> HD 4106AMC/1-80 <br/> HDQ 496AMBS/1-S <br/> HWPS4954DAMR-11                                           | RPW41066BWMR/1-S                                                                                                        |
| **Oven**            | HWO60SM2F3XH                                                                                                                                                                                                                       | HSOT3161WG                                                                                                                                     |                                                                                                                         |
| **Dish Washer**     | XIB 3B2SFS-80 <br/> XIB 6B2D3FB                                                                                                                                                                                                    | HFB 6B2S3FX                                                                                                                                    |                                                                                                                         |
| **Air Conditioner** | AD105S2SM3FA <br/> AS09TS4HRA-M <br/> AS25PBAHRA <br/> AS25S2SF1FA-WH <br/> AS25TADHRA-2 <br/> AS25TEDHRA(M1) <br/> AS35PBAHRA <br/> AS35S2SF1FA-WH <br/> AS35S2SF2FA-3 <br/> AS35TADHRA-2 <br/> AS35TAMHRA-C <br/> AS35TEDHRA(M1) |                                                                                                                                                | CY-12TAIN                                                                                                               |
| **Fridge**          | HFW7720ENMB <br/> HFW7819EWMP <br/> HSW59F18EIPT                                                                                                                                                                                   |                                                                                                                                                | CCE4T620EWU <br/> CCE4T618EW                                                                                            |
| **Hob**             | HA2MTSJ68MC                                                                                                                                                                                                                        |                                                                                                                                                | CIS633SCTTWIFI                                                                                                          |
| **Hood**            | HADG6DS46BWIFI                                                                                                                                                                                                                     |                                                                                                                                                |                                                                                                                         |
| **Wine Cellar**     | HWS247FDU1                                                                                                                                                                                                                         |                                                                                                                                                |                                                                                                                         |
| **Air Purifier**    |                                                                                                                                                                                                                                    | HHP30C011 <br/> HHP50CA001 <br/> HHP50CA011                                                                                                    |                                                                                                                         |

| Please add your appliances data to our [hon-test-data collection](https://github.com/Andre0512/hon-test-data). <br/>This helps us to develop new features and not to break compatibility in newer versions. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Supported Languages
Translation of internal names like programs are available for all languages which are official supported by the hOn app:
* 🇨🇳 Chinese
* 🇭🇷 Croatian
* 🇨🇿 Czech
* 🇳🇱 Dutch
* 🇬🇧 English
* 🇫🇷 French
* 🇩🇪 German
* 🇬🇷 Greek
* 🇮🇱 Hebrew
* 🇮🇹 Italian
* 🇵🇱 Polish
* 🇵🇹 Portuguese
* 🇷🇴 Romanian
* 🇷🇺 Russian
* 🇷🇸 Serbian
* 🇸🇰 Slovak
* 🇸🇮 Slovenian
* 🇪🇸 Spanish
* 🇹🇷 Turkish

## Compatiblity
Haier offers different apps for different markets. Some appliances are compatible with more than one app. This integration only supports appliances that can be controlled via hOn. Please download the hOn app and check compatibilty before you open an issue.   
The apps on this (incomplete) list have been requested so far:

| App             | Main Market   | Supported                               | Alternative                                                                     |
|-----------------|---------------|-----------------------------------------|---------------------------------------------------------------------------------|
| Haier hOn       | Europe        | :heavy_check_mark:                      |                                                                                 |
| Candy simply-Fi | Europe        | :grey_question: (only newer appliances) | [ofalvai/home-assistant-candy](https://github.com/ofalvai/home-assistant-candy) |
| Hoover Wizard   | Europe        | :grey_question: (only newer appliances) |                                                                                 |
| Haier Uhome     | China         | :x:                                     | [banto6/haier](https://github.com/banto6/haier)                                 |
| Haier U+        | China         | :x:                                     |                                                                                 |
| GE SmartHQ      | North America | :x:                                     | [simbaja/ha_gehome](https://github.com/simbaja/ha_gehome)                       |   
| Haier Evo       | Russia        | :x:                                     |                                                                                 |

## Contribute
Want to help us to support more appliances? Or add more sensors? Or help with translating? Or beautify some icons or captions? 
Check out the [project on GitHub](https://github.com/Andre0512/hon), every contribution is welcome!

## Useful Links
* [GitHub repository](https://github.com/Andre0512/hon) (please add a star if you like this integration!)
* [pyhOn library](https://github.com/Andre0512/pyhOn)
* [Release notes](https://github.com/Andre0512/hon/releases)
* [Discussion and help](https://github.com/Andre0512/hon/discussions)
* [Issues](https://github.com/Andre0512/hon/issues)
