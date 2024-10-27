# Notion Citation Updater
<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

The **Notion Citation Updater** is a Python script designed to automate the process of updating citation counts for academic papers stored in a Notion database. By leveraging the power of the Scholarly library, this tool searches for publications by title and retrieves their citation information.




<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/Vincia-Jun/Notion-Citation-Updater/">
    <img src="images/logo.png" alt="Logo" width="546" height="235">
  </a>
</p>

![paperbot_demo](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/images/paperbot_demo.gif)

## 📖 Introduction
I use a **Notion database** (tempelate refer to [paper_notion](https://frosted-hacksaw-782.notion.site/81473a1176454a17916de88f22fe79bd?v=ec80ed4fd3b248efbb2c23a8055ef268)) as my literature management tool. However, it can't update citation counts for articles in real time. Therefore, I aim to use Python to implement real-time updates of citation counts.

The **Notion Citation Updater** is a Python script designed to automate the process of updating citation counts for academic papers stored in a **Notion database**. By leveraging the power of the Scholarly library, this tool searches for publications by title and retrieves their citation information. Notion Citation Updater requires configuration in two aspects:
- **Notion Integration:** obtain the API for the Notion database, used to add, delete, query, and modify the database.
- **scholarly:** a Python module for retrieving academic literature information from Google Scholar.

## 🤖 Notion Integration
**Notion integrations** using the API allow you to connect and interact with Notion’s features programmatically.

- **Step1:** Creat your own notion integration from [here](https://www.notion.so/profile/integrations).
- **Step2:** Copy the "Internal Integration Secret", which will be used in Python to access the database.
- **Step3:** Navigate to the database you want your integration to interact with. Connect this page to your previously created integration by clicking the "..." menu in the top-right corner of the page.

Hence, your integration now has access to your dataset/page. You can use Python to interact with this database, performing actions like updating existing entries or creating new pages. For database access and modification operations, refer to the [notion_demo.ipynb](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/notion_demo.ipynb) file. It showcases how to use Python to update the "**Citations**" property value for all pages—for instance, setting it to 99:
![notion_demo](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/images/notion_demo.gif)

## 🔎 scholarly module
**scholarly** is a module that allows you to retrieve author and publication information from Google Scholar in a friendly, Pythonic way without having to solve CAPTCHAs. Here we simply use the following function to retrieve paper information from Google Scholar:
```python
search_query = scholarly.search_single_pub('attention is all you need')
```

You can find the output in the [scholarly_demo.ipynb](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/scholarly_demo.ipynb) file. For more information and a demonstration, please refer to the official repository [scholarly-python-package](https://github.com/scholarly-python-package/scholarly).

## 🚩Quick Start
Make sure you've completed the **Notion Integration** setup and configured **scholarly** as described above. Once done, check your **personal parameters** ( :red_circle: e.g., database_id, integration_token, etc.) in [**paperbot_pool.py**](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/paperbot_pool.py). Then, simply run:
```bash
python paperbot_pool.py
```
Alternatively, you can choose to run the [paperbot_base.py](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/paperbot_base.py) file, though it will be slower than [**paperbot_pool.py**](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/paperbot_pool.py), as [**paperbot_pool.py**](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/paperbot_pool.py) incorporates multithreading for faster processing, while [paperbot_base.py](https://github.com/Vincia-Jun/Notion-Citation-Updater/blob/main/paperbot_base.py) processes tasks in a single thread.

## 🤝 Acknowledgement
This repository provides a simple example workflow for using **Notion** with **Python**. You can easily adapt this code to any scenario in Notion that requires bulk data updates.

Special thanks to Zhihu user [ZZZzzz](https://www.zhihu.com/people/kun-peng-jie-jie) for sharing her Notion-based literature management template. Building on her work, I've further enhanced the efficiency of Notion-based literature management. I hope this brings added convenience to users who rely on Notion for managing their references. If you find this helpful, please feel free to give it a **star**⭐! Wishing you all the best!

<!-- links -->
[your-project-path]:Vincia-Jun/Notion-Citation-Updater
[contributors-shield]: https://img.shields.io/github/contributors/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[contributors-url]: https://github.com/Vincia-Jun/Notion-Citation-Updater/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[forks-url]: https://github.com/Vincia-Jun/Notion-Citation-Updater/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[stars-url]: https://github.com/Vincia-Jun/Notion-Citation-Updater/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/Vincia-Jun/Notion-Citation-Updater.svg
